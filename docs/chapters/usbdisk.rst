=================
Adding a new disk
=================

=================

Adding a new disk is relatively simple to a BSD system, However the most common
way of adding a disk is through the USB subsystem.  So I am trying to cover the
two approaches here.  Superficially the USB disk and the 'normal' disk just need
to be 'recognised' - that is have a device file put in /dev/ with an appropraite
driver.

Lets get to the point where a disk is recognised by dmesg.

Getting to dmesg
----------------

We can add a disk inside the PC as 'normal' - that is unscrew the covers and
connect up a PATA (IDE) or SATA disk.  In pretty much every case here, you will
see that disk show up in dmesg

::

  ad4: 57231MB <Hitachi HTS541660J9SA00 SBBOC70P> at ata2-master SATA150

So as expected I have a 60GB HDD on sata

However if I then plug in my USB enclosed external hard drive I see on Dmesg

::

  umass0: <Maxtor OneTouch, class 0/0, rev 2.00/1.22, addr 2> on uhub2
  da0 at umass-sim0 bus 0 target 0 lun 0
  da0: <Maxtor OneTouch 0122> Fixed Direct Access SCSI-4 device
  da0: 40.000MB/s transfers
  da0: 114473MB (234441648 512 byte sectors: 255H 63S/T 14593C)

now this shows two things.  FIrstly the umass driver.  this is the USB-mass
storage driver and it has found something on the USB Bus Then the driver is able
to recognise the actual model, and so I have now got a device driver lined up
and a 'file' sitting in /dev/da0

I can now use this as normal and proceed to the next step.

If umass discovers the disk but there is no device listed, frankly its
tough. The drivers are not there and unless its vital, go buy another supported
disk.  See umass(8) for supported disks.  There are loads, and given you can buy
a 1TB for less than a hundred quid, its not worth worrying.

However if you really need that disk, try a firewire enclosure.  This has less
driver issues than USB.


Preparing and mounting the disk
-------------------------------

0. Zero the disk
1. fdisk - Being nice to the PC BIOS
2. bsdlabel - prepping for BSD
3. newfs - writing the filesystems
4. mount

bibliography: http://www.freebsd.org/doc/en/books/handbook/disks-adding.html

zero the disk
-------------

