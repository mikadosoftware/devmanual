=============================
Managing a PC BSD workstation
=============================

I am a big fan of the clean lines of FreeBSD Unix.  However, I am in a
minority, where the winner (Linux) has massive network effect
advantages.

Migrating my main workstation(s) to Linux is not my preferred solution.

I used to build my workstation from scracth - rebuilding the whole from source (See OSBuilder).  However that started taking more and more precious time.

So I am looking for productivity solutions. 

I am a software professional choosing to use BSD to develop on, and choosing to  do so in a manner that does not lose me days of client-billable time if a driver upgrade fails.

PC-BSD presents a workstation on FreeBSD.  They spend a lot of time and effort making things work.  But we can cut down a lot on the outliers.


* Why is the world changing when the basic stuff still works?


Networking
==========

Ethernet networking just *works*.  So stick with it.
For a desktop machine this is fine.
For a laptop - well I *used* to stick to one dongle and one set of configs - till that changed below me.
Now - Netgear universal WiFi.


Portjails
---------

PC-BSD have prebuilt pbis.  THats fine but on an upgrade they wipe out all your nice ports you built.  And if you dont use ports, you dont get source - fopr example you need to build postgres-client apps (psql) from source so that Python psycopg libraries can be built.

So - the PC_BSD upgrade doesnot wipe *portjails*


1. initialising the portjail

2. updating a working portjail ::

     portjail console
     su (sudo not configured here)
     portsnap fetch extract (or update)

3.




GitHub
======

Setting up ghi 
--------------
sudo /usr/local/bin/gem18 install iconv -- --with-opt-dir=/usr/local/


Xorg and Dual Monitors
======================

I know VGA moniotr works - I used to have iut running pre PC-BSD and I can dual moniotr with anohter laptop
xrandr not finding VGA


[pbrian@hadrian ~]$ sudo lspci | grep -i vga
00:01.0 VGA compatible controller: ATI Technologies Inc Device 9802

sudo update-pciids



==============

http://unix.stackexchange.com/questions/44299/how-to-deal-with-freebsds-move-to-pkgconf
migrating from pkg_config to pkgconf

Basically a main junction is being replaced / renamed.
We want to renameit thoughtout beforr more problems
::

  sudo portmaster -o devel/pkgconf devel/pkg-config
 
