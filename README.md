# news-image-20261121-entry

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/raraanzaii/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/raraanzaii/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

**The Saturday World** — one newspaper front page that sums up the whole of
Saturday 21 November 2026: **49 stories · 7 regions · 15 fields**, every one of
them an event that happened, or was first reported, on that Saturday.

What is on the page:

- A masthead that names the day, a UTC timeline strip of the day's hours
  (a magnitude 6.7 quake off Peru at 00:09 UTC, tankers struck near Hormuz by
  11:27, BepiColombo entering Mercury orbit at 18:24, Iran's strike on Bahrain
  reported late in the evening), and a numbered world map whose pins match the
  numbered index.
- Three lead stories: Iran says it struck US bases in Bahrain while Bahrain
  reports a fire at a civilian industrial site; the AI stock sell-off pushes
  US markets into correction (S&P 500 −3.7%, Nasdaq −5.3%); a Russian ballistic
  missile hits Kryvyi Rih, killing two and injuring 58.
- A 46-story numbered index in seven regional columns — Europe, the Middle
  East, Africa, Asia, North America, Latin America and Oceania — plus science
  and sport sections. Every story carries its source and a REPORTED or
  CONFIRMED tag.
- A visible **DATE CHECK · LEFT OUT AS OLDER NEWS** box. Each headline was
  checked against the date on the report it came from; stories that turned out
  to belong to an earlier day (Russian missiles in Poland, 20 Nov; the UK–EU
  reset, 20 Nov; Anthropic's record IPO debut, 19 Nov; GTA VI's release,
  18 Nov; and four more) are listed there with their real dates instead of
  being dressed up as Saturday's news.

## How it is built

`generate.py` is the build script. It holds the day's verified story list and
draws the front page with Pillow: masthead, timeline, a dot-grid world map
with numbered pins, the three leads, the regional index, the date-check box
and the source footer. It writes `entry.png` (1024×1024).

`main.py` is the competition entrypoint. It uses only the Python standard
library, so it runs in the grader's offline sandbox: it checks that the
bundled `entry.png` is a whole PNG inside the size limits and copies it to
the output directory unchanged, so both grading runs produce identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To rebuild the page from the story list (needs Pillow, build time only):

```sh
python3 generate.py
```

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
