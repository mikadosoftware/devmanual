===========
Workstation
===========

How to setup a Linux workstation
================================

There are several basic principles

1. Automate it.
2. Keep to the old technologies
3. Keep it really simple
   

I am coming to the conclusion that mainatining my own
workstation build scripts is ... a bit pointless, and
yet I still keep trying.

I have left the FreeBSD laptop world, and headed into Linux,
but have not yet moved full scale into Mac.  I know a number of people
I respect who feel that move to mac simplified a lot of their needs

   
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

This Xresources setting will give us a solarized look and feel for the
terminal, similar to installing the emacs theme
https://github.com/solarized/xresources/blob/master/Xresources.dark

How to get inconsolata??
THis is a Xwindows font not a terminal font.
So ... I am going for terminus...

What is best unicode terminal

mlterm plus SCIM will allow chinese, arabic, RTL fonts
https://en.wikipedia.org/wiki/Smart_Common_Input_Method

But its not following the .Xresources settings.
So its more awkward

I am having fun installing inconsolata

apt-get install fonts-incolsolata
works
and I can see a .otf file in

ls /usr/share/fonts/truetype/
But that still not working
Am converting  OTF to TTF

apt-get install fontforge
 

*font:    *-inconsolata-*-*-*-24-*
URxvt.font: *-inconsolata-*-*-*-24-*,\
            -misc-fixed-bold-r-normal--15-140-75-75-c-90-iso10646-1,\
            -misc-fixed-medium-r-normal--15-140-75-75-c-90-iso10646-1, \
            [codeset=JISX0208]xft:Kochi Gothic:antialias=false, \
            xft:Code2000:antialias=false


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


Xterm, xmonad and urxvt
=======================

this is the font option (put in .XDefaults) that can 
http://blog.liangzan.net/blog/2012/01/19/my-solarized-themed-arch-linux-setup/
https://github.com/vicfryzel/xmonad-config
https://wiki.haskell.org/Xmonad/Using_xmonad_in_Lubuntu