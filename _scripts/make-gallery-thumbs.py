#!/usr/bin/env python3
"""갤러리용 웹 썸네일 생성기.

_data/gallery.yml 에 있는 사진마다 assets/gallery/thumbs/<이름>.jpg 를 만듭니다.
- 긴 변 1200px, JPEG 품질 80 (그리드 카드는 약 400px 폭으로 표시 → 레티나 대응)
- EXIF 회전 정보를 실제 픽셀에 반영 (세로 사진이 눕지 않도록)
- 이미 있는 썸네일은 원본이 더 새로울 때만 다시 만듦

사용법: python3 _scripts/make-gallery-thumbs.py   (Pillow 필요: pip3 install pillow)
"""
import re
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
GALLERY = ROOT / "assets" / "gallery"
THUMBS = GALLERY / "thumbs"
MAX_SIDE = 1200

THUMBS.mkdir(exist_ok=True)
data = (ROOT / "_data" / "gallery.yml").read_text(encoding="utf-8")

for line in data.splitlines():
    m = re.match(r'\s*-\s*image:\s*"?/assets/gallery/([^"]+)"?', line)
    if not m:
        continue
    src = GALLERY / m.group(1)
    dst = THUMBS / (src.stem + ".jpg")
    if not src.exists():
        print(f"✗ 원본 없음: {src.name}")
        continue
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        continue
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im).convert("RGB")
        im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        im.save(dst, "JPEG", quality=80, optimize=True, progressive=True)
    print(f"✓ {dst.relative_to(ROOT)}  ({dst.stat().st_size // 1024} KB)")
