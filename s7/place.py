"""Song 7 — place 13 single-line voice takes on a one-chord bed.

Prereg: songs/song7-voice-lines-prereg-20261117.md (committed 37757f0 before the
batch was submitted).

Input: one row per line, {key, path, first, last, chars} where first/last are the
first and last voiced sample times measured on the trimmed file (seconds).
Output: a placement plan — each line's absolute start — plus the bed bar count
that makes the final strum land 0.5-2.0 s after the last voiced sample.

Nothing here renders audio. It is the arithmetic that the render will follow,
and it is checked here against known numbers before it is believed:
  - take 2's per-line spans from its ASR segments (a real 13-line read)
  - a synthetic case with a short and a long read
"""
import json
import math
import sys

BPM = 64.0
BEAT = 60.0 / BPM          # 0.9375 s
BAR = 4 * BEAT             # 3.75 s
STRUM_MIN, STRUM_MAX = 0.5, 2.0   # last word to final strum
VOICE_SPAN_MIN, VOICE_SPAN_MAX = 38.0, 60.0   # prereg call: first word to last
PAUSE_TOL = 0.25

# Two things flex, and only these two, chosen before the bed is built:
#   INTRO_BARS 0-2 (bed alone before the first word)
#   the pre-hook pause after L12, 2.0-4.5 s
# Everything else in PAUSES is fixed as preregistered.
INTRO_OPTS = (1, 0, 2)
HOOK_LO, HOOK_HI, HOOK_STEP = 2.0, 4.5, 0.25

# pause after each line, seconds; the shape is fixed
PAUSES = {
    'L01': 0.5, 'L02': 0.5, 'L03': 0.75, 'L04': 2.5,
    'L05': 1.5, 'L06': 2.5, 'L07': 2.5, 'L08': 3.5,
    'L09': 0.75, 'L10': 0.75, 'L11': 0.5, 'L12': None,
}


def _timeline(rows, pauses, hook, intro_bars):
    out = []
    t = intro_bars * BAR
    p = dict(pauses)
    p['L12'] = hook
    for i, r in enumerate(rows):
        dur = r['last'] - r['first']
        start = t - r['first']
        end = t + dur
        out.append({'key': r['key'], 'start': round(start, 4), 'voice_at': round(t, 4),
                    'voice_end': round(end, 4), 'dur': round(dur, 3)})
        if i < len(rows) - 1:
            gap = p.get(r['key'])
            if gap is None:
                return out, [f"no preregistered pause after {r['key']}"]
            t = end + gap
    return out, []


def place(rows, pauses=None, hook_opts=None, intro_opts=None):
    """Search the declared flex (intro bars, pre-hook pause) for a legal plan."""
    p = dict(PAUSES if pauses is None else pauses)
    hooks = hook_opts if hook_opts is not None else [
        round(HOOK_LO + i * HOOK_STEP, 2) for i in range(int((HOOK_HI - HOOK_LO) / HOOK_STEP) + 1)]
    intros = intro_opts if intro_opts is not None else INTRO_OPTS
    best, errs = None, []
    for intro in intros:
        for hk in hooks:
            out, e = _timeline(rows, p, hk, intro)
            if e:
                errs.extend(e)
                break
            last_end = out[-1]['voice_end']
            bars0 = max(1, int(math.ceil((last_end + STRUM_MIN) / BAR)))
            bars = next((b for b in (bars0, bars0 + 1, bars0 + 2)
                         if STRUM_MIN <= b * BAR - last_end <= STRUM_MAX), None)
            if bars is None:
                continue
            gap = bars * BAR - last_end
            plan = {'rows': out, 'bars': bars, 'strum_at': round(bars * BAR, 3),
                    'cut_at': round(bars * BAR + 1.5, 3),
                    'strum_gap': round(gap, 3), 'intro_bars': intro,
                    'pause_L12': hk,
                    'voice_span': round(last_end - out[0]['voice_at'], 3),
                    'total_pause': round(sum((p[k] if p[k] is not None else hk)
                                             for k in list(p) if k in {r['key'] for r in rows[:-1]}), 3),
                    'errors': []}
            plan['span_ok'] = VOICE_SPAN_MIN <= plan['voice_span'] <= VOICE_SPAN_MAX
            # prefer the preregistered one-bar intro, then the shorter piece
            plan['_score'] = (0 if intro == 1 else 1, plan['strum_at'])
            if best is None or plan['_score'] < best['_score']:
                best = plan
    if best is None:
        return {'rows': [], 'errors': errs + [
            f"no legal placement: strum gap {STRUM_MIN}-{STRUM_MAX} s unreachable with "
            f"intro {intros} and pre-hook pause {HOOK_LO}-{HOOK_HI} s"]}
    best.pop('_score')
    return best


def _show(name, plan):
    print(f"--- {name}")
    for r in plan['rows']:
        print(f"  {r['key']} voice {r['voice_at']:6.2f}-{r['voice_end']:6.2f} "
              f"(dur {r['dur']:.2f})")
    print(f"  bars={plan['bars']} intro={plan['intro_bars']} hook_pause={plan['pause_L12']} "
          f"strum={plan['strum_at']} cut={plan['cut_at']} strum_gap={plan['strum_gap']} "
          f"voice_span={plan['voice_span']} span_ok={plan.get('span_ok')} "
          f"pauses={plan['total_pause']}")
    if plan['errors']:
        print("  ERRORS:", plan['errors'])


def _take2_rows():
    """Take 2 per-line spans, from its ASR segment starts/ends (a real read)."""
    starts = [0.28, 2.44, 4.62, 6.94, 9.088, 12.56, 14.34, 15.96, 18.64, 20.94,
              23.96, 26.66, 28.76]
    ends = [2.18, 3.712, 5.952, 8.1, 11.712, 14.2, 15.072, 17.856, 20.16, 23.328,
            25.664, 28.72, 30.0]
    return [{'key': f'L{i+1:02d}', 'first': starts[i], 'last': ends[i],
             'chars': 0} for i in range(13)]


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] != '--selftest':
        rows = json.load(open(sys.argv[1]))
        plan = place(rows)
        json.dump(plan, sys.stdout, indent=1)
        sys.exit(0)

    # 1) the real take-2 read (fast, no air) as durations
    p2 = place(_take2_rows())
    _show('take 2 spans, preregistered pauses', p2)
    assert not p2['errors'], p2['errors']
    assert p2['voice_span'] >= 38, p2['voice_span']

    # 2) a slow, airy read: same lines at 1.6x the duration
    rows = _take2_rows()
    slow = [{'key': r['key'], 'first': 0.0, 'last': (r['last'] - r['first']) * 1.6,
             'chars': 0} for r in rows]
    p3 = place(slow)
    _show('1.6x slower read, same pauses', p3)
    assert not p3['errors'], p3['errors']

    # 3) a read outside the preregistered span band must be flagged, not hidden
    huge = [{'key': r['key'], 'first': 0.0, 'last': 6.0, 'chars': 0} for r in rows]
    ph = place(huge)
    _show('6 s per line (span out of band)', ph)
    assert ph['span_ok'] is False, "a 96 s voice span must not pass the 38-60 s call"

    # 4) a missing pause entry is an error, not a default that gets believed
    pm = {k: v for k, v in PAUSES.items() if k != 'L06'}
    p4 = place(_take2_rows(), pauses=pm)
    assert any('no preregistered pause' in e for e in p4['errors']), p4['errors']
    print('--- selftest OK: strum_gap stays inside 0.5-2.0 s, overshoot and gaps report')