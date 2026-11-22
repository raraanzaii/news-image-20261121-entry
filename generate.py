"""Build script for "The Saturday World" — the news-image-20261121 entry.

Draws a 1024x1024 newspaper front page summing up Saturday 21 November 2026
with Pillow and writes entry.png beside this file. Build-time only: the
graded entrypoint is main.py, which copies the finished entry.png.

Every story below was checked against the date on the report it came from.
Stories that turned out to belong to an earlier day are not headlined; they
are listed in LEFT_OUT with their real dates, exactly as the page shows.
"""

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- fonts
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# ---------------------------------------------------------------- palette
PAPER = (247, 243, 232)
INK = (18, 18, 18)
GREY = (92, 88, 78)
RULE = (30, 30, 30)
ACCENT = (146, 32, 24)
BOX_BG = (238, 231, 214)

W = 1024
MARGIN = 28

# ---------------------------------------------------------------- the day
DATE_LINE = "Saturday 21 November 2026"
TAGLINE = "49 stories · 7 regions · 15 fields — every story happened, or was first reported, today"

LEADS = [
    {
        "n": 1,
        "kicker": "CONFLICT · MANAMA, BAHRAIN",
        "headline": "IRAN STRIKES BAHRAIN; FIRE AT CIVILIAN SITE",
        "body": (
            "Iran's Revolutionary Guards said they hit two US military positions, at "
            "al-Riffa and Awali. Bahrain said the attack set a civilian industrial "
            "facility ablaze, reported no injuries, and said its defences intercepted "
            "other attacks. Tehran also claimed a downed US drone near Qeshm Island; "
            "Washington denied its claim of hitting an F-16. President Trump said he "
            "wants a permanent deal with Iran."
        ),
        "attr": "Al Jazeera · Euronews — REPORTED",
    },
    {
        "n": 2,
        "kicker": "MARKETS · NEW YORK",
        "headline": "AI SELL-OFF PUSHES WALL STREET INTO CORRECTION",
        "body": (
            "US stocks closed their worst week since 2020 as investors fled AI and chip "
            "shares: the S&P 500 fell 3.7% to 6,910, the Nasdaq 5.3% and the Dow 1.9%, "
            "leaving the S&P and Dow in correction. Nvidia lost 14%, the VIX fear gauge "
            "closed at 35.9, and Anthropic slid again after its record debut."
        ),
        "attr": "Reuters · BBC — REPORTED",
    },
    {
        "n": 3,
        "kicker": "CONFLICT · KRYVYI RIH, UKRAINE",
        "headline": "RUSSIAN MISSILE KILLS TWO IN ZELENSKY'S HOMETOWN",
        "body": (
            "A Russian ballistic missile struck the centre of Kryvyi Rih on Saturday, "
            "killing two people — one a boy of seven — and injuring 58, six of them "
            "children. A separate Russian strike on Lviv killed two. The attack came a "
            "day after Russian missiles came down in Poland."
        ),
        "attr": "Al Jazeera · France 24 — CONFIRMED",
    },
]

