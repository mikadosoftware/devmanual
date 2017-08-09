=====================
VirtualBox on FreeBSD
=====================

.. sidebar:: Historical note

   This never made it into the FreeBSD manual because I was a lazy a** and never
   did the re-formating they wanted, but I am still quite proud of it.

.. figure:: ../img/virtualisation.png
   :class: screenshot


   Windows and Ubunutu running inside a FreeBSD Host.

Introduction
============

Virtualisation, running more than one instance of (potentially) more
than one Operating System on a single physical computer, is growing in
popularity and power.

FreeBSD offers two different types of virtualisation, which can be
characterised as single-kernel virtualisation and multiple-kernel
virtualisation.

The first, implemented natively to FreeBSD, is Jails, allowing one
FreeBSD kernel to run many instances of a compatible FreeBSD system.
This approach is simple, and fast and is probably the best choice if
you wish to run several non-GUI instances (ie a mail machine, a web
server and a database).  The author has successfully used this
approach for some years commercially and at home.  However if the
author wished to run Windows or any other operating system on the Jail
Host it would not work - every instance in a Jail uses the same
kernel, so not even different versions of FreeBSD will run on a jail.
In order to run different operating systems one turns to multi-kernel
virtualisation.

This second approach, often called "true" virtualisation, (but usually
only by the vendors of this class of software), is where a Virtual
Machine Manager (VMM) is created that acts as a "interpretation layer"
between the Host OS (in our case FreeBSD) and the Guest OS (for
example a Windows XP instance).

VirtualBox, currently owned by Oracle, is a dual-licensed VMM, with a
commercial version and and OSE (Open Source Edition).  This Open
Source Edition has been ported natively to FreeBSD, and this chapter
shall demonstrate the steps necessary to successful implementation.

It is worth noting that VirtualBox OSE has been intentionally crippled
- it will not pass through RDP requests (you cannot "remote desktop"
into the box) and it will not allow USB devices plugged into the Host
OS to be accessible to the Guest OS.  The commerical version does
allow these functions.


Hardware support
----------------

Until recently virtualised machines were noticeably slow - because the
"interpretation layer" was implemented solely in software.  However as
virtualisation has grown in popularity, the major chip vendors have
worked to develop hardware extensions to improve speed.

There have been two major innovations in hardware-based
virtualisation.  VMX extensions and nested paging.  The first has been
around for a couple of years, and in essence performs the marking of
each process in the host as belonging to the correct Guest OS.

The second is most recent, found in the Nehalem-range on Intel CPUs
and their AMD competitor (?)- without this, a VM must pretend it holds
a paging cache - so any cache misses end up being processed twice,
once in the "real" cache, once in the VM version.

Anecdotally, a CPU without VMX flags and Nehalem, can be around 3-5
times slower in virtualisation, and for a desktop machine this is very
noticeable.

You can detect if your CPU supports the VMX extensions by looking at
dmesg for CPU flags, notable VMX and SSE flags ::

   CPU: Intel(R) Core(TM) i7 CPU       M 620  @ 2.67GHz (2660.02-MHz 686-class CPU) Origin = "GenuineIntel"  Id = 0x20652  Family = 6  Model = 25  Stepping = 2

   Features2=0x298e3ff<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,SMX,EST,TM2,SSSE3,
                                                          ^^^
                         CX16,xTPR,PDCM,SSE4.1,SSE4.2,POPCNT,AESNI>
                                        ^^^^^^^^^^^^^

VMX (almost certainly a requirement for decent Desktop vitualisation)
and SSE4 extensions are shown above.


Prerequisities
--------------

You will need a properly configured X-Windows installation (see
Handbook) and sufficient RAM and Hard Disk space.  For each
desktop-style Guest OS you would expect to need between 256-384MB of
RAM and 6+GB of space, and the more especially of RAM the better the
experience.


Installing VirtualBox
---------------------

NB. These instructions deal with port at or after OSE 3.1.2/

To build VirtualBox use the port found at

::

  cd /usr/ports/emulators/virtualbox; make install clean

You are *strongly* recommended to select the GuestAdditions option
when configuring the port.  This will install the port
virtualbox-ose-additions, an .iso of dirvers and other useful
features.  If you find Windows is unable to exceed 800x600 then Guest
additions is not installed.

This port has been rewritten recently to make VirtualBox install
simpler and easier.  Once you have compiled it, you will need to
adjust /boot/loader.conf as below

