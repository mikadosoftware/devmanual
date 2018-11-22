#. /home/pbrian/venvs/devmanual/bin/activate
#prepare by putting it all in one big file
python preprocess.py docs/index.pre
cd docs/
make clean
make html
#make latexpdf
#sphinx-build -b rinoh . _build/pdf

#I expect to run this in a docker instacne on my laptop
#so i need to run it on here like a server

#build it as a book marketring site
cd ../
python postprocess.py
echo `pwd`

#firefox http://172.17.0.2:8000/_build/latex/TheDevManual.pdf
firefox http://172.17.0.2:8000/marketingsite/index.html
python -m http.server 8000
