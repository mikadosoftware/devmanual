====================================================
Also distributed filesystems - cephfs, HDFS, GLUSTER
====================================================


================
NFS File sharing
================

.. sidebar:: Historical Note

   Wow, this one is a golden oldie too.  Look, Samba, NFS.
   I am fairly sure that samba / windows file sharing is slowly getting
   replaced with cloud based file sharing like `Dropbox
   <http://www.dropbox.com>`_
   It won't completely happen, its generally a security nightmare, but
   a good product might be a dropbox proxy that encrypts in and out traffic
   so no matter what is sent out, it is encrypted on disk "out there"



Summary
=======

First there was NFS - it was written to share files over trusted networks (cos
back then everyone trusted everyone else, and wore flowers in their hair.)  The
program that supports this is nfsd.

Then came SMB/CIFS which did not trust everyone, and was built to work with
WIndows machines.  THe program that supports this is SAMBA.

Then people started to really miss NFS, so they made it work with Kerberos.

This chapter starts with NFS, and then moves onto NFS with Kerberos.  For file
sharing within a windows domain see the chapter on SAMBA.

NFS Plain
---------

We need a server and a client.

Server
~~~~~~

This needs to run nfsd (which handles incoming requests) and mountd (which deals
with actually sending receiving the files). rpcbind is also needed so clients
can see what port the nfsd is on.

/etc/rc.conf ::

  rpcbind_enable="YES"
  nfs_server_enable="YES"
  mountd_flags="-r"

client
~~~~~~
/etc/rc.conf ::

  nfs_client_enable="YES"



Sharing
~~~~~~~
On the server we determine which directories we want to 'share' or 'export'.
These are listed line by line in /etc/exports along with the hosts that can see them

::

/workspace/projects/projects/build_system/trunk/bsdbasebuild/new belmarsh belmarsh2


*maproot*
 The -maproot=root flag allows the root user on the remote system to write data on the exported file system as root. If the -maproot=root flag is not specified, then even if a user has root access on the remote system, he will not be able to modify files on the exported file system.



To connect.
Easiest way is to reboot both machines then

::

  mount server:/path /local/mnt/point


Trouble shooting
----------------
- symlinks.
This gets *everyone*. NFS cannot deal with (in fact for security is designed not to deal with) exporting from the server a path witha symlink in it.  If you find that the mounting on the client is failing with *permission denied*, suspect this first.
To check tail /var/log/messages.  You will almost certainly find a message like

::

  Apr 27 12:39:35 paullaptop mountd[643]: mount request denied from 10.137.1.42 for /usr/home/pbrian/workspace/projects/projects/build_system/trunk/bsdbasebuild/new

now if I look at my /etc/exports

::

  /root/workspace/projects/projects/build_system/trunk/bsdbasebuild/new -maproot=root belmarsh belmarsh2

aha! ::

  lrwxr-xr-x   1 root  wheel    22B Dec 11 11:11 workspace -> /home/pbrian/workspace

(yes, I am evil and am running as root)


so I solve it by altering the /etc/exports to

then I give NFS a kick (do this whenever adjusting /etc/exports)

::

  kill -HUP `cat /var/run/mountd.pid`


bibliography
------------
http://www.freebsd.org/doc/en/books/handbook/network-nfs.html
http://www.freesoftwaremagazine.com/columns/securing_nfs
http://www.the-labs.com/FreeBSD/JailTools/cookbook.html
