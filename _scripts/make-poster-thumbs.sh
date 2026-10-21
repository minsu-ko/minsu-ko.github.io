#!/bin/sh
# assets/posters/*.pdf 의 첫 페이지로 미리보기 이미지(.jpg, 긴 변 520px)를 만듭니다. (macOS sips 사용)
# PDF 원본은 .gitignore 로 커밋되지 않고, jpg 미리보기만 사이트에 올라갑니다.
# 사용법: sh _scripts/make-poster-thumbs.sh
cd "$(dirname "$0")/../assets/posters" || exit 1
for pdf in *.pdf; do
  [ -e "$pdf" ] || continue
  jpg="${pdf%.pdf}.jpg"
  sips -s format jpeg -s formatOptions 75 -Z 520 "$pdf" --out "$jpg" >/dev/null && echo "✓ $jpg"
done
