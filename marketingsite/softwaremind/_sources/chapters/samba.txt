===========================
Samba File and Print Server
===========================


.. sidebar:: historical note

   This is an interesting sliver of history - but I am amazed there are
   still people doing this.  I thought DropBox ruled the world!


http://us1.samba.org/samba/docs/using_samba/toc.html
http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/network-samba.html
http://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/






Example::

    [global]
        workgroup = PIRC
        server string = NAGIOS SMB Server
        security = share
        log file = /var/log/samba/log.%m
        max log size = 50
        dns proxy = no
        guest account = guest
        unix extensions = off

    [install]
        comment  = Unattended
        writable = yes
        locking  = no
        path     = /usr/local/PIRC/w32install/install
        guest ok = yes


Troubleshooting
---------------
1. The above file has

          guest account = guest

But that account (guest) did not exist on my Box so I got

 tail /var/log/samba/log.smbd

[2008/01/13 22:56:38, 0] smbd/server.c:main(1059)
  ERROR: failed to setup guest info.

Interestingly I want to view the source itself  so
/usr/ports/distfiles holds all the tarballs, expand and have a look


SWAT
----
uncomment inetd.conf line to run swat

#!/bin/sh

#smbclient  -U paul.brian -L \\ADC

### mounting samba
mount_smbfs //nobody@samba/FILES /mnt/samba/FILES
mount_smbfs //nobody@samba/PDOXDATA0 /mnt/samba/PDOXDATA0
mount_smbfs //nobody@samba/PDOXDATA1 /mnt/samba/PDOXDATA1
mount_smbfs //nobody@samba/IT /mnt/samba/IT

mount_smbfs //paul.brian@ADC/Managers /mnt/ADC/Managers
