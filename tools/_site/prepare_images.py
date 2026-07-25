from pathlib import Path
from PIL import Image

SOURCE = Path("../originals")
DISPLAY = Path("../assets/images/paintings")
THUMBS = DISPLAY / "thumbs"

DISPLAY.mkdir(parents=True, exist_ok=True)
THUMBS.mkdir(parents=True, exist_ok=True)

DISPLAY_SIZE = 2000
THUMB_SIZE = 500

for image_file in SOURCE.glob("*"):

    if image_file.suffix.lower() not in [".jpg", ".jpeg", ".png", ".tif", ".tiff"]:
        continue

    name = image_file.stem.lower().replace(" ", "-")

    img = Image.open(image_file)

    if img.mode != "RGB":
        img = img.convert("RGB")

    #
    # Display image
    #

    display = img.copy()

    display.thumbnail((DISPLAY_SIZE, DISPLAY_SIZE))

    display.save(
        DISPLAY / f"{name}.jpg",
        quality=92,
        optimize=True
    )

    #
    # Square thumbnail
    #

    thumb = img.copy()

    w, h = thumb.size

    side = min(w, h)

    left = (w - side) // 2
    top = (h - side) // 2

    thumb = thumb.crop((left, top, left + side, top + side))

    thumb = thumb.resize((THUMB_SIZE, THUMB_SIZE))

    thumb.save(
        THUMBS / f"{name}-thumb.jpg",
        quality=90,
        optimize=True
    )

print("Finished.")