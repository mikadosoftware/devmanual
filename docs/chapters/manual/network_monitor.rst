==================
Network Monitoring
==================

.. sidebar:: historical note

   This area has moved on considerably as well.  netflow is still the heart of
    it and RRTD graphs exist everywhere still but graphite and the new
    PacketBeat are showing a new wave.

Introduction
============

Monitoring what is flowing over your network tubes is more important than ever.
For reasons of capacity planning, as well as security and "getting a feel for
the network" good tools matter.

Net-flow and cousins
====================

http://forums.freebsd.org/showthread.php?t=248


net-mgmt/softflowd
$ softflowd -i rl0 -n 192.168.1.20:8888

$ softflowctl statistics
softflowd[11241]: Accumulated statistics:
Number of active flows: 182
Packets processed: 2529
Fragments: 0
Ignored packets: 5 (5 non-IP, 0 too short)
Flows expired: 0 (0 forced)
Flows exported: 0 in 0 packets (0 failures)
Packets received by libpcap: 2579
Packets dropped by libpcap: 0
Packets dropped by interface: 63


net-mgmt/flow-tools
mkdir /var/log/netflow

echo /usr/local/bin/flow-capture -p /var/run/flow-capture.pid -n 287\
    -N 0 -w /var/log/netflow/ -S 5 0/0/8888



http://onlamp.com/bsd/2005/08/18/Big_Scary_Daemons.html