::

  echo vboxdrv_load="YES" >> /boot/loader.conf

If you enter "VirtualBox" from a terminal you should see a start up screen like this:

.. figure:: ../img/vbox_intro.png
   :class: screenshot


Preparing for first Guest OS
----------------------------

The principle behind the setup is simple.  Allocate a certain amount
of your harddisk to become a single file.  That single file will
pretend to be a real Hard Disk to the VM, which will also have access
to all your peripherals, network card and a pre-determined slice of
RAM.

The VMM has a simple to use wizard and it is recommended to use this
for the first VM.  You will need to experiment a little on the optimum
Hard disk and RAM allocation for your machine, but 384MB and 8GB has
been found to be a workable minimum for Windows XP and ubuntu
installs.

After the wizard has run you should now have a "virtual machine" ready
to start - 8GB of Harddrive (actually a single file on your real
harddrive) and 384MB of RAM ready to go.  At this point we can boot up
the instance, and you should see a complaint that there is no bootable
image.  We shall now install a OS onto the vitual machine.

.. figure:: ../img/vbox_ready.png
   :class: screenshot


Setting up first Guest OS
-------------------------

We want the VM to boot up, and then look for a bootable image (ie the
VM boots and is given a install CD).  This can be done in two ways -
by allowing the VM access to our own CD/DVD drive, or by mounting an
ISO for it.  THe second is a lot more convenient - especially for
ubuntu.

Obtain ISO
~~~~~~~~~~

You can just download the latest Ubuntu ISO, or you can extract your
*licensed* copy of XP by placing the CD in your CD drive and ::

   # dd if=/dev/acd0 of=/home/pbrian/downloads/xp.iso bs=2048

(NB the block size setting is *very* important - without it you will not
copy anything from a CD drive)

Now visit the CD tab in the VMM GUI.  tick the 'Mount CD Drive' and
then tick 'Mount from ISO'.  Simply find the iso image on your HDD,
and now the Virtual Machine you selected will be able to "see" the CD
as if it was in a normal CD drive.

Install From ISO
~~~~~~~~~~~~~~~~

Start up the VM instance, now you will be able to install the chosen
OS as you would expect, perhaps a little faster than you are used to.

After installing your chosen OS, you will be able to "start" the VM
from the VMM control panel - do so now, and you will see the usual
boot up screens and then a working instance of another Operating
System in your FreeBSD machine.


Networking
----------

VirtualBox offers a NAT-based networking address for your VM out-of-the-box.
This enables you to initiate connections from the VM, but to have connections
initiated *to* the VM, you will need to set up "Ethernet Bridging".


Bridged Networking
~~~~~~~~~~~~~~~~~~

Netgraph is one such popular way of setting up Bridged Networking,
creating a driver that is able to bypass the usual networking stack.

With this the VM can take a packet off the real NIC, read it
and then put its own reply back onto the real NIC at the same layer -
it looks to the Host OS as if right next door on the Ethernet network is
another NIC reading the packets it reads and putting more on the
network.

The Virtual machine on the other hand just sets up its stack as
normal, thinking it has access to a genuine real NIC.

Its a bit like this::

   Host  VM
    \    /
     \  /
      --  Netgraph
      |
      NIC

You will need to re-compile your kernel (see Handbook for instructions).
The following can be used as a kernel configuration file::


    include GENERIC
    ident NGRAPH

    options NETGRAPH


You will then need to switch the current virtual NIC over to Bridged mode
in the VMM GUI and select the appropriate driver - PCNet III works well the
Netgraph driver.



bibliography
------------

::

  - https://help.ubuntu.com/community/Installation/QemuEmulator
  - https://help.ubuntu.com/community/WindowsXPUnderQemuHowTo
  - http://wiki.freebsd.org/qemu
  - http://dryice.name/blog/freebsd/using-freebsd-as-a-network-bridge-and-use-dummynet-to-shape-the-traffic/
  - http://www.freebsd.org/doc/en/books/handbook/network-bridging.html

Bibliography
------------

::

  http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/virtualization-host.html
  http://wiki.freebsd.org/VirtualBox


.. [#]  Well, attitudes to this might be changing.  ARM-based blade servers can actually deliver more CPU cycles per Watt, actually being more green, but other issues start to dominate, ranging from deciding if your work is IO bound or CPU bound, or handling the logistics required.
