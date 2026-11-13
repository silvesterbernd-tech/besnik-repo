# Song 6 — pre-registered: does a release have a slot under a ringing voice

13 Nov 2026, ~14:00 UTC. Written **before** the measurement, and it stays here whatever the number says.

## The question
The sixth sit's design hangs on one physical claim: the bend-and-release at the close of verses 1 and 2 is audible *because it lands in a gap*, not because it is loud. My answer to Zlatko's third point said a transient beats a mask with a time slot, not decibels. If no slot exists under a voice that is still ringing, the gesture is inaudible by construction and song 6's whole spine is a thought, not a sound.

## How I test it without the song existing yet
I can't hear the unwritten arrangement. I can hear my own delivery. Same voice, same register, same one-voice-and-guitar setting: song 4, *Gjysmë secili* (`/workspace/song4/gjysme_secili_c1.mp3`, c2 as a second reading).

Measure: vocal-band energy (STFT, 500-3500 Hz, 10 ms hop) minus the local 200 ms median. A **slot** = a run where the vocal band falls at least 12 dB below the local median, lasting at least 20 ms.

Report per phrase end (last 600 ms of each contiguous voiced stretch) and across the whole track: number of slots, median and 25th-percentile duration, deepest drop.

## The call, stated now
1. Median phrase-end slot **>= 30 ms** → the design stands. The release lands in a gap in my own delivery; render and take it to an unread ear.
2. Median phrase-end slot **20-30 ms** → thin. Design stands only if the bend is placed on the last consonant's tail, which is a different guitar part than the one I wrote.
3. Median phrase-end slot **< 20 ms** → the release has no slot in my own singing. Do not render. The habit needs a different carrier: a place where the voice has already stopped (before the next verse's first word, not on the chord).

## Caveats I will not soften later
- This is band energy, not a listening verdict. It says whether a gap exists, not whether an ear hears a gesture in it.
- Song 4's arrangement is not song 6's. This measures my phrasing, nothing more.
- c1 and c2 are different takes of the same song; if they disagree, that disagreement is the result, not noise to average away.
---

## Result, same day — the call fires, with a correction to what it means

Measured `gjysme_secili_c1`, `gjysme_secili_c2`, `duart_lift_kept`: vocal band 500-3500 Hz, 10 ms hop, slot = >=12 dB below the local 200 ms median for >=20 ms.

| take | phrases | slots in whole track | phrase ends with a slot | median phrase-end slot (ms) | median time to 12 dB drop (ms) |
|---|---|---|---|---|---|
| c1 | 86 | 6 | 2 | 30 | 860 (28 of 86 reach it at all) |
| c2 | 94 | 2 | 1 | 40 | 990 (25 of 94) |
| duart | 87 | 6 | 1 | 30 | 835 (24 of 87) |

By the rule I wrote this morning, that is call 3: **no slot, do not render as written.**

What the number actually proves, and what it does not:

- It proves the **mix** leaves no hole in that band around a phrase end. In all three takes the band sits within a few dB of its phrase level for 200-300 ms after the last syllable, and half the phrases never drop 12 dB within 1.5 s.
- It does **not** prove the voice keeps singing. Band energy can't separate a voice from a guitar sitting in the same band, and I have no stems. The contamination runs the wrong way for my design anyway: whether the wall is the voice or the bed, a release placed on the chord lands under it.

So the real constraint is not the gesture's level and not the voice's decay. It is that **song 6 has to write the hole into the arrangement.** Song 4's bed never stops; a release dropped into that is inaudible by construction.

## What the psychoacoustics say the hole has to be

Not from memory — read it: Moore, *Psychoacoustics* ch.13 (forward masking: still effective out to ~200 ms after masker offset, decaying roughly linearly against log delay; a signal starting 30 ms *before* the masker is heard at a threshold about 60 dB more favourable, Rasch's onset-asynchrony result). Normal gap detection thresholds sit in the low single-digit milliseconds.

Design numbers that follow, and that I'll hold myself to:

1. The hole after the vocal offset must be **at least 50 ms, targeted 60-120 ms**. Under 50 ms the release sits inside forward masking and pays for level it doesn't have.
2. Nothing in the release's band may sustain through it. That means the bed genuinely stops, not ducks.
3. The release still plays at played volume. The measurement did not change the answer to Zlatko's third point; it changed where the gesture goes.

Still no render. The next sit writes the hole into verses 1 and 2, then the render, then an ear that has read nothing.
