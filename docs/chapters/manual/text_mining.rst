===========
Text Mining
===========

===========

We shall use the well-regarded python library `spacy`

Installing Spacy
----------------

$ workon <>
$ pip install spacy
$ python -m spacy.en.download all

The data is kept as python package data in <venv>/local/lib/python2.7/site-packages/spacy/data
::

  pbrian@shiny:~/venvs/mikadotext/local/lib/python2.7/site-packages/spacy$ ls -lh data/
  drwxrwxr-x 8 pbrian pbrian 4.0K Jan 13 13:03 en-1.1.0
  drwxrwxr-x 3 pbrian pbrian 4.0K Jan 13 13:46 en_glove_cc_300_1m_vectors-1.0.0


Biblio
------
http://textminingonline.com/getting-started-with-spacy
