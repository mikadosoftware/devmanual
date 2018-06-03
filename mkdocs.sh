. /home/pbrian/venvs/devmanual/bin/activate
cd docs/
make clean
make html
sphinx-build -b rinoh . _build/pdf

firefox _build/html/index.html &
xpdf _build/pdf/TheDevManual.pdf &
