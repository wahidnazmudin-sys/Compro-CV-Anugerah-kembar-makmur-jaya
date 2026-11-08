"""Generate favicon + apple-touch-icon.

Mode sementara (tanpa logo): pakai monogram snowflake brand.
Setelah file logo tersedia, jalankan ulang dengan --from-logo agar ikon
diambil langsung dari logo perusahaan.

Contoh:
    python _tools/make_icons.py
    python _tools/make_icons.py --from-logo assets/logo.png
"""

from pathlib import Path
import math
import sys

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
BRAND_BLUE = (30, 138, 233)
BRAND_DEEP = (13, 43, 78)


def rounded_background(size: int, radius_ratio: float = 0.22) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i in range(size):
        t = i / max(size - 1, 1)
        r = int(BRAND_DEEP[0] * (1 - t) + BRAND_BLUE[0] * t)
        g = int(BRAND_DEEP[1] * (1 - t) + BRAND_BLUE[1] * t)
        b = int(BRAND_DEEP[2] * (1 - t) + BRAND_BLUE[2] * t)
        draw.line([(0, i), (size, i)], fill=(r, g, b, 255))
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, size * 4 - 1, size * 4 - 1], radius=int(size * 4 * radius_ratio), fill=255
    )
    mask = mask.resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def draw_snowflake(size: int) -> Image.Image:
    """Snowflake 6 lengan, digambar 4x lalu diperkecil agar halus."""
    scale = 4
    s = size * scale
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = cy = s / 2
    length = s * 0.40
    width = max(int(s * 0.055), 2)
    for k in range(6):
        ang = math.radians(60 * k)
        x2 = cx + length * math.cos(ang)
        y2 = cy + length * math.sin(ang)
        d.line([(cx, cy), (x2, y2)], fill=(255, 255, 255, 255), width=width)
        # cabang kecil
        for t, blen in ((0.55, 0.22), (0.75, 0.17)):
            bx = cx + length * t * math.cos(ang)
            by = cy + length * t * math.sin(ang)
            for da in (math.radians(52), math.radians(-52)):
                ex = bx + length * blen * math.cos(ang + da)
                ey = by + length * blen * math.sin(ang + da)
                d.line([(bx, by), (ex, ey)], fill=(255, 255, 255, 255), width=width)
    return img.resize((size, size), Image.LANCZOS)


def icon_snowflake(size: int) -> Image.Image:
    bg = rounded_background(size)
    flake = draw_snowflake(size)
    bg.alpha_composite(flake)
    return bg


def icon_from_logo(logo_path: Path, size: int, background=None) -> Image.Image:
    """Ikon diambil dari logo apa adanya (logo sudah punya bentuk sendiri)."""
    src = Image.open(logo_path).convert("RGBA")
    bbox = src.getbbox()
    if bbox:
        src = src.crop(bbox)
    canvas = Image.new("RGBA", (size, size), background or (0, 0, 0, 0))
    side = max(1, int(size * 0.94))
    src.thumbnail((side, side), Image.LANCZOS)
    canvas.alpha_composite(src, ((size - src.width) // 2, (size - src.height) // 2))
    if background is not None:
        return canvas.convert("RGB")  # apple-touch-icon harus opaque
    return canvas


def main() -> None:
    logo = None
    if "--from-logo" in sys.argv:
        idx = sys.argv.index("--from-logo")
        try:
            logo = Path(sys.argv[idx + 1])
        except IndexError:
            print("Path logo tidak diberikan.")
            return
        if not logo.is_absolute():
            logo = ROOT / logo
        if not logo.exists():
            print(f"File logo tidak ditemukan: {logo}")
            return

    ASSETS.mkdir(parents=True, exist_ok=True)
    # Nama file berversi: dipakai juga untuk memaksa browser membuang cache
    # favicon lama. Kalau logo diganti lagi, naikkan angka versinya.
    jobs = (
        (32, "favicon-logo-32.png", None),
        (64, "favicon-logo-64.png", None),
        (180, "apple-touch-icon.png", (255, 255, 255, 255)),
    )
    for size, name, bg in jobs:
        icon = icon_from_logo(logo, size, bg) if logo else icon_snowflake(size)
        target = ASSETS / name
        icon.save(target, "PNG", optimize=True)
        print(f"OK  {target.relative_to(ROOT)}  ({size}x{size})")


if __name__ == "__main__":
    main()
