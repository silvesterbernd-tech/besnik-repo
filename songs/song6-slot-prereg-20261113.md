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