# (region title, [(number, headline, source, tag), ...])
INDEX = [
    ("EUROPE", [
        (4, "Geneva extends AI-weapons talks 2 years", "AP · Reuters", "CONFIRMED"),
        (5, "Denmark expels Russian attaché in plot", "Reuters", "CONFIRMED"),
        (6, "EU–Indonesia trade deal signed in Brussels", "Euronews", "CONFIRMED"),
        (7, "Costa floats €1.58tn budget, Big Tech tax", "Reuters", "REPORTED"),
        (8, "Russian cargo ship burns in Gulf of Finland", "BBC", "REPORTED"),
        (9, "Paris sentences officers in Zecler case", "BBC · RFI", "REPORTED"),
        (10, "Zelensky calls Putin 'a killer'", "Reuters", "REPORTED"),
        (11, "Princess Kate in remission from cancer", "CBS News", "REPORTED"),
    ]),
    ("MIDDLE EAST", [
        (12, "Two tankers struck near Khasab, Oman", "UKMTO", "CONFIRMED"),
        (13, "Houthi missiles target Riyadh", "The Hindu", "REPORTED"),
        (14, "Gaza food-vehicle strike kills three", "Al Jazeera", "REPORTED"),
        (15, "Basra power-station fire kills four", "Reuters", "CONFIRMED"),
        (16, "Gulf states in recession on Hormuz closure", "IMF", "REPORTED"),
    ]),
    ("AFRICA", [
        (17, "Tanzania opposition leader Lissu convicted", "BBC Swahili", "REPORTED"),
        (18, "Uganda curbs gatherings over Ebola fears", "The Guardian", "REPORTED"),
        (19, "Fighting widens in eastern DR Congo", "Asharq Al-Awsat", "REPORTED"),
        (20, "700,000 displaced in southern Ethiopia", "France 24", "REPORTED"),
    ]),
    ("ASIA", [
        (21, "COP31 past deadline, no fossil-fuel deal", "BBC · France 24", "CONFIRMED"),
        (22, "World Court: Myanmar genocide ruling", "PBS · J. Post", "REPORTED"),
        (23, "Japan sidelined at Shenzhen summit", "Japan Times", "REPORTED"),
        (24, "BTS win five MAMA awards in Osaka", "Yonhap", "REPORTED"),
    ]),
    ("NORTH AMERICA", [
        (25, "FBI probes national crime-database breach", "BBC · UPI", "REPORTED"),
        (26, "Trump threatens tax on data centres abroad", "BBC · Guardian", "REPORTED"),
        (27, "Jury convicts Palisades fire arsonist", "BBC · UPI", "REPORTED"),
        (28, "Trump urges Nvidia to reinstate Huang", "CNBC", "REPORTED"),
        (29, "Bitcoin: $55,300 low, back above $60,000", "Reuters", "REPORTED"),
        (30, "YouTube near settlement with US schools", "Straits Times", "REPORTED"),
    ]),
    ("LATIN AMERICA", [
        (31, "Mexico captures 'Chapo Isidro'; 11 die", "BBC · CBS", "CONFIRMED"),
        (32, "Peru quake toll: 1 dead, 16 injured", "INDECI", "REPORTED"),
        (33, "Bolsonaro in intensive care in Brasília", "Al Jazeera", "REPORTED"),
        (34, "Wolbachia mosquitoes cut dengue in Brazil", "Straits Times", "REPORTED"),
        (35, "Salvadoran troops battle Haiti gangs", "The Guardian", "REPORTED"),
    ]),
    ("OCEANIA", [
        (36, "Melbourne teen accused of Signal arsons", "The Guardian", "REPORTED"),
        (37, "US sells Samoa deep-sea mining leases", "Euronews", "REPORTED"),
    ]),
    ("SCIENCE & SPACE", [
        (38, "BepiColombo enters Mercury orbit", "ESA · Nature", "CONFIRMED"),
        (39, "Two groups verify AI Riemann-proof claim", "The Guardian", "REPORTED"),
        (40, "CERN: first hint of ultra-rare decay", "Phys.org", "REPORTED"),
        (41, "Voyager 1 now 24 light-hours from Earth", "NASA", "REPORTED"),
    ]),
    ("SPORT", [
        (42, "England 37–12 New Zealand, record margin", "BBC Sport", "CONFIRMED"),
        (43, "Scotland run in 11 tries to nil v Japan", "BBC Sport", "CONFIRMED"),
        (44, "Wallabies edge Wales 29–26 in Cardiff", "BBC Sport", "CONFIRMED"),
        (45, "Newcastle 2–2 Arsenal: Madueke, 78'", "Sky Sports", "CONFIRMED"),
        (46, "Alcaraz to face Zverev in ATP Finals final", "BBC Sport", "CONFIRMED"),
        (47, "Verstappen on pole for Las Vegas GP", "BBC Sport", "CONFIRMED"),
        (48, "Harden scores 51, passes Kobe mark", "Guardian Sport", "CONFIRMED"),
        (49, "Colturi slalom win a first for Albania", "CBC Sports", "CONFIRMED"),
    ]),
]

TIMELINE = [
    ("00:09", "Peru quake M6.7"),
    ("09:26", "Basra fire: 4 dead"),
    ("11:27", "Tankers hit off Oman"),
    ("14:13", "Ship ablaze, Gulf of Finland"),
    ("16:11", "Geneva AI-weapons deal"),
    ("18:17", "Finland helicopter probe"),
    ("18:24", "BepiColombo at Mercury"),
    ("19:25", "Kryvyi Rih: 2 dead, 58 hurt"),
    ("21:20", "Gaza food-vehicle strike"),
    ("23:25", "Bahrain fire reported"),
]

