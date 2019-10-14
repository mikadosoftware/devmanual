#. /home/pbrian/venvs/devmanual/bin/activate

## This is the *production* process for the book
## 
## ref: https://digitalsuperpowers.com/blog/2019-02-16-publishing-ebook.html

# Get back out of bin
cd ..

echo "Run PreProcess"
#prepare by putting it all in one big file
python bin/preprocess.py docs/index.pre

echo "Make Sphinx Docs"
cd docs/
make clean
make html
make latex

#I expect to run this in a docker instacne on my laptop
#so i need to run it on here like a server

echo "Run post Process (build marketing site)"
#build it as a book marketring site
cd ../
python bin/postprocess.py
echo `pwd`

#firefox http://172.17.0.2:8000/_build/latex/TheDevManual.pdf
firefox http://172.17.0.2:8000/marketingsite/index.html &

cd /tmp
python -m http.server 8000
