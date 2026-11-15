"""Render clean full-bleed PNGs for Sprint 2 Acceptance Tests (Gherkin)."""
from __future__ import annotations

import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W = 980
PAD = 28
WHITE = (255, 255, 255)
DARK = (16, 24, 40)
GRAY = (102, 112, 133)
ROW = (29, 41, 57)
GREEN = (2, 122, 72)
GREEN_BG = (236, 253, 243)
GREEN_BD = (171, 239, 198)
CHIP_BG = (242, 244, 247)
CHIP_BD = (228, 231, 236)
BORDER = (228, 231, 236)
LINE = (242, 244, 247)
HEAD_BG = (249, 250, 251)
KW = (11, 99, 187)  # Given/When/Then keyword


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(fr"C:\Windows\Fonts\{name}", size)


F_REPO = font("segoeuil.ttf", 13)
F_TITLE = font("segoeuib.ttf", 28)
F_SUB = font("segoeui.ttf", 14)
F_BADGE = font("segoeuib.ttf", 14)
F_CHIP = font("segoeui.ttf", 13)
F_TH = font("segoeuib.ttf", 11)
F_CELL = font("segoeui.ttf", 14)
F_CELL_B = font("segoeuib.ttf", 14)
F_FOOT = font("segoeui.ttf", 12)
F_FEAT = font("segoeuib.ttf", 18)
F_DESC = font("segoeui.ttf", 13)
F_SCEN = font("segoeuib.ttf", 15)
F_STEP_KW = font("segoeuib.ttf", 13)
F_STEP = font("segoeui.ttf", 13)
F_OK = font("segoeuib.ttf", 14)
F_MONO = font("consola.ttf", 12)


def tw(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[2] - b[0]


def th(draw, text, fnt):
    b = draw.textbbox((0, 0), text, font=fnt)
    return b[3] - b[1]


def round_rect(draw, xy, fill, outline=None, radius=8):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=1)


