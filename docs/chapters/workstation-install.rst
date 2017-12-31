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


I have recently built a set of tools called `weaver` which I am using to manage
the automation of. This then links back to the longer winded explanations of how and
why in here. Some weaver commands maybe shown here.

   
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



    python devmanual/mikado-installer.py xfce4 xdm

We hope and pray that our graphucs cards and xfce4 play well together.
If not read docs on fixing X - it is a long and lsow process.
This is the time we think MAC is a good move.

We then configure xfce4 to correctly open up when X is started::

    echo "exec startxfce4" > ~/.xinitrc

Then we simply reboot - XDM will ask for our login and then run .xinitrc
We are good to go.

NB
Many "modern" desktop environments no longer use `.xinitrc` because they do not
activate via startx, instead these 'first time starting X' commands go into `.xsession`


Control Files
-------------
in `/etc/X11` we find a number of files that are run on Xorg startup and then
proceed to update or fix user session stuff.

TBD
  fontpath.d

/etc/sysconfig
https://www.sitepoint.com/understanding-nix-login-scripts/

The original Xterm
------------------
Thomas E. Dickey's xterm was written in the mid-late '80's and shipped with XFree86
It is the venerable version of X. History of X? 


.Xresources
-----------

in our ~/.Xresources file we configure the xterm settings for our needs.

Firstly we get a half decent and free font ::

  apt-get install xfonts-terminus
  xset fp rehash

then use xlsfonts to see what fonts are available::

    xlsfonts
    xlsfonts | cut -b -20 | uniq | less

Then we alter out xterm settings in .Xresources as::

  xterm*font:    *-terminus-*-*-*-24-*

Then we set the database for xterm and update it::

  xrdb -merge ~./Xresources


dnf/yum will install '/usr/share/fonts' and we can list those with
fc-list

Now I have installed google droid as a TTF, but I cannot use it
in the console - I need to convert TTF over to console fonts using FOnt FOrge

For now I will use terminus in console and droid in emacs.
As for the rest of X - I will look into it later.
  
This Xresources setting will give us a solarized look and feel for the
terminal, similar to installing the emacs theme
https://github.com/solarized/xresources/blob/master/Xresources.dark

we can review the excellent http://www.futurile.net/2016/06/15/xterm-256color-themes-molokai-terminal-theme/ for more details

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
xfontsel
--------
We can use xfontsel to help us with the slightly ridiculous XLFD style for font definitions - the long tortuous names like::

              -misc-fixed-bold-r-normal--15-140-75-75-c-90-iso10646-1

These are simple really, each - seperated field tells us things like foundary, fontname, size etc.
https://wiki.archlinux.org/index.php/X_Logical_Font_Description gives good detail.

What we want is to load new fonts, and then see which line will give us the font we want,
without getting too bogged down.

::

   
NB
 If -print is specified on the command line the selected font specifier will be written to standard output when the quit button is activated. Regardless of whether or not -print was specified, the font specifier may be made the PRIMARY (text) selection by activating the select button.

 -*-terminus-*-*-*-*-28-*-*-*-*-*-*-*

What a palaver. I should probably get a three-button mouse.

	      
Colours
=======

We can easily see the currently set terminal colours with a bash script::

  for i in {0..255} ; do
      printf "\x1b[48;5;%sm%3d\e[0m " "$i" "$i"
      if (( ((i+1)) % 15 == 0  )); then
          printf "\n";
      fi
  done

THis gives us a nice view of the colours currently set in the terminal


tip of the hat to `https://askubuntu.com/questions/821157/print-a-256-color-test-pattern-in-the-terminal`
	    
emacs
=====

the new location for .emacs file is ~/emacs.d/init.el::

  (set-default-font "Droid Sans Mono-24")

Thats my complete setup now


NB
We want .xsession and .xinitrc to be used.
So we dont use modern gnome but use gnome-classic -which is a clicky thing to do at the xdm layer 

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


Biblio
------
Detailed Look at Fedora Boot Process
https://docs-old.fedoraproject.org/en-US/Fedora/11/html/Installation_Guide/s1-boot-init-shutdown-process.html
