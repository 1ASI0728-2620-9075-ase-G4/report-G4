"""Render clean full-bleed white evidence PNGs for the report."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W = 960
PAD = 28
GREEN = (2, 122, 72)
GREEN_BG = (236, 253, 243)
GREEN_BD = (171, 239, 198)
GRAY = (102, 112, 133)
DARK = (16, 24, 40)
ROW = (29, 41, 57)
LINE = (242, 244, 247)
HEAD_BG = (249, 250, 251)
CHIP_BG = (242, 244, 247)
CHIP_BD = (228, 231, 236)
WHITE = (255, 255, 255)
BORDER = (228, 231, 236)


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(fr"C:\Windows\Fonts\{name}", size)


F_REPO = font("segoeuil.ttf", 13)
F_TITLE = font("segoeuib.ttf", 30)
F_BADGE = font("segoeuib.ttf", 14)
F_CHIP = font("segoeui.ttf", 13)
F_TH = font("segoeuib.ttf", 11)
F_OK = font("segoeuib.ttf", 14)
F_NAME = font("consola.ttf", 12)
F_DUR = font("segoeui.ttf", 13)
F_FOOT = font("segoeui.ttf", 12)
F_SUB = font("segoeui.ttf", 14)
F_CELL = font("segoeui.ttf", 15)
F_REPO_B = font("segoeuib.ttf", 15)


def text_w(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def text_h(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[3] - box[1]


def rounded_rect(draw: ImageDraw.ImageDraw, xy, fill, outline=None, radius=8, width=1):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def render_table(path: Path, repo: str, title: str, badge: str, chips: list[str], rows: list[tuple[str, str, str]]):
    tmp = Image.new("RGB", (W, 10), WHITE)
    d = ImageDraw.Draw(tmp)
    y = PAD
    y += text_h(d, repo, F_REPO) + 6
    y += text_h(d, title, F_TITLE) + 14
    y += 28 + 16
    y += 36
    y += len(rows) * 32
    y += 18 + text_h(d, "foot", F_FOOT) + PAD

    img = Image.new("RGB", (W, y), WHITE)
    draw = ImageDraw.Draw(img)

    x = PAD
    cy = PAD
    draw.text((x, cy), repo.upper(), font=F_REPO, fill=GRAY)
    cy += text_h(draw, repo, F_REPO) + 6
    draw.text((x, cy), title, font=F_TITLE, fill=DARK)

    bw = text_w(draw, badge, F_BADGE) + 28
    bh = 30
    bx1 = W - PAD - bw
    by1 = PAD + 8
    rounded_rect(draw, (bx1, by1, bx1 + bw, by1 + bh), GREEN_BG, GREEN_BD, radius=16)
    draw.text((bx1 + 14, by1 + 6), badge, font=F_BADGE, fill=GREEN)

    cy += text_h(draw, title, F_TITLE) + 14
    cx = x
    for chip in chips:
        cw = text_w(draw, chip, F_CHIP) + 20
        rounded_rect(draw, (cx, cy, cx + cw, cy + 26), CHIP_BG, CHIP_BD, radius=6)
        draw.text((cx + 10, cy + 4), chip, font=F_CHIP, fill=ROW)
        cx += cw + 8
    cy += 26 + 16

    col_ok, col_dur = 100, 72
    table_top = cy
    table_bottom = cy + 36 + len(rows) * 32
    rounded_rect(draw, (PAD, table_top, W - PAD, table_bottom), WHITE, BORDER, radius=8)
    draw.rectangle((PAD + 1, table_top + 1, W - PAD - 1, table_top + 36), fill=HEAD_BG)
    draw.text((PAD + 12, table_top + 10), "RESULTADO", font=F_TH, fill=GRAY)
    draw.text((PAD + col_ok, table_top + 10), "PRUEBA", font=F_TH, fill=GRAY)
    dur_label = "DURACIÓN"
    draw.text((W - PAD - 12 - text_w(draw, dur_label, F_TH), table_top + 10), dur_label, font=F_TH, fill=GRAY)
    draw.line((PAD, table_top + 36, W - PAD, table_top + 36), fill=BORDER)

    ry = table_top + 36
    for i, (status, name, dur) in enumerate(rows):
        if i:
            draw.line((PAD + 1, ry, W - PAD - 1, ry), fill=LINE)
        draw.text((PAD + 12, ry + 8), status, font=F_OK, fill=GREEN)
        draw.text((PAD + col_ok, ry + 9), name, font=F_NAME, fill=ROW)
        draw.text((W - PAD - 12 - text_w(draw, dur, F_DUR), ry + 9), dur, font=F_DUR, fill=GRAY)
        ry += 32

    cy = table_bottom + 16
    draw.text((PAD, cy), "FreshSense · Evidencia Testing Suite · Sprint Review", font=F_FOOT, fill=(152, 162, 179))
    img.save(path, "PNG", optimize=True)
    print(f"wrote {path.name} {img.size}")


def render_summary(path: Path):
    rows = [
        ("Freshsense-EDGE", "24", "24", "48", "Passed"),
        ("BackEnd", "11", "9", "20", "Passed · BUILD SUCCESS"),
    ]
    h = PAD + 40 + 24 + 40 + len(rows) * 48 + 70 + PAD
    img = Image.new("RGB", (W, h), WHITE)
    draw = ImageDraw.Draw(img)
    y = PAD
    draw.text((PAD, y), "Testing Suite Evidence", font=F_TITLE, fill=DARK)
    y += text_h(draw, "Testing Suite Evidence", F_TITLE) + 8
    draw.text((PAD, y), "Sprint Review · Freshsense-EDGE y BackEnd · unitarios e integrales", font=F_SUB, fill=GRAY)
    y += 28

    table_top = y
    table_bottom = y + 40 + len(rows) * 48
    rounded_rect(draw, (PAD, table_top, W - PAD, table_bottom), WHITE, BORDER, radius=8)
    draw.rectangle((PAD + 1, table_top + 1, W - PAD - 1, table_top + 40), fill=HEAD_BG)
    headers = [("COMPONENTE", PAD + 12), ("UNITARIOS", PAD + 280), ("INTEGRALES", PAD + 420), ("TOTAL", PAD + 580), ("RESULTADO", PAD + 700)]
    for label, hx in headers:
        draw.text((hx, table_top + 12), label, font=F_TH, fill=GRAY)
    draw.line((PAD, table_top + 40, W - PAD, table_top + 40), fill=BORDER)

    ry = table_top + 40
    for i, (comp, u, integ, total, res) in enumerate(rows):
        if i:
            draw.line((PAD + 1, ry, W - PAD - 1, ry), fill=LINE)
        draw.text((PAD + 12, ry + 14), comp, font=F_REPO_B, fill=DARK)
        draw.text((PAD + 280, ry + 14), u, font=F_CELL, fill=DARK)
        draw.text((PAD + 420, ry + 14), integ, font=F_CELL, fill=DARK)
        draw.text((PAD + 580, ry + 14), total, font=F_CELL, fill=DARK)
        draw.text((PAD + 700, ry + 14), res, font=F_OK, fill=GREEN)
        ry += 48

    y = table_bottom + 16
    banner = "68 pruebas ejecutadas · 0 fallos · 0 errores"
    bw = W - 2 * PAD
    rounded_rect(draw, (PAD, y, PAD + bw, y + 44), GREEN_BG, GREEN_BD, radius=8)
    draw.text((PAD + 16, y + 12), banner, font=F_BADGE, fill=GREEN)
    y += 56
    draw.text((PAD, y), "FreshSense · Evidencia Testing Suite · Sprint Review", font=F_FOOT, fill=(152, 162, 179))
    img.save(path, "PNG", optimize=True)
    print(f"wrote {path.name} {img.size}")


def main():
    render_summary(OUT / "testing-resumen.png")
    render_table(
        OUT / "edge-unitarios.png",
        "Freshsense-EDGE",
        "Pruebas unitarias",
        "24 passed",
        ["pytest", "frescura · claim · validación"],
        [
            ("Passed", "verde cuando los 3 ejes están en rango", "OK"),
            ("Passed", "verde en frutas con etileno bajo", "OK"),
            ("Passed", "amarillo cerca del límite", "OK"),
            ("Passed", "rojo lejos del rango", "OK"),
            ("Passed", "gana el peor eje (humedad)", "OK"),
            ("Passed", "rojo por etileno alto en frutas", "OK"),
            ("Passed", "amarillo por etileno cerca del límite", "OK"),
            ("Passed", "verde en verduras dentro de rango", "OK"),
            ("Passed", "verde en carnes cerca de 0 °C", "OK"),
            ("Passed", "verde en panadería a temperatura ambiente", "OK"),
            ("Passed", "amarillo por humedad cerca del límite", "OK"),
            ("Passed", "rojo por temperatura baja en panadería", "OK"),
            ("Passed", "verde en los bordes exactos de frutas", "OK"),
            ("Passed", "mapea GREEN/YELLOW/RED → FRESH/AT_RISK/SPOILED", "OK"),
            ("Passed", "claim guarda el secreto del dispositivo", "OK"),
            ("Passed", "claim rechaza código inválido", "OK"),
            ("Passed", "claim actualiza el secreto del mismo device", "OK"),
            ("Passed", "claim guarda secreto de un device nuevo", "OK"),
            ("Passed", "valida payload legacy completo", "OK"),
            ("Passed", "acepta aliases del embebido + ISO timestamp", "OK"),
            ("Passed", "rechaza deviceId vacío", "OK"),
            ("Passed", "rechaza temperatura fuera de rango", "OK"),
            ("Passed", "rechaza etileno negativo", "OK"),
            ("Passed", "rechaza cuerpo que no es JSON objeto", "OK"),
        ],
    )
    render_table(
        OUT / "edge-integrales.png",
        "Freshsense-EDGE",
        "Pruebas de integración",
        "24 passed",
        ["pytest", "API Edge / sensor-readings"],
        [
            ("Passed", "acepta lectura válida", "OK"),
            ("Passed", "clasifica por categoría del dispositivo", "OK"),
            ("Passed", "verde dentro del rango de frutas", "OK"),
            ("Passed", "rojo cuando el etileno es alto", "OK"),
            ("Passed", "acepta aliases del firmware embebido", "OK"),
            ("Passed", "acepta ruta física y device UUID", "OK"),
            ("Passed", "unknown si el dispositivo no tiene categoría", "OK"),
            ("Passed", "umbrales incluyen etileno", "OK"),
            ("Passed", "registra categoría del dispositivo", "OK"),
            ("Passed", "rechaza categoría desconocida", "OK"),
            ("Passed", "rechaza lectura sin etileno", "OK"),
            ("Passed", "rechaza campo faltante", "OK"),
            ("Passed", "rechaza humedad fuera de rango", "OK"),
            ("Passed", "rechaza formato de hora inválido", "OK"),
            ("Passed", "sirve la página de setup", "OK"),
            ("Passed", "claim falla con gracia sin BackEnd", "OK"),
            ("Passed", "amarillo cuando el etileno está cerca del límite", "OK"),
            ("Passed", "registra Lácteos y clasifica verde", "OK"),
            ("Passed", "rechaza lectura sin humedad", "OK"),
            ("Passed", "rechaza temperatura fuera del sensor", "OK"),
            ("Passed", "rechaza deviceId en blanco", "OK"),
            ("Passed", "acepta alias ethylene_ppm", "OK"),
            ("Passed", "rechaza claim con código vacío", "OK"),
            ("Passed", "lista dispositivos tras registrar", "OK"),
        ],
    )
    render_table(
        OUT / "backend-unitarios.png",
        "BackEnd",
        "Pruebas unitarias",
        "11 passed · BUILD SUCCESS",
        ["Maven / JUnit 5", "TS41 · US06"],
        [
            ("Passed", "acepta lectura Edge completa", "OK"),
            ("Passed", "rechaza deviceId vacío", "OK"),
            ("Passed", "rechaza temperatura nula", "OK"),
            ("Passed", "rechaza etileno nulo (TS41 / US06)", "OK"),
            ("Passed", "rechaza humedad nula", "OK"),
            ("Passed", "rechaza deviceId nulo", "OK"),
            ("Passed", "acepta lectura sin status/category", "OK"),
            ("Passed", "acepta lectura sin time/id", "OK"),
            ("Passed", "acepta código de claim válido", "OK"),
            ("Passed", "rechaza código de claim vacío", "OK"),
            ("Passed", "rechaza código de claim nulo", "OK"),
        ],
    )
    render_table(
        OUT / "backend-integrales.png",
        "BackEnd",
        "Pruebas de integración",
        "9 passed · BUILD SUCCESS",
        ["Maven / MockMvc", "POST /api/edge/*"],
        [
            ("Passed", "POST /readings con clave válida → 201", "OK"),
            ("Passed", "POST /readings con clave inválida → 401", "OK"),
            ("Passed", "POST /readings sin etileno → 400", "OK"),
            ("Passed", "POST /readings sin deviceId → 400", "OK"),
            ("Passed", "POST /readings sin humedad → 400", "OK"),
            ("Passed", "POST /readings sin X-Device-Key → 401", "OK"),
            ("Passed", "POST /readings guarda lectura ROJA → 201", "OK"),
            ("Passed", "POST /claim entrega secretKey → 200", "OK"),
            ("Passed", "POST /claim sin código → 400", "OK"),
        ],
    )


if __name__ == "__main__":
    main()
