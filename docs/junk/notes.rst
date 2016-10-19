These are notes on how to bootstrap my workstation build
soon to turn automated::

    wget https://bootstrap.pypa.io/get-pip.py

This downloads get-pip.py, which solves the whole chicken and egg issue by basically being a one script
installer - it has a zip/base64 encoding of the real pip package, and it just unzips it in place.
Its sort of neat and sort of an ugly hack.::

   python get-pip.py

Now what we should do it build a venv first and then download pip... but that means pip is needed.
Damn

So lets install virtualenv::

    pip install virtualenv
    pip install virtualenvwrapper

    
virtualenvwrapper
-----------------

export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh

restart shell (source ~/.bashrc)


we need to create an env:

mkvirtualenv <name>

But we could

mkproject <name> and get a venv and a (softlink?) to a project directory
even better is associate a project with a venv so we jyump there after workon

fabirc
no acceptable c compiler found in $PATH
Need to install gcc



Now we would like to install python3 as well
  

So we need a number of things before we get to fabric
its different levels of bootstrapping

1. plain install
2. python / fabirc
   3. fabric driven installs / the whole clever stuff.

      No fucking yaml!
      
   

   
