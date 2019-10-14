===============================
Python Packaging Best Practises
===============================


Rule number 1: Run! Run for the hills !

Some notes

How to pacakge
--------------
(Notes as autodocs)



How to send packages to PyPi
----------------------------

* sudo pip install twine
 Install to test location

 python -m twine upload --repository-url=https://test.pypi.org/legacy/ dist/<nameofwheel>

 (username and password - ignore kde wallet request?)


real repositry is upload.pypi.org

WOrks !!!
