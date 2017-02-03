:manual
Workstation
===========

Bootstrap Python
----------------

sudo apt-get install python python-dev python-pip
pip install mkvirtualenv



Describe initial seetup and reasons

Next steps

* X
* slim
* emacs
* python
* plotting
* firefox

Base OS
-------

- apt-get install
make

Installing X windows
--------------------

We are going to keep this simple and straight

::

    python devmanual/mikado-installer.py xfce4 xdm

We hope and pray that our graphucs cards and xfce4 play well together.
If not read docs on fixing X - it is a long and lsow process.
This is the time we think MAC is a good move.

We then configure xfce4 to correctly open up when X is started::

    echo "exec startxfce4" > ~/.xinitrc

Then we simply reboot - XDM will ask for our login and then run .xinitrc

We are good to go.


.Xresources
-----------

in our ~/.Xresources file we configure the xterm settings for our needs.

Firstly we get a half decent and free font ::

  apt-get install xfonts-terminus
  xset fp rehash

then use xlsfonts to see what fonts are available

    xlsfonts
    xlsfonts | cut -b -20 | uniq | less

Then we alter out xterm settings in .Xresources as::

  xterm*font:    *-terminus-*-*-*-24-*

Then we set the database for xterm and update it::

  xrdb -merge ~./Xresources





emacs
=====


Web services
============

Mozilla cos its more free than Chrome, Chrome cos its got better developer
 tools for now

Installing Python utilities
---------------------------

Sphinx
~~~~~~

We install into a venv


Prince XML
----------

Download from http://www.princexml.com/download/
Its a free non-commerical,pay for commercial license (500 USD for single user desktop)
We will need to also install

   apt-get install libcurl3
