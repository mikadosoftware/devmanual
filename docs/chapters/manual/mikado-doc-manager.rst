==================
Mikado-doc-manager
==================

==================

I wish to capture, store, retrieve and tag "documents" used in the course of
the business.  A document is a single file holding useful infomration that is
not itself a file designed to be a database.

Examples include image files, PDF files, Text files (thought less common) and
possibly so-called office productivity files like Word.
An HTML file is less likely a document as to achieve the human readbility it needs to be processed through a browser, and will 99% of time
need other files to make sense (CSS, img, js etc)

The doc-manager will simply - for now - accept input via a email box, and will
store the single, selfcontained file in a disk location using tags associated
with it in the email

the main tag will be the subject line such as mikado.travel.train
and would be a image file of a train receipt ticket

Further tags would be key value pairs on their own lines in the mail body::

    user=pbrian
    value=37.50 GBP
    date=<taken from mail timestamp>

The file(s) in the mail would be hashed (md5/sha1) and that hash used to
index the files and associate the tag information with image

A simple doc-browser would be a "web app" that will allow browsing
of the docs by tags etc

Security review will be needed
