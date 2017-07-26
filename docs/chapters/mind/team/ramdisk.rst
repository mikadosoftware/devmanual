=================
FreeBSD - RAMDISK
=================



::

    #!/bin/sh

    case "$1" in
    start)
            /sbin/mdmfs -s 256M md10 /mnt/ramdisk
            echo "256MB ramdisk created on /dev/md10 and mounted on /mnt/ramdisk"
            exit 0
            ;;
    stop)
            /sbin/umount /mnt/ramdisk
            /sbin/mdconfig -d -u 10
            echo "ramdisk unmounted from /mnt/ramdisk and deleted from /dev/md10"
            ;;
    *)
            echo "Usage: `basename $0` {start|stop}" >&2
            exit 64
            ;;
    esac


biblio:

http://www.freebsdwiki.net/index.php/RAMdisks,_creating_under_FreeBSD_5.x