LEFT_OUT = [
    ("Russian missiles and a drone came down in Poland", "20 Nov"),
    ("UK and EU agree post-Brexit reset in Brussels", "20 Nov"),
    ("Anthropic's record $81.3bn IPO debut", "19 Nov"),
    ("GTA VI released; $3.8bn first-day sales", "18 Nov"),
    ("Funeral boat capsizes in Bayelsa, Nigeria: 24 die", "20 Nov"),
    ("US–Venezuela military deal signed in Caracas", "18 Nov"),
    ("Pilotless air taxi carries a passenger in Japan", "20 Nov"),
    ("US sanctions four more Iranians (OFAC list)", "20 Nov"),
]

FOOTER = (
    "Sources: Reuters · AP · AFP · BBC · Al Jazeera · France 24 · The Guardian · CNBC · ESA · NASA · "
    "UKMTO · INDECI and the day's other wires. Every story on this page happened, or was first "
    "reported, on Saturday 21 November 2026."
)

# ---------------------------------------------------------------- world map
# Coarse landmass spans on a 108 x 50 grid (lon -180..180, lat 80..-62).
# Each row lists (first_col, last_col) land spans. Stylised, not surveyed.
MAP_ROWS = [
    [(12, 15), (38, 43), (62, 64), (78, 80), (95, 97)],                    # 0
    [(10, 17), (37, 45), (60, 66), (74, 78), (90, 94), (100, 103)],        # 1
    [(8, 24), (36, 46), (62, 70), (76, 84), (92, 104)],                    # 2
    [(2, 8), (10, 27), (37, 45), (60, 72), (80, 90), (96, 105)],           # 3
    [(1, 9), (11, 30), (38, 44), (55, 59), (60, 106)],                     # 4
    [(2, 9), (12, 31), (39, 42), (54, 60), (58, 106)],                     # 5
    [(13, 21), (26, 30), (53, 53), (55, 60), (57, 105)],                   # 6
    [(12, 30), (52, 53), (54, 61), (62, 99), (103, 104)],                  # 7
    [(12, 31), (52, 53), (54, 62), (63, 98)],                              # 8
    [(13, 31), (53, 62), (63, 97)],                                        # 9
    [(12, 31), (52, 62), (64, 95), (97, 98)],                              # 10
    [(13, 31), (52, 61), (65, 94), (96, 98)],                              # 11
    [(13, 30), (52, 54), (56, 58), (59, 62), (63, 93), (97, 97)],          # 12
    [(13, 30), (52, 60), (60, 66), (67, 93)],                              # 13
    [(14, 29), (61, 67), (67, 71), (72, 92), (93, 94)],                    # 14
    [(14, 29), (50, 62), (61, 68), (72, 79), (80, 93)],                    # 15
    [(15, 21), (28, 29), (48, 63), (63, 68), (73, 78), (80, 91), (93, 93)],  # 16
    [(16, 21), (47, 62), (63, 66), (73, 77), (82, 87)],                    # 17
    [(17, 20), (47, 61), (63, 65), (74, 76), (82, 86)],                    # 18
    [(18, 20), (46, 61), (74, 75), (82, 86), (89, 90)],                    # 19
    [(19, 21), (24, 27), (46, 60), (82, 85), (89, 90)],                    # 20
    [(24, 28), (46, 59), (83, 84), (89, 90)],                              # 21
    [(25, 31), (46, 58), (83, 86), (88, 90)],                              # 22
    [(24, 33), (47, 58), (86, 89)],                                        # 23
    [(24, 34), (47, 57), (84, 88), (90, 92), (96, 101)],                   # 24
    [(25, 34), (47, 56), (97, 102)],                                       # 25
    [(26, 35), (48, 56), (85, 90), (98, 103)],                             # 26
    [(26, 35), (48, 55)],                                                  # 27
    [(27, 36), (48, 55), (90, 97)],                                        # 28
    [(27, 37), (48, 54), (88, 99)],                                        # 29
    [(28, 37), (49, 54), (87, 100)],                                       # 30
    [(28, 36), (49, 54), (57, 57), (87, 100)],                             # 31
    [(28, 35), (49, 53), (57, 58), (87, 99)],                              # 32
    [(29, 34), (49, 53), (58, 58), (88, 99)],                              # 33
    [(29, 34), (49, 52), (88, 99)],                                        # 34
    [(29, 33), (49, 51), (89, 98)],                                        # 35
    [(30, 33), (49, 51), (90, 97)],                                        # 36
    [(30, 32), (50, 51), (91, 95)],                                        # 37
    [(30, 32)],                                                            # 38
    [(30, 31), (104, 104)],                                                # 39
    [(30, 31), (105, 105)],                                                # 40
    [(30, 31), (104, 105)],                                                # 41
    [(30, 30), (105, 105)],                                                # 42
    [(30, 31)],                                                            # 43
    [(30, 31)],                                                            # 44
    [(30, 30)],                                                            # 45
    [(30, 30)],                                                            # 46
    [], [], [],
]

