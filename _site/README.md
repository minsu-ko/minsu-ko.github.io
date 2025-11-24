# minsu-ko.github.io

new commit. - -


How to open local

docker run --rm -it \
  -p 4000:4000 \
  -v "$PWD":/srv/jekyll \
  -v "$PWD"/vendor/bundle:/usr/local/bundle \
  jekyll/jekyll \
  jekyll serve --watch --drafts --livereload