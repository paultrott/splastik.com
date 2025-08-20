from PIL import Image, ImageDraw, ImageFont

# Target sizes: (pixels, output filename, font size heuristic)
SPECS = [
    (16,  "favicon-16.png", 10),
    (32,  "favicon-32.png", 20),
    (180, "apple-touch-icon.png", 120),
]

TEXT = "SP"
BG = (0, 0, 0, 255)
FG = (255, 255, 255, 255)

def load_font(px):
    # Try a common bold font; fall back to default if not found.
    preferred = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/SFNSRounded.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/Windows/Fonts/arialbd.ttf",
    ]
    for path in preferred:
        try:
            return ImageFont.truetype(path, px)
        except Exception:
            continue
    return ImageFont.load_default()

for size, filename, font_px in SPECS:
    img = Image.new("RGBA", (size, size), BG)
    draw = ImageDraw.Draw(img)
    font = load_font(font_px)

    # Measure text
    bbox = draw.textbbox((0, 0), TEXT, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    # Center placement
    x = (size - w) / 2
    y = (size - h) / 2 - 1  # tiny vertical optical tweak
    draw.text((x, y), TEXT, font=font, fill=FG)

    # For very small sizes, optional pixel cleanup (skip for simplicity)
    img.save(filename)
    print(f"Wrote {filename}")