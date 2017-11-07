==============
Virtualisation
==============

.. figure:: ../img/virtualisation.png
   :class: screenshot

   Windows and Ubunutu running inside a FreeBSD Host.  Cool Huh?

There are two major types of virtualisation possible these days `Jails
</SoHoFromScratch/jails.html>`_ about which I have written ad-nauseam and think
make excellant option for a FreeBSD system.  Jails however can only virtualise
the host OS - that is I can have a dozen FreeBSD servers running on one host.
But I cannot put Windows on.

If I want to run Windows, then it is over to "true" virtualisation.  Its only
called true by vendors of this class of software, but frankly the name has stuck
a little.

So, how does one do this, and more importantly, why?

Why virtualise?
---------------

Well, the obvious reasons do count - improved power usage, space usage,
reduction in sheer complexity. Its usually cheaper and easier to buy one big
server and put a dozen servers on it, than to actually buy a dozen servers. [#]_

I use Jails all the time - in fact it is a driving reason and enabler for giving
each developer a complete logical clone of the production system to develop
*on*.  If every developer has a set of machines they can put the complete system
onto, several things happen

- deployments are scripted.  If the developer has to deploy to a server each
  time they want to test, magically deploy scripts are written *and kept
  up-to-date*.

- integration problems become more visible early.  Deploying your local working
  copy to your local server set is fine, but if someone checks in bad code, it
  gets noticed, quick.

But that is fine for Jails.  Why this mucking around with Windows?

Quite simple - for testing.

Want to do some web-based UI testing and verification.  Then `Selenium
</SoHoFromScratch/selenium.html>`_ from ThoughtWorks is your friend.  I can
script my browser to open websites, enter in data, capture results, under Python
control and so able to do all that tedious testing you previously hated.


So here we go...

VirtualBox or KVM?
==================

VirtualBox is a commercial company that launched a virtualisation machine
manager (VMM) and then realised it might improve sales if it open-sourced the
code.  The OSS version is slightly crippled (it cannot pass through USB hard
disks or something mostly irrelevant) but it is a good, solid platform and I
highly recommend it.  In fact, the above screenshot is from VirtualBox.

refs::

  http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/virtualization-host.html
  http://wiki.freebsd.org/VirtualBox


Install
-------

::

  cd emulators/virtualbox; make install clean
  echo vboxdrv_load="YES" >> /boot/loader.conf

The principle behind setup is simple.  Allocate a certain amount of your
harddisk to become a single file.  That single file will pretend to be a real
Hard Disk to the VM, which will also have access to all your peripherals,
network card and a pre-determined slice of RAM.

For once this is simple enough to do with a GUI - and I recommend keeping this
simple.  For me clever virtualisation using VMM is for the birds.  Jails do more
than enough if all you want is servers.


proc filesystem
---------------

VirtualBox makes use of the /proc file system (not same as linprocfs which we
enabled for qemu - qemu was run as linux compatibility.  Virtualbox runs native
on FreeBSD.)


either ::

 mount -t procfs proc /proc

 (proc is a virtual device so it has no leading / - the mountpoint does however)

or put this into /etc/fstab.  Probably best to do this... ::

 proc		/proc		procfs	rw		0	0

so you see::

  pbrian_laptop# cat /etc/fstab
  # Device    Mountpoint FStype	Options	Dump	Pass#
  /dev/ad4s1b none	swap	sw	0	0
  ...
  proc   	    /proc       procfs  rw      0       0

Thats it.  (Well, nearly). To start run ::

  $ VirtualBox

You will get a GUI wizard (!).

It seems straightforward - firstly create the virtual hard disk (VirtualBox uses
a format no other virtualisation software does, so this is the only way), assign
the amount of RAM you want to let the VM use.  Since my only intention with this
form of virtualisation is to emulate simple desktop clients, 192MB is more than
enough all round.  (well, OK, this depends, emulating XP running a many flash
clients *eats* RAM.  God, this can be a painful setup.)

Oh, yes, 6GB of Hard disk space seems to be a good amount too.  Down to 2GB and
both ubunutu and windows might complain.  I had a kernel panic - but I increased
RAM from 64 to 192 (and gave it 2 cpus). worked ok.

Install the VM
--------------

We want the VM to boot up, and then look for a bootable image (ie the VM boots
and is given a install CD).  This can be done in two ways - by allowing the VM
access to our own CD/DVD drive, or by mounting an ISO for it.  THe second is a
lot more convenient - especially for ubuntu.

So download the latest Ubuntu .iso (weirdly I was experimenting with this on the
day of a new Ubunutu release, so my download took forever.)  And then goto the
CD tab in the VMM GUI.  tick the 'Mount CD Drive' and then tick 'Mount from
ISO'.  Simply find the iso image on your HDD, and away we go.

Speeding things up
------------------

There are two innovations in hardware-based virtualisation.  VMX extensions and
nested paging.  The first has been around for a couple of years, and, in
essence, performs in hardware the process-marking function that we see in Jails
(ie marking each process as belonging to a given VM).

The second is most recent, found in the Nehalem-range on Intel CPUs (Nehalem is
surprisingly awkward to pronounce - I have it on good assurance that it is
pronounced Neham-a-llama-la-la-ding-dong).  Without this, a VM must pretend it
holds a paging cache - so any cache misses end up being processed twice, once in
the "real" cache, once in the VM version.

Anyway, a CPU without VMX flags and Neham-a-llama-la-la-ding-dong, can be around
3-5 times slower in virtualisation.  So its worth it.


screensize
----------

Refs ::

  http://forums.opensuse.org/new-user-how-faq-read-only/unreviewed-how-faq/385392-virtualbox-screen-size.html

My god - what a palaver.  The basic screen size of 800x640 pixels is what we get
out of the (Virtual)Box.  But try making the thing show the right size.  You
need the extra drivers produced by VirtualBox.

VirtualBox comes with a set of extra goodies, called GuestAdditions. This is an
iso of drivers and so forth that amoungst other things allow you to set the
screen resolution > 800x600.

Now, the instructions say click Devices, then Download Guest Additions.
Unfortunately the download fails.  The iso is not kept where the VMM thinks it
is

The reason - the iso is normally included in the binary that one downloads, for
FreeBSD its not.

so, to solve this we do the following ...

Open up my Ubunutu guest VM.  In the VM, we install virtualbox-ose-guestaddition
using synaptic package manager.  So I download it from the Internet using the
VM.  But I need it in the host.

Then ::

 $ updatedb
 $ locate virtualbox | grep guest

There is a .deb package of 24MB, scp that to my actual host (yes, from the VM to
the host) and use *deb2targz* to extract it, and eventually pull out the iso.

Now put the iso where devices> tries to look for it
(/usr/local/share/virtualbox/VBoxGuestAdditions.iso)

Now it mounts a CDROM, inside the guest.

You need to run the appropriate install pkg on the cd rom for the guest OS
(Linux/win32/solaris are what I can see)

Now with that in place we need to do some extra work

On the *host* machine set a VirtualBox parameter

::

 $ VBoxManage setextradata global GUI/MaxGuestResolution any

Now restart your Guest OS.  It is unlikely it is correct, and if that is a Unix
box it is because the xorg.conf file is incorrect.  I opened up /etc/xorg.conf
in the guest machine and it had two lines from VirtualBox.

I then added ::

 Section "Screen"
         Identifier "Screen0"
         Device     "Card0"
         Monitor    "Monitor0"
         DefaultDepth 24

         SubSection "Display"
                 Viewport   0 0
                 Depth     24
                 Modes "1280x1024 1028x768"
         EndSubSection
 EndSection

Restarted the Guest OS and suddenly I had a choice of resolutions.

Windows
-------

Curiously windows resized, out of the box, with no fuss.  But that is, I guess,
I had already install GuestAdditions onto the VMM as above.


Loading from CD/DVD Drive
-------------------------
Booting from a downloaded iso is nice.
However I have Windows Disk and wanted to load from CD.

This seems ok, but hald slowed my host machine down to a crawl - so I used a .iso of a windows disk
This .iso approach is a *lot* simpler.

::

  from the wiki
  # atapicam kernel module needs to be loaded
  # HAL has to run at the moment
  # Permissions to access /dev/xpt0, /dev/cdN and /dev/passN

  $ kldload atapicam
  $ echo atapicam_load="YES" >> /boot/loader.conf
  $ echo dbus_enable="YES" >> /etc/rc.conf
  $ echo hald_enable="YES" >> /etc/rc.conf

  http://www.freebsd.org/gnome/docs/halfaq.html
  http://wiki.freebsd.org/VirtualBox



Networking
----------

Getting a NAT based IP address for the VM machine is an out of the box issue -
so one can initiate connections from the VM to anywhere.  However, if you want
to run SeleniumRC, you want to connect *to* the VM (the SeleniumRC runs a server
that python client connects to and says "open browser to www.google.com".)

However, we want to do Ethernet bridging, - the simple way is to bring up the
VMM.  There are 4 virtual Ethernet adaptors - one can be the NAT, one can be a
bridged adaptor to the real host NIC.  So just set the NIC adapator number 2 to
brided adaptor, and you can connect to that IP from any machine on the subnet
the host is on.




KQemu
=====

Qemu is a CPU emulator written by Fabrice Bellard.  It is able to translate
system calls from one OS, written for one CPU to the binary equivalents for
another OS or another CPU.  In short one can run Windows OS on a FreeBSD host.

With KQemu, this has been adapted to run on VMX flagged CPUs (specifically on Linux)


Install
-------
::

  cd emulators/kqemu-kmod; make install clean
  cd emulators/qemu; make install clean

  (setup Linux-compatibility on FreeBSD first too)

Somewhere to put it:
we need a 'virtual disk' - a file that is nothing but empty
space for the img to run. its very own hard disk, as it were.

::

  qemu-img create /usr/local/DATA/ubuntu.disk 4G

  or

::

  dd of=/usr/local/DATA/ubuntu.disk bs=1024 seek=4194304 count=0

Now download the .iso file ::

 fetch http://Whereever/the/hell/ubunutu/is/kept

Install it the normal way ::

 qemu -hda /usr/local/DATA/ubuntu.disk -cdrom \
  /home/pbrian/downloads/ubuntu-9.10-desktop-i386.iso -m 192 -boot d

At this point the file image is just like a HDD that has been installed with Ubuntu
But to start the image normally::

 qemu -hda /usr/local/DATA/ubuntu.disk -m 192



Ripping XP CD
-------------
Its much easier with a .iso file than pass-through

  # dd if=/dev/acd0t01 of=/home/pbrian/downloads/xp.iso bs=2048

Really it was awful to get this far.  Had to read the man page to the
bottom - adding bs=2048 solved a lot.

# dd if=/dev/acd0t01 of=/home/pbrian/downloads/xp.iso
dd: /dev/acd0t01: Invalid argument
0+0 records in
0+0 records out
0 bytes transferred in 0.000084 secs (0 bytes/sec)

plus why the acd0t01 worked when acd0 did not?

Actually it seems to be the bs=2048 - CD's transfer at that rate and dd fails
presumably after the first 512Bytes come and 513th is not buffered and a CRC
fails somewhere.

Anyway,

  dd if=/dev/acd0 of=/home/pbrian/downloads/xp.iso bs=2048

works.  Now I have the ISO I install it the usual way, and presto, Windows on
Virtual Machine.  And with Bridging.

VirtualBox
==========

Installing
----------

First guest
-----------

The first one to create is Unbuntu.  Its simple and free.
Download the latest version (www.ubuntu.com), and keep somewhere safe.
Create a harddisk - there is a simple wizard on VirtualBox, I recommend
512MB RAM and min 8GB disk space, 5 years ago that was a damn good spec.!

Then open File > Virtual Media Manager, which will allow us to make the ISO
visible. Just "add" a CD/DVD image, and it is available to the guest image.  Now
go to Settings for the image. Choose Storage and click on the CD below the IDE
COntroller You should see on RHS "Attributes" of the CD device, and can select
any one of the "mounted" CD drives above to "put into" the virtual CD tray.

Start the image as usual, and select boot menu (probably f12), boot from the CD.
You should see a normal install from ubuntu.  Just install.


Bridged Networking
------------------

Compile Kernel with Netgraph included Basically, bridge networking uses a driver
in the Host OS, to bypass the usual host network stack (ie grab packets before
they have gone through all the usual layers).  Netgraph is one such popular way
of doing this.  Thus the virtual machine can take apacket off the real NIC, read
it and then put its own reply back onto the real NIC at the same layer - it
looks to the Host as if right next door on the Ethernet network is another NIC
reading the packets it reads and putting more on the network.

The Virtual machine on the other hand just sets up its stack as normal, thinking
it has access to a genuine real NIC.

Its a bit like this::

   Host  VM
    \    /
     \  /
      --  Netgraph
      |
      NIC

But not really.



http://www.virtualbox.org/manual/ch06.html







bibliography
------------

::

  - https://help.ubuntu.com/community/Installation/QemuEmulator
  - https://help.ubuntu.com/community/WindowsXPUnderQemuHowTo
  - http://wiki.freebsd.org/qemu
  - http://dryice.name/blog/freebsd/using-freebsd-as-a-network-bridge-and-use-dummynet-to-shape-the-traffic/
  - http://www.freebsd.org/doc/en/books/handbook/network-bridging.html



.. [#] Well, attitudes to this might be changing.  ARM-based blade servers can
   actually deliver more CPU cycles per Watt, actually being more green, but
   other issues start to dominate, ranging from deciding if your work is IO
   bound or CPU bound, or handling the logistics required.
