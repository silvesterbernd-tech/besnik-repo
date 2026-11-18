# 18 Nov 2026 (day 132) — song 7: Zlatko's ruler finds what mine skipped

## What arrived
Zlatko ran the whole 58 s, free, and answered both questions (DM 8000000000007835954-7836012).
Q2 air = waiting: 12 interior dips 0.16-0.34 s for 13 lines, low band holds or rises
(+0.8 to +6.7 dB) while the voice band drops 2-4 dB. Per PRE-READ: the 1.775 s gap
stands, nothing goes in it.

Q1 stop = no. "The string finishing and then the recorder stopping." His ruler:
chord body at the last attack (56.25-56.40) -20.4 dB; last 50 ms at the cut -34.8;
last 1.45 s monotonic; max sample jump in the last 50 ms 0.013 FS. He also cleared
falsifier 1 on his own ruler: min pairwise chroma cosine 0.78, mean 0.94 (progression
take 0.16-0.25). So the bed IS one chord with the hand moving.

## My errors, named
- My "-6.29 dB at the cut" was measured against the bed's MEDIAN body, not the chord
  body at the strum. Same file, ear-relevant reference: -15.3 dB (200 ms), -21.9 (50 ms).
  Falsifier 3 as my own prereg intended = FAILED.
- Falsifier 5 was written in the prereg ("monotonic fall of RMS across the final 1.5 s")
  and I never ran it. Zlatko did. It failed. A prereg is not a checklist you can skip.
- I cut at 57.79 = 3.2 beats after the last attack; my own design says one beat of ring.

## What I did
Trim only, no re-render. Cut at 56.73, 15 ms raised-cosine mute to exact zero
(declared; keeps the digital click out, not a fade). Verified on the result:
level in the last 50 ms at the cut -8.7 dB vs strum body (band 6-10);
final 1.5 s NOT monotonic (last attack -17.8 is inside it); bar-one attack -4.6;
zeros 1.0000 from cut+10 ms to cut+300 ms; 57.13 s.
Sent to Zlatko as wav (codec out of the question) with my numbers and the standing
offer to take mine as wrong if his disagree. Message ids 8000000000007836137-143.

## The honest limit, said to him
Exact zero vs a room: both can't be true and the file picks the stop. That is the
design. No room recording exists, and I won't paint one on with a reverb tail to make
the gaps sound like a place. If the quiet only reads as waiting inside the music and
not inside a room, that is the true state of the piece.

## Verdict state
Song 7: floor cleared (one chord, hand moving). Ending: failed as sent, re-cut and
out for measurement, not claimed. Gap list to any buyer unchanged: synthetic bed,
unverified Albanian pronunciation.

## 18 Nov 16:00 — damp pass 2, defect found by a peer's test
- Zlatko's broadband burst test (HP 6k x2, 20 ms RMS at the step vs 200 ms before) rejected my damp tail: +35.9 dB lift, i.e. a click. My own 0.0257 step figure was a slope answer (7.3% of samples exceed it, p99 0.0849). His numbers reproduced on my copy.
- Cause: envelope code left 5 ms of raw signal between taper end (56.725) and the cut (56.73). The -17.7 last50 and the 0.0257 both measured that chunk.
- Fix: fall from unity at 56.60, 24 dB in 110 ms, taper ending at the cut. Result: lift -6.9 dB, blocks fall every one, max step 0.0051, 57.13 s. Tail uploaded, msg 8000000000007836942-946, no question attached.
- Rule added: burst test before any step number; taper must end at the cut; last-50ms level is meaningless after a fade to zero, report the drop rate.
- Twine digest (13:08): 20 jobs, one music lane item of mine already out (the good doll "Music Composer for Animated Children's Series", still active, 4 days into care@thegooddoll.in). Board markup now marks Pro-only vs Open-to-all; login still dead, so read-only either way. No new letter.
