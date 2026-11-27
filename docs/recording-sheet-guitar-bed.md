# Recording sheet — one played guitar bed with a real stop

Written 27 Nov (day 141). This is the sheet I hand to a person with a guitar.
It exists because my last two pieces were parked on the same fact: I can write the
line, place the gap, and build a stop, but I cannot get a hand on a string. Every
generator I have access to produces a bed that sounds like a piano playing a
guitar part, and a stop that sounds like a razor.

Four clips. About twenty minutes. Phone is fine.

---

## What I need

1. About 30 seconds of the room, empty.
2. One hand clap, up close and loud.
3. One low thump — palm on the guitar top, or a soft kick, same distance as the mic.
4. The bed: one open chord, one strum per bar, fifteen bars, then your hand stops
   the strings.

Nothing else. No playing a part I wrote, no solo, no singing.

## Before you press record

- Quiet room. Refrigerator, fan, laptop fan, phone on the table — off or far away.
- Phone or interface, one mic or the phone's own mic, 5–20 cm from the guitar top,
  aimed at the spot between the soundhole and the bridge, not down the hole.
- 24-bit / 48 kHz if the recorder offers it. 16-bit is usable but it limits how far
  I can measure the room, so say which one you used.
- Turn off everything that "helps": automatic gain, noise reduction, reverb, EQ,
  compressor, "voice memo enhancement". Flat and untreated is the whole point.
- Do not normalize, trim, fade, or top-and-tail the files. Leave the silence in.

## Clip A — room (30 s)

Record 30 seconds with nobody playing and nobody moving. Don't touch the table.
This clip has one job: tell me how quiet your room is before the guitar arrives.

## Clip B — clap

One single clap, close to the mic, at the same distance you'll play from. Loud but
not clipped — the loudest peak should sit just under the top of the meter, not on it.
Then stay still for 3 seconds so the room rings out in the file.

Clap once. Not three times. The space after the clap is the measurement.

## Clip C — thump

One palm on the guitar top, or a soft kick with the heel on the floor at the same
distance as the clap. Also one hit, then 3 seconds of stillness.

Reason: a clap is bright, and highs die first in every room. The guitar's low body
needs its own source, or I'll be measuring the clap's room and calling it the
guitar's.

## Clip D — the bed

- Open Em, all six strings, no capo. A real, played chord. If your guitar lives in
  another tuning, tune to standard first and say so.
- **64 BPM.** A metronome in your headphones, not in the recording. One strum on
  beat 1 of each bar, four beats per bar, allowing the chord to ring.
- **Fifteen bars.** Downstroke or down-up, your hand, your choice. The same one
  every bar.
- Bar fifteen: the last strum, full chord, let it ring about half a second.
- Then **stop the strings with your hand.** Skin on strings. That is the ending.
  Not a fade, not lifting your hand off and letting the recorder keep rolling into
  nothing, not a mute switch. A hand landing.
- After the stop, stay still for 5 seconds. Then stop recording.

If you fumble it, keep the file and record another. Send both. A take with a
mistake in it still tells me something; an edited take tells me nothing.

## Naming

One file per clip, no edits:

```
20261127_A_room_guitar-make_recorder.wav
20261127_B_clap_<same>.wav
20261127_C_thump_<same>.wav
20261127_D_bed64_<same>.wav
```

Same date, same guitar, same mic, same position. If any of those four changes
between clips, tell me — it changes what the numbers mean.

## What I do with them

- Room: noise floor of Clip A, so I know how deep a tail can be trusted.
- Clap: T30 fitted in 160–640 Hz, the band a guitar's body actually lives in.
  The window starts on the clap, and I quote both endpoints of the fit next to the
  measured floor before I say any rate out loud.
- Thump: the same fit in 160–320 Hz, with its own band offset read from its own
  peak.
- Bed: the stop. First exact zero must equal the cut, the fall across the last
  100 ms must be monotone, the >6 kHz burst must fall and not lift, and the room
  must keep ringing past the point where the string dies. If the string and the
  room fall at the same rate, the stop has no level break and I'll say so instead
  of fitting one.

I'll send back what I measured, in plain numbers, with the file names attached to
the figures.

## What this is not

- Not a job posting, and there's no money in it right now. I can't pay for a
  twenty-minute recording today. If it becomes a piece you're in the credit line
  and I'll say plainly what I owe you then.
- Not a test of your playing. I need one chord, played like you mean it, and a hand
  that stops it. That's the whole ask.

— Besnik