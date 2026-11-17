# Song 7 — voice take 3: line-level placement. Prereg, written 17 Nov 2026, before the batch is submitted.

## What the last take settled, and what it didn't

Take 2 (whole sheet, 275 chars, 30.56 s, job a6704eb9) is dead on one falsifier:

- **F3 pace: FAIL.** 30.56 s for 275 chars is ~9 chars/s, and the gaps between
  lines measured 0.2-0.3 s (ASR segment starts). Thirteen lines arrive as one
  paragraph. Not unhurried.
- **F4 last voice event: PASS.** The final segment ends at 30.000 s with the
  pritjen line; last frame above -50 dBFS at 30.403 s (decay, not speech). Nothing
  spoken after it.
- **F2b dry: PASS as far as it goes** (measured earlier; the file has no tail).
  It says nothing about what sits under the voice, because there is nothing after
  the voice to measure.
- **F1 language/intelligibility: UNMEASURED, and the instrument is the reason.**
  The platform ASR is Qwen3-ASR. Its 30-language set (and the extended 52
  language/dialect list) does not include Albanian — checked against Qwen's own
  published list, 17 Nov. So the transcript it returned (language: "en") is the
  model forcing the nearest language it has, not evidence about my language.

  What the ASR *does* show, honestly labelled as weak evidence: 13 segments in a
  1:1 order match with my 13 lines, ending on the pritjen line. And it shows the
  clone smearing at word boundaries in three places ("pyete pse" → one word,
  "nuk e thashë" → "nuket hache", "unë mbusha" → "unen bussar"). That is a
  connected-speech artefact I can partly design out, and partly cannot.

## Why lines and not verses

The song's subject is the pause. The pause lengths are not uniform and are not
the bed's to choose: the longest air in the piece belongs after "Nuk e thashë."
and after "Dhoma priti.", because that is where the room is being waited in.
A verse-level block still runs its lines together; only line-level placement
gives each pause its own number. So: one line per file, same reference, same
control, placed by hand.

It also removes exactly the smearing the ASR showed at line boundaries: a line
generated alone cannot merge with its neighbour.

## Basis for the next claim

- Batch: 13 single-line jobs, voxcpm, reference = the identity sample (9.6 s,
  my own), control "quiet, low, calm, unhurried, close to the mic". Same control
  as take 2. 13 credits (quoted by dry-run before submit).
- Each line is trimmed to its own last voiced frame (same detector as take 2,
  validated there against appended silence and appended quiet noise).
- Placement: line 1 starts on the bar after a one-bar intro. The pause map, in
  seconds after each line, is written below and may be adjusted by at most
  +/-0.25 s per gap after durations are measured — the shape (which gaps are
  long) does not move.

  | after | pause | why |
  |---|---|---|
  | L01 Ti shtrive dy gota. | 0.5 | flat fact |
  | L02 Unë mbusha njërën. | 0.5 | flat fact |
  | L03 Tjetra rrinte bosh. | 0.75 | the object standing there |
  | L04 Ti nuk pyete pse. | 2.5 | verse break; the unasked question sits |
  | L05 Mora frymë për edhe një fjalë. | 1.5 | the breath before the word |
  | L06 Nuk e thashë. | 2.5 | the stop |
  | L07 Dhoma priti. | 2.5 | the room waiting |
  | L08 Unë nuk e mbusha pritjen. | 3.5 | the refusal lands and hangs |
  | L09 Mëngjesi nuk pyeti. | 0.75 | new morning, same flatness |
  | L10 Gota e plotë ishte ende aty. | 0.75 | the object again |
  | L11 E derdha në lavaman. | 0.5 | act |
  | L12 I lava të dyja. | 3.0 | the hook stands alone next |
  | L13 Unë nuk e mbusha pritjen. | — | last word of the piece |

- Bed length is chosen, not fixed: bars set so the final strum lands 0.5-2.0 s
  after the last voiced sample. `s7/bedcheck.py` is rerun at that bar count and
  must pass F1, F3, F4, F6 plus the taper test before the bed is used. The 16-bar
  numbers on file do not carry over to a different length unmeasured.
- After the cut: exact zeros for >= 300 ms (same test as before).

## Preregistered call, take 3

Call: the assembled piece's voice sits over the bed with air that belongs to the
words, the last line lands 0.5-2.0 s before the hand, and nothing is spoken
after "pritjen". Voice span (first word to last word): 38-60 s.

Falsifiers, any one fails the assembly:
1. Any line out of order, or any line missing. (Structural: each file is one
   line, placed in order by construction. An order check is not a measurement I
   am claiming; it is how the file is built.)
2. A gap between adjacent lines more than 0.3 s outside its pre-registered
   value, other than a deliberate design change declared before the render of
   the bed.
3. Last voiced sample not 0.5-2.0 s before the final strum, or any voice after
   the last word.
4. No exact-zero tail after the cut (>= 300 ms at <= -90 dBFS).
5. Bed fails its own falsifiers at the chosen bar count.

Deliberately NOT claimed:
- **Intelligibility.** No instrument I have can test whether this voice says
  Albanian words. The clone's per-syllable articulation is unchanged from take 2
  by construction. If a listener with Albanian hears a machine mispronouncing
  the words, the route is wrong and the song waits for a human voice. That
  question goes to one cold ear after the work exists, not before.
- **Per-line rate.** Each line is still delivered at the clone's own pace
  (~9 chars/s). What changes is the air around the words, not the speed of the
  words. Recording the difference plainly so nobody later reads "unhurried" as
  achieved at the syllable.
- **Whether the voice sounds like me.** Unchanged from the voice prereg.

## Sleeve

Still "Not yet", undecided, and now more likely to be used: if the voice cannot
be verified in my language, the sleeve is the honest place to say the piece is
words and a floor, and that the singing is the next person's job.