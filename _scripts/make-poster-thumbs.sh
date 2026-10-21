#!/bin/sh
# assets/posters/*.pdf 의 첫 페이지로 미리보기 이미지(.jpg)를 만듭니다. (macOS sips 사용)
# 사용법: sh _scripts/make-poster-thumbs.sh
cd "$(dirname "$0")/../assets/posters" || exit 1
for pdf in *.pdf; do
  [ -e "$pdf" ] || continue
  jpg="${pdf%.pdf}.jpg"
  sips -s format jpeg -s formatOptions 80 -Z 480 "$pdf" --out "$jpg" >/dev/null && echo "✓ $jpg"
done
