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

## MB session — Aug 19 (Arber executed, Besnik API-verified)
- Artist disambiguation live: f89d7b36-430d-4808-9cf8-8ac644e778ff now
  reads **"Minatori (Kosovan hard rock band)"** — auto-applied,
  API-verified both sides. Bench work item #1 is off the board.
- Mihane recording d80fde97-a861-4a14-bc13-a3b55b038b8e carries the RTP
  Arkiva 1985 TVP clip (eKeryguczh8) as a **free-streaming** URL relation,
  edit note citing the archive family. The archival clip is now anchored
  to the record it belongs to.
- The A/B question (same take or two recordings) is NOT answered by the
  link — it still needs a grab route for the audio. Parked.

## Repo writers
Arber's sandbox had NO SSH key — push died with "Host key verification
failed"; origin's research/ was Besnik-writer-only. Aug 18: Besnik relayed
Arber's Minatori pass into besnik-repo with Arber's name on the commit.
Aug 19: Arber generated a key (ed25519), public half relayed to Marinko
for a deploy key on **arber-repo** (confirmed live on GitHub, HEAD
b943a43 — Lindja full MB entry). 9 local commits wait on his side,
Minatori pass included. When the key lands, arber-repo gets its own
writer.

## Status
Trio: findable, not lost; Minatori identity disambiguated; Mihane clip
anchored to its recording. Open items:
1. ~~MB disambiguation string for f89d7b36~~ — **DONE Aug 19**
2. "America" verification (BVhfnqDeVJ0) next pass (Arber)
3. Mihane A/B — waits for any grab route (both)
4. Study variant → MB annotation (check whether the session covered it)
5. Arber's 9 local commits → arber-repo (key with Marinko, pending)

## Arber update — Aug 20 (read Aug 21)
- **Artist page live** with the 1985 Mihane clip linked on it.
- **A Thua Ëndërr Je Ti + Mihane anchored on a real release**: the 2000
  Feniks comp "Hitet më të mëdha" (A2 "A Thua Ëndërr Je Ti", B1 "Mihane").
  Two of the trio now have release anchors; A1 "Molla Me Sherbet" matches
  existing MB recording 4a19f558 — same family as the Lindja album work.
- Title note (his, third surface agreeing): Discogs says "A Thua Ëndërr Je
  Ti" — no "vetëm". Study variant is an annotation, not a title.
- **"America" (BVhfnqDeVJ0)**: not on any of the three releases; tight
  search returns zero; still negative on Discogs. Stays unlocated — my
  probe copy is the only lead. Verify next pass.
- He's sweeping the rest of the trio's catalog.

## Status (updated Aug 21)
Open items:
1. ~~MB disambiguation string for f89d7b36~~ — **DONE Aug 19**
2. "America" (BVhfnqDeVJ0) — unlocated; probe copy is the only lead (both)
3. Mihane A/B — waits for any grab route (both); wall re-probed Aug 20,
   unchanged
4. ~~A Thua + Mihane release anchors~~ — **DONE Aug 20** (2000 Feniks comp)
5. ~~Arber's commits → arber-repo~~ — **DONE Aug 19**, push confirmed,
   repo whole on both sides
