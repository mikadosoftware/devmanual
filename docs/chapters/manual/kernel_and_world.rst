======================
Keeping src up to date
======================

(Re)build a custom Kernel
=========================

1. Make sure we have latest sources
::

 $ cat src-supfile

 *default tag=RELENG_9
 *default host=cvsup3.uk.freebsd.org
 *default prefix=/usr
 *default base=/var/db
 *default release=cvs delete use-rel-suffix compress

 src-all

 $ sudo cvsup src-supfile


RELENG_9 is the STABLE release of FreeBSD.  We shall stick with that.

We want to (we should never not!) build the kernel and the "world"
(userland) from the same src update.

2. Read /usr/src/UPDATING

::

   less /usr/src/UPDATING

   Honestly, it is worth it. The times I did not bother, of course the
   thing I cared about was right there in UPDATING.


3. The run through (from my OSBuilder code) ::

    echo `$dd` start makeworld >> $log
    echo NO_PROFILE=true >> /etc/make.conf
    cd /usr/src
    make -j6 buildworld

    echo `$dd` start kernelbuild >> $log
    cd /usr/src
    make buildkernel KERNCONF=GENERIC
    make installkernel KERNCONF=GENERIC


    echo `$dd` start installworld >> $log
    cd /usr/src
    echo make installworld
    make installworld
    echo now run mergemaster
     #run so that it automatically installs new config files, and puts any diffs into /var/tmp/temproot.xxx
    mergemaster -ia


4. do the above, manually ...









http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/makeworld.html
