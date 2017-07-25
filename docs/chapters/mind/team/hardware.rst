========
Hardware
========

--------


.. sidebar::  Historical Note

   At first I thought this was going to be running your own servers in
   your own (air-conditioned) rooms.  I mean how 20th Century
   But its local mini servers, RPis and the like.  Very 21st.


.. todo:: links on aircon

What should I buy as a server?
------------------------------
Depends

http://www.soekris.com/
- small form, firewalls routers etc. Freebsd compatible

beagleboard
- low power, single board computer.
- hobbyist, aimed at wearable computers etc.
http://arstechnica.com/open-source/news/2008/08/ti-launches-hackable-beagle-board-for-hobbyist-projects.ars





How to determine what hardware is running?

# sysctl -a | grep -i hw.model
hw.model: Intel(R) Pentium(R) 4 CPU 1.90GHz

# sysctl -a | grep -i memory
Virtual Memory:         (Total: 2161196K, Active 56164K)
Real Memory:            (Total: 19760K Active 10812K)
Shared Virtual Memory:  (Total: 6184K Active: 4760K)
Shared Real Memory:     (Total: 4944K Active: 3668K)
Free Memory Pages:      219288K
hw.cbb.start_memory: 2281701376
p1003_1b.memory_protection: 0
p1003_1b.shared_memory_objects: 1


That is usually enough for one day.

#sysctl -ad
Will show all measures and a description


biblio
------
http://www.freebsd.org/cgi/man.cgi?query=sysctl&sektion=8
http://www.onlamp.com/pub/a/bsd/2005/01/13/FreeBSD_Basics.html


read the source
---------------
ee /usr/src/sys/sys/sysctl.h
