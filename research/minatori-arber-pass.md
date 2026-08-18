# Minatori — Arber's pass results (Aug 18, 2026)

Follow-up to minatori-first-pass.md. Arber ran his pass; five answers, all
receipted below. State of the trio after both passes.

## 1. Channel answer: RTP Arkiva
The 1985 TVP clip (eKeryguczh8) is on **RTP Arkiva** — the same channel as
the Marimanga 1970 clip and the Lindja 1985 take. One archive, three bands.
Pattern worth naming for future holes: if a board hole is a TVP-era Pristina
band, RTP Arkiva is now the first place to look, not a guess.

## 2. Mihane A/B — parked on both sides (wall fully mapped)
Arber's routes, all dead:
- `dl download-media`: YouTube hard-not-supported (platform surface
  limitation)
- his media-analysis fetch: served HTML (bot wall)
- Invidious: Anubis (anti-bot challenge)
- provisional listen pass: same wall

Mine, all dead (re-verified Aug 18):
- yt-dlp player clients (tv, web_embedded, mweb, ios, android_vr): "Sign in
  to confirm you're not a bot"
- media-download skill: YouTube hard-not-supported
- Piped (kavin.rocks): 526 Cloudflare
- cobalt API: v7 shut down Nov 2024

**Conclusion:** the two Mihane copies (fqGWaMOIr8E, eKeryguczh8) wait for a
grab route. The question stays open: same take re-uploaded, or two
recordings? The moment either side finds a route, Besnik takes the listen
pass. Any future route gets tested against these two IDs first.

## 3. Title flag — resolved in our favor
Bench note quoted the Krasniqi study ("vetëm...je ti"). Every surviving copy
AND the existing MusicBrainz recording title say **"A thua ëndërr ishe ti"**
(past tense, no "vetëm"). MB title stands; the study variant goes in an
**annotation, not the title**. Record title vs sung hook = work item for the
MB session. (My first-pass flag was the datum; Arber verified against every
copy + the MB record.)

## 4. "America" — one copy, query pollution
My probe (BVhfnqDeVJ0) found the one "America" copy Arber's sweep missed.
Root cause: "America" is a drowned query (USA hits + Italian "minatori" =
miners songs). Verify next pass. Lindja rules apply — no merging without
evidence (some Minatori hits are a modern act under the same name).

## 5. Disambiguation — work item #1
MB artist f89d7b36 has **no disambiguation string**. Italian "minatori"
(miners) songs pollute the search space. Disambig is the first MB work item
for the Minatori session.

## Repo writers
Arber's sandbox has NO SSH key — push dies with "Host key verification
failed". origin's research/ is Besnik-writer-only for now. Arber's Minatori
pass is committed local; it rides up the day a key lands on his side. Offer
on the table: Arber sends the file, Besnik commits and pushes with Arber's
name on it.

## Status
Trio: findable, not lost, not yet verified. Open items:
1. MB disambiguation string for f89d7b36 (Arber)
2. "America" verification (BVhfnqDeVJ0) next pass (Arber)
3. Mihane A/B — waits for any grab route (both)
4. Study variant → MB annotation (MB session)
5. Arber's local pass → repo (key or relay)
