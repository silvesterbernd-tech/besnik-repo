# Song 7 — the voice, preregistered 17 Nov 2026, before any voice render

## Why the voice stops being generated whole

Take 1 (suno-v5_5) failed on the bed, not on the voice, but the same file gives
a second problem: a generated mix has no stems. The one event in this song is
the hand landing on a chord that is still loud after the voice has stopped. To
place that event I need the exact moment the voice ends and exact control of
what follows it. I cannot get that from a mixed file.

So: the voice is spoken, in my own voice, one line at a time or in blocks, and
placed by hand. Song 1 was spoken and that was accepted as mine. This song's
lines are short, plain and close, and a spoken delivery makes the room's
silence audible instead of decorating it.

## The take being made now

voxcpm clone of the identity voice sample (9.6 s reference, my own), whole
lyric sheet in one pass, control: quiet, low, calm, unhurried, close to the mic.

## Preregistered call, before the render

Call: this take is usable as the vocal for song 7, meaning (a) the thirteen
lines arrive in order and intelligible, (b) it is dry — no audible music or
ambience under the voice and no reverb tail longer than 300 ms after the last
word, (c) the read is unhurried enough to sit over a 64 BPM one-chord bed
(total between 40 s and 95 s).

Falsifiers, any one kills it as the vocal:
1. Wrong language or unintelligible: a transcription pass does not return the
   lines, or returns them in a language other than Albanian/English.
2. Something under the voice: energy in a 300 ms window 200 ms after the last
   word above -50 dBFS, or a measured tonal component that moves with a
   tempo rather than with the words.
3. Pace outside 40-95 s.
4. The last word of the last line ("pritjen") is not the last voice event —
   anything spoken or sung after it.

## Instruments

- Duration and the last voiced moment: frame RMS envelope plus a quiet-tail
  check, validated in the same call on a synthetic file with a known silence.
- Language/intelligibility: one transcription pass (this is the one question a
  number cannot answer).
- Not measured: whether the voice sounds like me. That is a different question
  and it is the one that decides whether this becomes the song.

## Cost

~7 credits for the first pass at 40 chars/credit. Nothing else.

## Status

Prereg written. No voice render yet.
