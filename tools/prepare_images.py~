from pathlib import Path
from PIL import Image, ImageOps
import re
from datetime import date

SOURCE = Path("originals")
OUTPUT = Path("assets/images/paintings")
THUMBS = OUTPUT / "thumbs"
PAINTINGS = Path("_paintings")
PAINTINGS.mkdir(exist_ok=True)

OUTPUT.mkdir(parents=True, exist_ok=True)
THUMBS.mkdir(parents=True, exist_ok=True)

DISPLAY_SIZE = 2000
THUMB_SIZE = 500


def clean_name(name):
    name = name.lower()
    name = name.replace("_", "-")
    name = re.sub(r"[^a-z0-9-]+", "-", name)
    name = re.sub(r"-+", "-", name)
    return name.strip("-")
    
def create_markdown(name, title):

    md_file = PAINTINGS / f"{name}.md"

    if md_file.exists():
        return

    content = f"""---
title: {title}
layout: painting
image: {name}.jpg
date_added: {date.today()}
year:
medium:
dimensions:
---

Write a description of the painting here.
"""

    md_file.write_text(content, encoding="utf-8")

    print(f"Created {md_file}")


for file in SOURCE.iterdir():

    if file.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
        continue

    name = clean_name(file.stem)
    title = file.stem.replace("_", " ")
    create_markdown(name, title)

    display_file = OUTPUT / f"{name}.jpg"
    thumb_file = THUMBS / f"{name}-thumb.jpg"

    img = Image.open(file).convert("RGB")


    # display image

    if not display_file.exists():

        display = img.copy()
        display.thumbnail((DISPLAY_SIZE, DISPLAY_SIZE))
        display.save(
            display_file,
            quality=92,
            optimize=True
        )


    # thumbnail - preserve whole painting

    if not thumb_file.exists():

        thumb = ImageOps.contain(
            img,
            (THUMB_SIZE, THUMB_SIZE)
        )

        canvas = Image.new(
            "RGB",
            (THUMB_SIZE, THUMB_SIZE),
            "white"
        )

        x = (THUMB_SIZE - thumb.width) // 2
        y = (THUMB_SIZE - thumb.height) // 2

        canvas.paste(thumb, (x, y))

        canvas.save(
            thumb_file,
            quality=90,
            optimize=True
        )


print("Images prepared.")