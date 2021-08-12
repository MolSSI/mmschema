set -e

if [ -d _build ]; then rm -r _build; fi
if [ -d build ]; then rm -r build; fi

make html
cd _build/html

# remove underscores (for gh-pages)
for d in _* ; do
    nd=${d//_}
    grep -rl "$d" *.html | xargs sed -i "s/${d}/${nd}/g"
    mv $d $nd
done

cd ../..
if [ -d ../docs ]; then rm -r ../docs; fi
cp -r _build/html ../docs