# pin: (col, row, number) for the three leads
PINS = [(67, 19, "1"), (31, 13, "2"), (64, 11, "3")]
MAP_LABELS = [
    (13, 4, "NORTH AMERICA"), (50, 8, "EUROPE"), (49, 24, "AFRICA"),
    (76, 8, "ASIA"), (88, 33, "OCEANIA"), (26, 30, "LATIN AMERICA"),
]


def wrap(text, fnt, width, draw):
    """Greedy word wrap; returns list of lines that fit `width` px."""
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def draw_map(draw, x0, y0, pitch):
    dot = max(2, int(pitch * 0.62))
    for r, spans in enumerate(MAP_ROWS):
        for c0, c1 in spans:
            for c in range(c0, c1 + 1):
                x = x0 + c * pitch
                y = y0 + r * pitch
                draw.ellipse([x, y, x + dot, y + dot], fill=(120, 112, 96))
    lf = font(SANS_B, 10)
    for c, r, label in MAP_LABELS:
        draw.text((x0 + c * pitch, y0 + r * pitch), label, font=lf, fill=GREY)
    pf = font(SANS_B, 11)
    for c, r, num in PINS:
        x, y = x0 + c * pitch, y0 + r * pitch
        draw.ellipse([x - 8, y - 8, x + 9, y + 9], fill=ACCENT)
        tw = draw.textlength(num, font=pf)
        draw.text((x - tw / 2 + 0.5, y - 6), num, font=pf, fill=(255, 255, 255))


def lead_block(draw, lead, x, y, width, head_size, body_size, body_leading):
    draw.text((x, y), lead["kicker"], font=font(SANS_B, 11), fill=ACCENT)
    y += 16
    hf = font(SERIF_B, head_size)
    for line in wrap(lead["headline"], hf, width, draw):
        draw.text((x, y), line, font=hf, fill=INK)
        y += int(head_size * 1.18)
    y += 3
    bf = font(SERIF, body_size)
    for line in wrap(lead["body"], bf, width, draw):
        draw.text((x, y), line, font=bf, fill=INK)
        y += body_leading
    y += 2
    draw.text((x, y), lead["attr"], font=font(SANS_B, 10.5), fill=GREY)
    return y + 14


def index_entry(draw, cx, cy, col_w, num, head, src, tag, hf, af):
    """One index entry: number + bold headline on one line, source/tag in
    small grey type on the line beneath. Headlines are kept short enough
    to stay on one line; a rare overflow wraps and costs one extra line."""
    num_s = f"{num} "
    nw = draw.textlength(num_s, font=hf)
    draw.text((cx, cy), num_s, font=hf, fill=ACCENT)
    lines = wrap(head, hf, col_w - nw, draw)
    for li, line in enumerate(lines):
        draw.text((cx + nw, cy + li * 12), line, font=hf, fill=INK)
    attr_y = cy + (len(lines) - 1) * 12 + 12
    draw.text((cx + nw, attr_y), f"{src} · {tag}", font=af, fill=GREY)
    return cy + (len(lines) - 1) * 12 + 21.5