This is straightforward dd from /dev/zero to your disk.  I find that as a rough
rule of thumb you can zero an entire 40GB disk in 20 minutes. [#]_

::

   #this overwrites the first 1024 bytes, effectviely killing the boot partition.
   #leave off count to do the whole disk, make count 1000 to do first 1MB etc etc

   dd if=/dev/zero of=/dev/da0 bs=1024 count=1


fdisk
-----

You do not have to do this, except for the boot disk iSo for a USB disk that is
solely for backup, fine, used 'dedicated' mode

PC BIOS usually 'controls' a HDD.  THat is it mediates the access from the OS to
the BIOS to the HDD.  THats how the PC was designed, and frankly BSD ignores it
and can control the disk directly.  However if BSD is controlling the disk
directly, it cannot be used by some other OS that expects the BIOS to do the
work.  So BSD has 'dedicated' mode that means you use that disk only fafter BSD
has booted - DOS wont like it, and BIOS wont boot from it.

a dedicated disk will look like /dev/da0e

We shall ignore that for now - the handbook recommends playing nice - using
'slices' A slice is a BSD term for one of the four BIOS partitions. so a BSD
disk with 4 partitions will have device files called

::

 /dev/ad4s1 /dev/ad4s2 /dev/ad4s3  /dev/ad4s4


Look at what is there

::


    # fdisk -s /dev/ad4
    /dev/ad4: 116280 cyl 16 hd 63 sec
    Part        Start        Size Type Flags
       1:          63   117210177 0xa5 0x80


    # fdisk /dev/ad4
    ******* Working on device /dev/ad4 *******
    parameters extracted from in-core disklabel are:
    cylinders=116280 heads=16 sectors/track=63 (1008 blks/cyl)

    Figures below won't work with BIOS for partitions not in cyl 1
    parameters to be used for BIOS calculations are:
    cylinders=116280 heads=16 sectors/track=63 (1008 blks/cyl)

    Media sector size is 512
    Warning: BIOS sector numbering starts with sector 1
    Information from DOS bootblock is:
    The data for partition 1 is:
    sysid 165 (0xa5),(FreeBSD/NetBSD/386BSD)
        start 63, size 117210177 (57231 Meg), flag 80 (active)
            beg: cyl 0/ head 1/ sector 1;
            end: cyl 1023/ head 254/ sector 63
    The data for partition 2 is:
    <UNUSED>
    The data for partition 3 is:
    <UNUSED>
    The data for partition 4 is:
    <UNUSED>

this tells me that there are 4 slices or partitions, just as the BIOS expects,
but that only one is initialised in a form readable to BIOS (ie the first
partition, which the BIOS needs to read to boot the disk).  The rest is handled
by BSD itself, using infomration found in bsdlabel


So finally how to initialise my external USB hard disk to have slices the nice
way

::

  fdisk -BI /dev/da0
  #this will
  # -I Initialize sector 0 slice table for one FreeBSD slice covering the entire disk.
  # -B Reinitialize the boot code contained in sector 0 of the disk

  GEOM not found is considered a benign warning by the man file.


[#]_

You will know have one slice on the disk, /dev/da0s1 This is generally what
happens when you use sysinstall and just choose 'use whole disk'


bsdlabel
--------

Here is where we create the traditional BSD partitions (not restrictive 4 BIOS
paritions which are called slices now).  The bsdlabel stores partition size and
location info, as well as other stuff.  it is read by BSD and used to control
the HDD, bypassing the BIOS.

How do BSD partitions work? Basically there are eight partitions (a-h).  (see
http://www.freebsd.org/doc/en/books/handbook/install-steps.html)


The a partition is solely for system disks (ie the disk you boot from). It is
only used for the root (/) partition.  The b partition is used for swap space.
Any number of disks can have swap space, and the rule of thumb is to have twice
RAM as swap.  The c partition is a sort of whole disk placeholder

the e partition is usually the point to put /var in system disks and everything
for other disks the f partition is usually the everything point (/usr) for
system disks

-B will turn a slice into a bootable slice - by copying the boot code from
 /boot/boot into the bootsector of the slice being worked on. It useful for
 system disks but this is not a system disk


::

  #bsdlabel -w /dev/da0s1

OK this has built a standard label onto that slice. But it does not have our BSD
partitions in it. we want swap, we want /usr etc.  We get this by using

::

  bsdlabel -e /dev/da0s1

this will use vi (EDITOR) to edit the label.  Now a couple of points.  firstly,
use -n

::

  bsdlabel -e -n /dev/da0s1

This will not write to the label, but do all calculations and output some hints
for you.  Second, the bsdlabel is good for calculating human-sized amounts

so when I freshly create the bsdlabel and use -e I get to see a label like this

::

    # /dev/da0s1:
    8 partitions:
    #        size   offset    fstype   [fsize bsize bps/cpg]
      a: 234436466       16    unused        0     0
      c: 234436482        0    unused        0     0         # "raw" part, don't edit

The whole disk is taken up with the a partition which is OKish but not to
convention.

I simply edit it using vi as follows

::

    # /dev/da0s1:
    8 partitions:
    #        size   offset    fstype   [fsize bsize bps/cpg]
      c: 234436482        0    unused        0     0         # "raw" part, don't edit
      e: *                *    4.2BSD        0     0

I have told it to create a e:  partition of 'the whole remainder of the disk' and it does the hard part for me.

Alternatives include

::

    # /dev/da0s1:
    8 partitions:
    #        size   offset    fstype   [fsize bsize bps/cpg]
      a:       30G      16    4.2BSD        0     0
      b:        6G       *    swap
      c: 251658225       0    unused        0     0         # "raw" part, don't edit
      e:         *       *    4.2BSD        0     0
    (cf http://keramida.wordpress.com/2008/09/14/moving-a-freebsd-installation/)





Building the file system
------------------------

Now in the first example of editing the bsdlabel above, I have only created one
partition so I only need one file system to be written on the partition.  I just
need to run

::

   newfs -L BACKUP /dev/da0s1e

however with the second where it is looking a bit like a system disk

::

   newfs -L ROOT /dev/da0s1a
   #swap needs no filesystem
   newfs -L USR /dev/da0s1e



Mount
-----

::

  # mkdir /mnt/disk1
  # mount /dev/da0s1e /mnt/disk1



Summary
-------

::

  # dd if=/dev/zero of=/dev/da1 bs=1k count=1
  # fdisk -BI da1 #Initialize your new disk
  # bsdlabel -B -w da1s1 auto #Label it.
  # bsdlabel -e da1s1 # Edit the bsdlabel just created and add any partitions.
  # mkdir -p /1
  # newfs /dev/da1s1e # Repeat this for every partition you created.
  # mount /dev/da1s1e /1 # Mount the partition(s)
  # vi /etc/fstab # Add the appropriate entry/entries to your /etc/fstab.




Actual results
--------------


::

    [root@paullaptop ~]# dd if=/dev/zero of=/dev/da0 bs=1024 count=10
    10+0 records in
    10+0 records out
    10240 bytes transferred in 0.208999 secs (48995 bytes/sec)

    [root@paullaptop ~]# fdisk -BI /dev/da0
    ******* Working on device /dev/da0 *******
    fdisk: invalid fdisk partition table found
    fdisk: Geom not found: "da0"



Just format a USB Disk for use between BSD and Windows
------------------------------------------------------


* http://lists.freebsd.org/pipermail/freebsd-questions/2010-May/215819.html
* http://en.wikipedia.org/wiki/BSD_disklabel

::

   In BSD-derived computer operating systems (including NetBSD,
   OpenBSD, FreeBSD and DragonFly BSD) and in related operating
   systems such as SunOS, a disklabel is a record stored on a data
   storage device such as a hard disk that contains information about
   the location of the partitions on the disk. Disklabels were
   introduced in the 4.3BSD-Tahoe release.[1] Disklabels are usually
   edited using the disklabel utility. In later versions of FreeBSD
   this was renamed as bsdlabel.




.. [#] Will this be unreadable?  Well yes, with caveats.  Overwriting
       the disk with zeros once makes it unrecoverable except by
       scanning the surface of the disk with specialised equipment
       which can detect the tiny magnetic differences between a zero
       that was overwritten with zero and a one that was overwritten
       with zero.  Unless you are a suspected terrorist or have stolen
       a billion dollars, overwriting with zeros once is fine.  If you
       are a terrorist, firstly do not put your secret plans on a
       computer in the first place, secondly, use a masonary drill to
       destroy the platters, a few holes sufficient heat and presto,
       no recovery.  Frankly this is all a bit academic.  If you know
       the cops will get you in sufficient time for you to zero a disk
       or otherwise destroy it, the cops need to get better funding.

.. [#] In order for the BIOS to boot the kernel, certain conventions
     must be adhered to.  Sector 0 of the disk must contain boot code,
     a slice table, and a magic number.  BIOS slices can be used to
     break the disk up into several pieces.  The BIOS brings in sector
     0 and verifies the magic num- ber.  The sector 0 boot code then
     searches the slice table to determine which slice is marked
     ``active''.  This boot code then brings in the bootstrap from the
     active slice and, if marked bootable, runs it.  Under DOS, you
     can have one or more slices with one active.  The DOS fdisk
     utility can be used to divide space on the disk into slices and
     set one active.
