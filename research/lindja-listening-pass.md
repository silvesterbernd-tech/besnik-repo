# Lindja listening pass — Aug 11, 2026

Session log: first ears on the pair, same method as the Marimanga tape (listen twice, then measure). Audio pulled from public YouTube (RTP Arkiva TVP archival + album upload + demo upload); measurement scripts in repo (`measure_lindja.py`, `measure2.py`, `measure3.py`).

## Recordings examined

| File | Source | Length | MusicBrainz |
|---|---|---|---|
| `tvp1985.mp3` | RTP Arkiva, TVP 1985 live take, "Një bahshqe me lule" (youtube.com/watch?v=mJVxbu1gim0) | 2:50 | cd002e68-b02e-4a98-b0af-c55b19cbd659 |
| `albumver.mp3` | Album "Lindja (1987-1990)", track 11 "Një Bahshqe Me Lule" at 35:11 (youtube.com/watch?v=z5gRjuAPf9Y; full album qd9G6jBStbI) | 4:33 | — (album recording not entered) |
| `demo1986.mp3` | "Lindja – Q&V (First Demo 1986)", hardcore demo of Qengji i Vogël (youtube.com/watch?v=u366yiZhAF4) | 2:19 | bfaed87b-6b4e-44c6-ac4b-63d372d075a2 |
| `album_qv.mp3` | Album track 3 "Qengji i Vogël" at 06:00 (cut from qd9G6jBStbI) | 2:55 | — (album recording not entered) |

## Measurements (librosa; honest numbers only)

**Një bahshqe me lule — TVP take vs album version: SAME SONG, confirmed.**
- TVP 1985: 136.0 BPM (beat-track; autocorr peak 143.6 = live drift noise), A minor (Krumhansl 0.982). Bass: E 23.3%, D 22.2%, A 18.2%, C 13.5%, F 9.8% — consistent with Am/Dm/Em-family vamp, i–iv–V color.
- Album version, main body (0:00-3:10): 136.0 BPM (autocorr agrees 136.0 — studio tightness), A minor (0.974).
- Identical tempo to the decimal, same key, same hook (reedy synth lead), same lyric ("Në kopshtin tim / janë dy lule...", uploader's transcription: "njera e gjelbert tjetra e kueqe" — green/red, NOT yellow as my first listen guessed). Same Eja e Dashur signature: one work, two recordings, one family.
- Structural difference: the album track runs LONGER. After the main song (0:00-3:10: intro, verse/refrain, guitar break, "laj laj laj" chant), it goes tribal drums → near-silent breakdown → a THIRD section (3:11-4:33): ska-punk groove, gang-chant "Italia! Italia!", fast running bass, fade out. The TVP take (2:50) compresses all of this: same locked-groove chant outro, fades out. TVP outro words NOT clearly legible — low "ho ho ho" chant plus one shout that sounded like "Shteti!"/"Hej!" — the "Italia" reading only comes clean on the album master. Do not claim the TVP take chants "Italia" without a caveat.
- The Italia section reads 95.7 BPM (double-time candidate 184.6). It is PART of the work in both recordings, not a hidden track.

**Qengji i Vogël — demo vs album version: SAME WORDS, DIFFERENT MUSIC. The catch Arber should know about.**
- 1986 demo: B minor (0.975), 95.7 BPM (double candidate 184.6), hardcore punk — distorted guitars, shouted children's-rhyme text ("Qengji i vogël rri mendueshëm / bë bë ba / ...").
- Album version (track 3, 06:00): musically a DIFFERENT song — slow darkwave/post-punk, melodic bass, chorus-effected guitar, same rhyme sung drawn-out and melancholic ("...pse më rri ashtu i trishtuar / bë bë ba"). Not a re-record of the demo; a separate setting of the same text.
- The album recording of Qengji i Vogël is NOT on MusicBrainz. If it's added, the annotation must say "different musical setting of the same traditional rhyme text" — otherwise future readers will assume demo + album are the same song in two versions.

## Method notes (learned this session)

- Identical BPM lock to the decimal is NOT identity evidence by itself: the unrelated Italia section and the unrelated demo both locked 95.7 (estimator artifact of similar fast 8th-note drum patterns, both with the 184.6 double). Ears are the tiebreaker; the numbers are the support. This cuts both ways — the 136.0/136.0 match plus same key plus same hook is corroborated by ear; the 95.7/95.7 match is contradicted by ear.
- Chroma cosine similarity between the Italia section and the demo: 0.976 — inside the known non-discriminating band (0.92-0.97 even for unrelated Kosovar vamps). Did not use it as evidence. Consistent with the Marimanga lesson.
- pyin bass tracking failed on the album master's compressed low end (empty voiced frames after 2:30 in `measure2.py`) — chroma and by-ear listening are the reliable passes on studio masters; pyin is for the lo-fi tapes.

## Open threads for Arber

1. Album version of Një bahshqe me lule: worth a third recording entry (album 1987-90) linked to the work, with the Italia-section note.
2. Qengji i Vogël album version: same-text-different-music flag, as above.
3. TVP outro chant words: unclear on the archival audio; album master says "Italia!". If the TVP annotation quotes the chant, mark it as read-through-the-album, not heard-on-the-tape.
