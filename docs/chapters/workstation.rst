======================================================
Building a FreeBSD laptop from scratch with Salt-stack
======================================================

Workstation 
-----------

Workstation builds also matter, but my preference now is local docker


So this chapter changed a lot...

I am a big FreeBSD user, both in servers and as a personal workstation.  Yes,
Linux is *easier* as a workstation, but then so is Windows.  And its nice to
have the same environments.

I however often find myself putting off important upgrades because my laptop
is my working life - losing a day here would cost real money.  I need to
automate the maintenance of my laptop.  And Shell scripts don't seem "official"
enough.  (I may occassionally cheat however :)

So as well as `installing servers using salt-stack
<http://pyholodeck.mikadosoftware.com>`_ here is how to build a set of
DevOps quality scripts to keep your workstation rebuildable at a moments notice,
and keep the day-to-day maintenance spruced up and ship shape!

The idea is to install the laptop with FreeBSD 10,
point it at the new packaging system, run the miniuon bootstrap,
download my own set of salt states, and ... presto.

Starting off
============

Firstly I need to wipe and install a FreeBSD minimum image onto a machine.
Luckily this is easy - just download the latest `.img` file from FreeBSD.org,
and copy it over to a USB.

Visit::

  ftp://ftp.freebsd.org/pub/FreeBSD/snapshots/ISO-IMAGES/10.0/

and pull back the latest `*memstick.img` file such as ::

  FreeBSD-10.0-STABLE-amd64-20140421-r264704-memstick.img

Now we `dd` over the image from disk to USB.::

  $ dd if=memstick.img of=/dev/da0 bs=1024 conv=sync

Reboot the laptop with USB key attached (ensuring of course the BIOS is set to
boot from USB *before* HDD).

Now install FreeBSD as usual.  It is a pretty straightforward install, and well
documented in the `FreeBSD Manual <http://www.freebsd.org/doc/handbook/install-start.html>`_.

Download and run bootstrap installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidenote:: Hey - I actually contributed a couple of patches to this (very proud!)

The salt stack bootstrap script essentially downloads salt onto your local
machine (OK, a number of potential issues there), and will do various OS
specific setups (in FreeBSD's case, prepare the `pkg` environment, point at the
right URLs etc.)

Unfortunately fetch is a bit rubbish compared to wget, and barfs on SSL
certificates like the dodgy ones at github.  I should look into it.

  $ setenv SSL_NO_VERIFY_PEER 1
  $ fetch http://bootstrap.saltstack.org

  This seems a very bad idea, as we are opening up to a MITM attack.
  I would prefer either:
  * md5 signing
  * download wget *first*
  https://github.com/saltstack/salt-bootstrap/issues/290

This will migrate me to using the `pkgng` (FreeBSD's own apt-get setup)
convert the laptop to a minion, and then all I need to do is set the
right values in /env/salt and call local highstate

.. todo::

   More about pkgng
   [expand on pkgng]


1. Download the appropriate salt-states
2. apply to /usr/local/etc/salt
3. run  `salt-call --local state.highstate`


This way I have now applied a set of states I want on the laptop to a local
cache location (for these
purposes, just Xorg).  They include config files etc.




Changes
-------

We want to put the states in /usr/local/etc/salt/states
We want to put our own execution modules in /usr/local/etc/salt/states
*and* alter /usr/local/etc/salt/minion to change its `module_dirs []` list
to include that.








How does salt-call work (brief)?
================================

1. Process the base environment top.sls file.  This is by default
   `/srv/salt/top.sls` but can be changed (see file_roots)

2.


What do I actually want on my workstation?
==========================================

An article per pkg, ala NTP plus the init.sls and assoc state files.


* sudo
* wget


* xfce4
  hal
  dbus
  xorg
  randr and multi head


* urxvt / xterm for unicode
  http://www.cl.cam.ac.uk/~mgk25/unicode.html
  https://wiki.archlinux.org/index.php/fonts
  $ setfont Lat2-Terminus16


* aspell
* bash
* bsdstats
* security
  port scanner
  gnupg
  keychain
  ssh

* sysadmin
  jails

* dbases
  sqlite
  postgres


* webkit

* sound

* video



* curl
* wget
* emacs
* git / git gui
* sublime?
* fonts


* printing
* Firewall
* python eco-system
* ZFS (TBD)
* web browsers
*
* ImageMagick
* gimp

* rabbitMQ
* spreadsheets??


Other needs
===========

* RPi Routers and NetFlow / packetburst for my local office network



Business Half
=============

* Reporting and Dotted Co-ordination Framework
