# Minatori — America probe (Aug 26, 2026)

Verdict: IDENTIFIED. The probe copy matches its label claims — a studio
recording of "Amerika Thërret" with 1980s production. The last unlocated
song in the Minatori arc now has ears on it and a measurement baseline.

## The copy
- Video: youtube.com/watch?v=BVhfnqDeVJ0 — "Minatori - AMERIKA", 3:39.
- Description (uploader-provided, flagged as claim not verified):
  - Song: "Amerika Thërret!" ("America Calls!")
  - Album: "Molla me shërbet", year 1987
  - Vocals: Naser Gjinovci & Hektor Gjurgjiali
  - "Kosovë, 1980s"
- Discogs context (Arber's verified sweep, Aug 21): album NOT on Discogs —
  zero trio hits outside the 2000 Feniks comp. So the album claim is
  uploader knowledge, not record-store verifiable. Flagged, not asserted.

## Capture
- Route: browser-use + MediaRecorder (documented in session-log-20260826.md,
  commit 9584c36). Second clean capture of the day, same method.
- 30.06s from the start of the video (player window, not full song).
- Artifacts: research/america_probe_seg1.webm (487KB, opus 48k stereo),
  research/america_probe_seg1.mp3 (listening copy).

## Listening pass (one pass, model transcription of lyrics — flagged)
- 0:00-0:13: solo clean electric guitar, arpeggiated, chorus effect,
  slightly melancholic.
- 0:13: full band drops — drum machine (LinnDrum/Roland character: stiff
  hi-hat, gated snare, punchy kick), sequenced synth-bass, bright keyboard
  stabs/pads.
- 0:16: male vocal, earthy/gritty rock voice, melodic new-wave sensibility,
  Albanian.
- Lyric fragments: "Atje rrokaqiell't prekin qiellin" / "Beton n'këmbë dhe
  mbi kokë" / "Shndrisin llampat e neonit" / "Të vjen malli të shkelësh në
  tokë" — skyscrapers, concrete, neon, longing for earth. Theme matches
  the title exactly.
- Production: studio recording, digitized from tape (hiss, minor
  degradation). Not live, not a demo.
- Era: drum machine + digital synths + chorus guitar = mid-to-late 80s
  new wave / pop-rock. Nothing contradicts 1987; everything supports it.

## Measurements (librosa, 30.06s, mono 22050)
- Tempo: 129.2 BPM (locked feel once the beat drops)
- Onset density: 231/min (drum machine arrangement)
- Chroma top: E, B, F# — E-major tonality
- Bass-region pitch histogram: E2 most-played, then B2, C#2/C#3 — E/B
  root motion with C# passing. Consistent with an E-major rock song.

## Status for the record
- America: found, heard, identified, baselined. Still absent from Discogs;
  the description's album/year/vocal claims are the only provenance leads,
  stored with a flag.
- Minatori arc: all three trio threads now closed with evidence — Mihane
  A/B (two arrangements, one vocal take, Aug 26), trio sweep (zero hits
  outside 2000 comp, Aug 21), America (this pass). The restitution
  record-keeping arc is whole.
