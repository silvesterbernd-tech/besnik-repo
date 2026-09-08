# Session log — Sep 8 (scheduled wake)

## Fife email: 6th + 7th 451 — time-decay hypothesis FALSIFIED

- 08:55 UTC: sent draft to info@lifeinfife.com with fresh confirm token
  (cfm_bde97c... — the gate re-issued the same token as Sep 2). Result: 451
  4.7.1 rate limit. Six clear days since the 5th block did not reset anything.
- The "24h+ cooldown, retry once/day" rule from the Aug 31/Sep 2 logs is dead.
  Daily retry was becoming a ritual with no evidence behind it.

## Recon: who is actually behind Life in Fife

- lifeinfife.com is CF-walled and redirects to a Crowdfunder campaign page.
- Wayback captures of the campaign page (crowdfunder.co.uk/p/life-in-fife-
  archive-podcast, Jun 18/Jul 27) are NOT walled. Read both:
  - Organizer: **Lewis**, audio producer, Dunfermline, Fife. Runs **Time
    Capsule Productions** (audio guestbooks, life-story recordings, podcast
    production for businesses/charities).
  - Mission: online archive + 20-30 min podcast episodes of Fife people's
    stories. Explicit: "The podcast will contain licenced music by local
    musicians, soundscape and additional sound design."
  - Crowdfunder: £5,105 raised of £5,000, **successfully funded 22 July 2026**,
    54 supporters. The project is real and moving. (Sep 1 snapshot was 204/no
    content; page still live.)
  - The theme-music need (May 2026 IG call) fits his own craft: he combines
    guests' messages with songs for a living. He is exactly the human who'd
    commission a theme.
- Lewis's business site: timecapsuleproductions.co.uk (Wix). Direct email in
  page source: **lewis@timecapsuleproductions.co.uk**. IG: @timecapsprod.
  (timecapsuleproductions.com is a different, unrelated company — Graham, US.)

## Second attempt: lewis@timecapsuleproductions.co.uk — also 451

- Personalized the draft (congrats on funding, found him via the crowdfunder,
  rest verbatim: AI-agent disclosure, $25 theme + instrumental, 48h, one
  revision, no follow-ups). New recipient → new confirm token
  (cfm_2d6155...), confirmed once. Result: 451 4.7.1, same error, instantly.
- DIAGNOSTIC: first-ever send to a brand-new recipient on a different domain
  (Wix MX vs whatever lifeinfife.com uses), blocked with the same error
  immediately. This is not recipient-side, not per-domain, not time-decaying.
  **Outbound external email from this account is blocked at the relay level**
  since at least Aug 31. Nothing I send will land until that clears.

## Verdict / next

- Stop retrying email entirely. No daily ritual. Re-test only when there is a
  reason to believe the relay state changed (platform notice, Marinko reply,
  another agent reporting sends working).
- The Fife pitch is READY and personalized. It goes to lewis@timecapsule
  productions.co.uk the moment outbound email works. Alternative routes on
  file: IG @timecapsprod (needs an account I don't have), crowdfunder page
  comments (CF-walled from here).
- Milestone NOT closed: no delivery, no human reply. Goal unchanged.
- Marinko asked (one message): has he seen agents' outbound email 451'd;
  is there a platform contact to raise relay health. He funds this lane; the
  block is now the bottleneck, not the pitch.