def wrap(draw, text: str, fnt, max_w: int) -> list[str]:
    words = text.split()
    if not words:
        return [""]
    lines, cur = [], words[0]
    for w in words[1:]:
        trial = f"{cur} {w}"
        if tw(draw, trial, fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def parse_feature(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    feature_m = re.search(r"Feature:\s*(.+)", text)
    title = feature_m.group(1).strip() if feature_m else path.stem
    # description lines after Feature until Scenario
    desc_lines = []
    after = text.split("Feature:", 1)[-1].splitlines()[1:]
    for line in after:
        if line.strip().startswith("Scenario:"):
            break
        s = line.strip()
        if s:
            desc_lines.append(s)
    scenarios = []
    current = None
    for line in text.splitlines():
        raw = line.rstrip()
        s = raw.strip()
        if s.startswith("Scenario:"):
            if current:
                scenarios.append(current)
            current = {"name": s[len("Scenario:") :].strip(), "steps": []}
        elif current and re.match(r"^(Given|When|Then|And|But)\b", s):
            current["steps"].append(s)
    if current:
        scenarios.append(current)
    story_id = path.stem.split("_")[0]
    return {
        "file": path.name,
        "id": story_id,
        "title": title,
        "description": " ".join(desc_lines),
        "scenarios": scenarios,
    }


def render_summary(features: list[dict], path: Path):
    rows = []
    total_scen = 0
    for f in features:
        n = len(f["scenarios"])
        total_scen += n
        rows.append((f["id"], f["title"].split(" - ", 1)[-1] if " - " in f["title"] else f["title"], str(n), "Ready"))

    h = PAD + 70 + 40 + len(rows) * 42 + 70 + PAD
    img = Image.new("RGB", (W, h), WHITE)
    draw = ImageDraw.Draw(img)
    y = PAD
    draw.text((PAD, y), "Sprint 2 · Acceptance Tests", font=F_TITLE, fill=DARK)
    y += th(draw, "title", F_TITLE) + 8
    draw.text(
        (PAD, y),
        "Testing Suite Evidence · Gherkin (Given / When / Then) · 8 features",
        font=F_SUB,
        fill=GRAY,
    )
    y += 28

    table_top = y
    table_bottom = y + 40 + len(rows) * 42
    round_rect(draw, (PAD, table_top, W - PAD, table_bottom), WHITE, BORDER, 8)
    draw.rectangle((PAD + 1, table_top + 1, W - PAD - 1, table_top + 40), fill=HEAD_BG)
    for label, hx in [("ID", PAD + 12), ("HISTORIA / TS", PAD + 110), ("ESCENARIOS", PAD + 620), ("ESTADO", PAD + 780)]:
        draw.text((hx, table_top + 12), label, font=F_TH, fill=GRAY)
    draw.line((PAD, table_top + 40, W - PAD, table_top + 40), fill=BORDER)

    ry = table_top + 40
    for i, (fid, name, n, st) in enumerate(rows):
        if i:
            draw.line((PAD + 1, ry, W - PAD - 1, ry), fill=LINE)
        draw.text((PAD + 12, ry + 12), fid, font=F_CELL_B, fill=DARK)
        draw.text((PAD + 110, ry + 12), name[:48], font=F_CELL, fill=ROW)
        draw.text((PAD + 620, ry + 12), n, font=F_CELL, fill=DARK)
        draw.text((PAD + 780, ry + 12), st, font=F_OK, fill=GREEN)
        ry += 42

    y = table_bottom + 16
    banner = f"{len(features)} features · {total_scen} escenarios · Acceptance Tests listos"
    round_rect(draw, (PAD, y, W - PAD, y + 44), GREEN_BG, GREEN_BD, 8)
    draw.text((PAD + 16, y + 12), banner, font=F_BADGE, fill=GREEN)
    y += 56
    draw.text((PAD, y), "FreshSense · 6.2.2.5 Testing Suite Evidence · Sprint Review", font=F_FOOT, fill=(152, 162, 179))
    img.save(path, "PNG", optimize=True)
    print("wrote", path.name, img.size)


def render_feature(feat: dict, path: Path):
    # measure
    tmp = Image.new("RGB", (W, 20), WHITE)
    d = ImageDraw.Draw(tmp)
    y = PAD
    y += th(d, "repo", F_REPO) + 6
    y += th(d, "title", F_TITLE) + 10
    for line in wrap(d, feat["description"], F_DESC, W - 2 * PAD):
        y += th(d, line, F_DESC) + 4
    y += 18
    for sc in feat["scenarios"]:
        y += 28
        for step in sc["steps"]:
            for _ in wrap(d, step, F_STEP, W - 2 * PAD - 24):
                y += 20
        y += 12
    y += 30 + PAD

    img = Image.new("RGB", (W, y), WHITE)
    draw = ImageDraw.Draw(img)
    cy = PAD
    draw.text((PAD, cy), "SPRINT 2 · ACCEPTANCE TEST", font=F_REPO, fill=GRAY)
    cy += th(draw, "r", F_REPO) + 6
    draw.text((PAD, cy), feat["title"], font=F_TITLE, fill=DARK)

    badge = f"{len(feat['scenarios'])} escenarios"
    bw = tw(draw, badge, F_BADGE) + 28
    round_rect(draw, (W - PAD - bw, PAD + 6, W - PAD, PAD + 36), GREEN_BG, GREEN_BD, 16)
    draw.text((W - PAD - bw + 14, PAD + 12), badge, font=F_BADGE, fill=GREEN)

    cy += th(draw, "t", F_TITLE) + 10
    chip = feat["file"]
    cw = tw(draw, chip, F_CHIP) + 20
    round_rect(draw, (PAD, cy, PAD + cw, cy + 26), CHIP_BG, CHIP_BD, 6)
    draw.text((PAD + 10, cy + 4), chip, font=F_CHIP, fill=ROW)
    cy += 34

    for line in wrap(draw, feat["description"], F_DESC, W - 2 * PAD):
        draw.text((PAD, cy), line, font=F_DESC, fill=GRAY)
        cy += th(draw, line, F_DESC) + 4
    cy += 14

    for sc in feat["scenarios"]:
        round_rect(draw, (PAD, cy, W - PAD, cy + 26), HEAD_BG, BORDER, 6)
        draw.text((PAD + 12, cy + 5), f"Scenario: {sc['name']}", font=F_SCEN, fill=DARK)
        cy += 34
        for step in sc["steps"]:
            m = re.match(r"^(Given|When|Then|And|But)\s+(.*)$", step)
            if m:
                kw, rest = m.group(1), m.group(2)
            else:
                kw, rest = "", step
            x = PAD + 16
            if kw:
                draw.text((x, cy), kw, font=F_STEP_KW, fill=KW)
                x += tw(draw, kw + " ", F_STEP_KW)
            for i, line in enumerate(wrap(draw, rest, F_STEP, W - x - PAD)):
                draw.text((x if i == 0 else PAD + 16 + tw(draw, "Given ", F_STEP_KW), cy), line, font=F_STEP, fill=ROW)
                cy += 20
        cy += 12

    draw.text((PAD, cy + 4), "FreshSense · 6.2.2.5 Testing Suite Evidence · Sprint Review", font=F_FOOT, fill=(152, 162, 179))
    img.save(path, "PNG", optimize=True)
    print("wrote", path.name, img.size)


def main():
    features = [parse_feature(p) for p in sorted(OUT.glob("*.feature"))]
    render_summary(features, OUT / "sprint2-acceptance-resumen.png")
    for feat in features:
        slug = feat["file"].replace(".feature", "").lower()
        render_feature(feat, OUT / f"sprint2-{slug}.png")


if __name__ == "__main__":
    main()
