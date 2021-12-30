commit=$(git rev-parse HEAD)
version="[$(git describe --always --tags)](https://github.com/volodymyrss/integral-ibis-isgri-le-response/tree/$commit) $(git show -s --format=%ci)"
echo "version: $version"
< README.md sed 's#@VERSION@#'"$version"'#' > README.md.version
diff README.md.version README.md || true
mv -fv README.md.version README.md