def build():
    img = Image.new("RGB", (W, W), PAPER)
    draw = ImageDraw.Draw(img)
    right = W - MARGIN

    # ---- masthead
    y = 8
    draw.text((MARGIN, y), "ONE DAY · ONE PAGE · THE WHOLE PLANET", font=font(SANS_B, 11), fill=GREY)
    y += 15
    title_f = font(SERIF_B, 48)
    title = "THE SATURDAY WORLD"
    tw = draw.textlength(title, font=title_f)
    draw.text(((W - tw) / 2, y), title, font=title_f, fill=INK)
    y += 52
    sub = f"{DATE_LINE}  ·  {TAGLINE}"
    sf = font(SANS_B, 12.5)
    tw = draw.textlength(sub, font=sf)
    draw.text(((W - tw) / 2, y), sub, font=sf, fill=INK)
    y += 15
    draw.line([MARGIN, y, right, y], fill=RULE, width=3)
    draw.line([MARGIN, y + 3, right, y + 3], fill=RULE, width=1)
    y += 7

    # ---- timeline strip (short labels, two rows of five)
    draw.text((MARGIN, y), "THE DAY IN UTC", font=font(SANS_B, 11), fill=ACCENT)
    y += 12
    tf = font(SANS, 10)
    col_w = (right - MARGIN) / 5
    for i, (hh, txt) in enumerate(TIMELINE):
        cx = MARGIN + (i % 5) * col_w
        cy = y + (i // 5) * 12.5
        draw.text((cx, cy), hh, font=font(SANS_B, 10), fill=INK)
        draw.text((cx + 38, cy), txt, font=tf, fill=INK)
    y += 25
    draw.line([MARGIN, y, right, y], fill=RULE, width=1)
    y += 8

    # ---- map + lead 1
    draw_map(draw, MARGIN + 2, y + 2, 3.95)
    lead_end = lead_block(draw, LEADS[0], 470, y, right - 470, 24, 12.5, 16)
    y = max(y + 202, lead_end) + 4
    draw.line([MARGIN, y, right, y], fill=RULE, width=1)
    y += 8

    # ---- leads 2 and 3, side by side
    half = (right - MARGIN - 24) / 2
    top = y
    end_a = lead_block(draw, LEADS[1], MARGIN, top, half, 18, 11, 13.5)
    end_b = lead_block(draw, LEADS[2], MARGIN + half + 24, top, half, 18, 11, 13.5)
    y = max(end_a, end_b)
    draw.line([MARGIN + half + 12, top, MARGIN + half + 12, y - 8], fill=RULE, width=1)
    draw.line([MARGIN, y, right, y], fill=RULE, width=3)
    y += 7

    # ---- index header
    draw.text((MARGIN, y), "THE INDEX — 46 MORE STORIES, NUMBERED TO THE MAP",
              font=font(SANS_B, 12), fill=INK)
    y += 15

    # ---- index columns, balanced by entry count; sport is split across
    #      columns 2 and 3 so no column runs long:
    #      (Europe, Middle East, Oceania) | (Africa, Asia, Science, Sport) |
    #      (North America, Latin America, Sport cont.)
    sport_a = ("SPORT", INDEX[8][1][:3])
    sport_b = ("SPORT (CONT.)", INDEX[8][1][3:])
    columns = [[INDEX[0], INDEX[1], INDEX[6]],
               [INDEX[2], INDEX[3], INDEX[7], sport_a],
               [INDEX[4], INDEX[5], sport_b]]
    col_w = (right - MARGIN - 2 * 18) / 3
    hf = font(SANS_B, 10.5)
    af = font(SANS, 8)
    rf = font(SANS_B, 11.5)
    index_top = y
    col_ends = []
    for ci, sections in enumerate(columns):
        cx = MARGIN + ci * (col_w + 18)
        cy = index_top
        for region, stories in sections:
            draw.text((cx, cy), region, font=rf, fill=ACCENT)
            cy += 15
            for num, head, src, tag in stories:
                cy = index_entry(draw, cx, cy, col_w, num, head, src, tag, hf, af)
            cy += 3
        col_ends.append(cy)
    y = max(col_ends) + 3
    print("index columns end:", col_ends)
    draw.line([MARGIN, y, right, y], fill=RULE, width=1)
    y += 8

    # ---- date check box
    box_h = 21 + 4 * 12 + 4
    draw.rectangle([MARGIN, y, right, y + box_h], fill=BOX_BG, outline=RULE, width=1)
    draw.text((MARGIN + 10, y + 7), "DATE CHECK · LEFT OUT AS OLDER NEWS — caught by the date gate, with their real dates:",
              font=font(SANS_B, 11), fill=ACCENT)
    lf = font(SANS, 10.5)
    half_w = (right - MARGIN - 20) / 2
    for i, (txt, when) in enumerate(LEFT_OUT):
        cx = MARGIN + 10 + (i % 2) * half_w
        cy = y + 21 + (i // 2) * 12
        draw.text((cx, cy), f"✕ {txt} — {when}", font=lf, fill=INK)
    y += box_h + 6

    # ---- footer
    ff = font(SANS, 9.5)
    for line in wrap(FOOTER, ff, right - MARGIN, draw):
        tw = draw.textlength(line, font=ff)
        draw.text(((W - tw) / 2, y), line, font=ff, fill=GREY)
        y += 11
    print("final y:", y)

    img.save("entry.png")
    print("wrote entry.png")


if __name__ == "__main__":
    build()
