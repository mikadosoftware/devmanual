Workstation
===========


Describe initial seetup and reasons

Next steps

* X
* slim
* emacs
* python
* plotting
* firefox

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

Web services
============

Mozilla cos its more free than Chrome, Chrome cos its got better developer
 tools for now

