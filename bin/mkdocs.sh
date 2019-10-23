#. /home/pbrian/venvs/devmanual/bin/activate

## This is the *production* process for the book
## 
## ref: https://digitalsuperpowers.com/blog/2019-02-16-publishing-ebook.html

# Get back out of bin
cd ..
REPODIR=`pwd`
echo "Run PreProcess"
#prepare by putting it all in one big file
python $REPODIR/bin/preprocess.py docs/index.pre

echo "Make Sphinx Docs"
cd $REPODIR/docs/
make clean
make html
make latex
cd $REPODIR/docs/_build/latex
pdflatex --interaction=nonstopmode TheDevManual.tex

#I expect to run this in a docker instacne on my laptop
#so i need to run it on here like a server

echo "Run post Process (build marketing site)"
#build it as a book marketring site
cd $REPODIR/
python $REPODIR/bin/postprocess.py


