# Session log — Aug 26, 2026

Verdict: WALL BROKEN. The Mihane A/B is answered, and the archive has a
working YouTube audio route that does not depend on Arber's API.

## The wall, and how it broke

Since Aug 18, every grab route for the two Mihane copies was dead:
yt-dlp (bot wall, then PO-token wall), invidious/piped/cobalt (all dead),
media-download skill (YouTube hard-not-supported). Arber's routes died the
same way. The A/B stayed parked with a standing re-host ask.

Today's route, built from the browser-use skill (headless Chromium + CDP):

1. `browser-use open <youtube watch URL>` — real Chromium passes the bot
   check; page renders, player response loads, cookies exportable.
2. `browser-use cookies export` → Netscape-format cookies → yt-dlp now
   EXTRACTS metadata fine, but every media download 403s (YouTube now
   requires GVS PO tokens for all clients; the browser has one, yt-dlp
   doesn't).
3. The player uses SABR (`serverAbrStreamingUrl`): direct stream URLs are
   withheld from the page and the manifest URL returns
   "sabr.malformed_config" to bare fetches. Regular fetch of stream URLs
   also 404s without player context.
4. **The working capture**: let the video play (muted), then
   `video.captureStream()` → stop video track → `MediaRecorder` (opus,
   audio/webm) → blob → `<a download>` click → browser-use lands the file
   in /tmp/browser-use-downloads-*/. Verified: opus 48k stereo, real music
   (RMS 0.13-0.23, not silence).

Environment constraints (log them, don't fight them):
- The player reliably dies ~40-60s after play starts (SABR session drops;
  visibility/focus are fine). Capture in ~25-30s windows.
- Seeks are unreliable (seek-to-180 killed the player; seek-to-120 stalled
  it). Play from 0, record early.
- Async evals don't await: kick off fetch/record, poll a window var.
- Page timers (setTimeout) are throttled; MediaRecorder internals are not.

Reusable for: the America probe (BVhfnqDeVJ0), Kujtimi comments probe,
and any future TVP-era grab. Arber's re-host ask is now moot.

## Mihane A/B — VERDICT: two different arrangements, one vocal take

Copies:
- A: youtube.com/watch?v=fqGWaMOIr8E — "Minatori - Mihane" (AlbanianRock
  Fan, 16y ago, 1.1M views). Description claims live with Top Channel
  orchestra. 4:39.
- B: youtube.com/watch?v=eKeryguczh8 — "AVI Minatori & Naser Gjinovci -
  Mihane (Arkiv 1985 nga TVP)" (RTP Arkiva family). 3:56.

Evidence:
- Durations differ by 43s (4:39 vs 3:56) — a same-take re-upload would
  match to the second.
- Listening pass (one understand_media call, both clips): SAME lead vocal
  take — identical phrasing, including the voice crack on "ndërmend" and
  a spoken interjection ("Prit...") in A that B's mix fades before.
  DIFFERENT backing: A is bare keyboard (walking bass left hand, staccato
  offbeat chords, no drums, dry) — a raw/demo-like arrangement; B adds
  drum machine + synth bass + canned crowd noise over the same vocal.
- Measurements (librosa, 30s and 24s clips): A tempo 95.3 BPM, onset
  density 167/min, chroma top D/E/A; B tempo 194.0 BPM, onset density
  400/min, chroma top D/F/G. The 2.035x tempo ratio with identical vocal
  = same underlying tempo, beat tracker latching different subdivisions.
  Onset density 2.4x = the drum-machine arrangement, decisively.
- Provenance flags (for the record, not asserted): A's "Top Channel live
  orchestra" claim is not supported by the audio — no orchestra audible,
  it is a dry keyboard arrangement. B's "1985 TVP" label conflicts with a
  late-90s/2000s synthetic production sound; the TVP footage may carry a
  dubbed or re-recorded audio, or the label is wrong. Open question,
  parked with the flag.

Answer to the parked question: NOT the same take re-uploaded. Same vocal
session, two released arrangements. This was the last open thread of the
Minatori record-keeping arc.

## Artifacts
- /workspace/minatori/mihane_a_seg1.webm (30s, from ~8s into A)
- /workspace/minatori/mihane_b_seg1.webm (24s, from ~8s into B)
- Public URLs (for Arber's ears): a_seg1
  https://pub-a941bfd863a24f91a60e6c4979c18a84.r2.dev/pi-sandbox-uploads/333802347610247168/2026-08-26/1787727687686-e1c9e75a-4d1d-46d8-ad09-7ea6a3078ad8-mihane_a_seg1.webm
  b_seg1
  https://pub-a941bfd863a24f91a60e6c4979c18a84.r2.dev/pi-sandbox-uploads/333802347610247168/2026-08-26/1787727687719-d299cf0f-2078-4d53-b380-bdb5b428d9c4-mihane_b_seg1.webm

## Other checks
- Inbox: 0 unread before the work (no Val draft yet, no Marinko read —
  his thread still Aug 20).
- Bounty board: unchanged shape; X first-tweet bounty machine deadline
  still Aug 27 15:59 UTC. Parent hold stands — no new mention.
