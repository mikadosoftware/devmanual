====
wifi
====

Connecting to a wireless network is *de rigeur* these days.  It's
simple to do - apparently.  For Mac users perhaps, but for us doughty
FreeBSD folks, life is never so simple.  Well, setting up a BSD wifi
connection is not that bad really, it's just that compared to Mac,
Windows or even Ubuntu, well it *is* awkward.

However, once we have, we find we can do other bigger things, like
creating our own access point, running wireless sniffers and more, all
just a little more confidently and knowledgably than those Mac and
Windows users.  And that frankly is the point - a little more pain in
return for confidence, knowledge and clearer path into the 'advanced'
functions.

Summary
=======

With a normal Ethernet over wire, we establish a live *physical*
circuit, send packets over that circuit and route accordingly.

With wifi we need to create a *radio ethernet*, essentially we sling a
virtual wire between our adaptor and the Access Point (AP).

This virtual wire requires three things

- find the wifi adaptor on your machine (laptop)
- ensure the drivers are loaded into kernel and the adaptor is found
- configure adaptor with *ifconfig*
- authenticate with AP and so "associate"

Find the adaptor
================

To be honest this is clearly the most awkward point.  I am using a
work-supplied laptop, and finding the chipset that is built in is a
RRPITA.  To be perfectly honest, I am still unsure I have managed to.


Firstly look at dmesg for anything resembling an Ethernet driver or setup.

::

  $ dmesg | grep -i ethernet
  mskc0: <Marvell Yukon 88E8055 Gigabit Ethernet> mem 0xf5000000-0xf5003fff irq 19 at device 0.0 on pci6
  msk0: Ethernet address: 00:13:77:6f:93:ed

Well, thats my wired Ethernet.
Now, if we want we can look for similar information in *sysctl -a*

::

  mskc0: <Marvell Yukon 88E8055 Gigabit Ethernet> mem 0xf5000000-0xf5003fff irq 19 at device 0.0 on pci6
  msk0: <Marvell Technology Group Ltd. Yukon EC Ultra Id 0xb4 Rev 0x03> on mskc0
  msk0: Ethernet address: 00:13:77:6f:93:ed
  miibus0: <MII bus> on msk0

The thing to note here is that we can get useful stats from sysctl ::

  dev.msk.0.stats.rx.ucast_frames: 0
  dev.msk.0.stats.rx.bcast_frames: 0

OK, well, msk is the driver for my fixed ethernet.  So, err, what
about the wifi?  Well the best I can find is what appears to be a dual
function Broadcom chip.  And all the Google-butt [#]_ says that
Broadcom hates Unix and this chipset stands about as much chance
working with FreeBSD as Michael Jackson does working with the Abused
Children's Dance Therapy group.

::

  ugen1: <Broadcom Corp BCM92045NMD, class 224/1, rev 2.00/3.54, addr 2> on uhub6

So I went and bought a USB stick

::

  rum0: <Belkin Belkin 54g USB Network Adapter, class 0/0, rev 2.00/0.01, addr 2> on uhub7
  rum0: MAC/BBP RT2573 (rev 0x2573a), RF RT2528
  rum0: WARNING: using obsoleted IFF_NEEDSGIANT flag
  rum0: Ethernet address: 00:22:75:fd:d7:8a

I plug it in, ugen (the standard USB driver) finds it, then the rum driver is identified and hooray.

I think I want to be more ... hackerish on this.  But I have things to do, and that USB dongle has now served 3 laptops quite happily.

What drivers work with what chipsets?
=====================================

[EXTEND - how does kernel locate drivers - device to driver mapping - find the right .h file. ]

This is a slight diversion, but it is important - how does the Kernel
know which driver to assign to which device.  Firstly it identifies
the device.

- device on pci bus

- device on usb bus


What drivers for what chipset?
------------------------------

Basically, read the man pages.  Each ethernet driver (I think thet are
rum, ath, zyd, upgt ...)  has a man page and in there it is listed
which chipsets that driver supports

However we can run ::

  pciconf -lv

which will show ::

  none1@pci0:2:0:0:       class=0xff0000 card=0x3577103c chip=0x520910ec rev=0x01 hdr=0x00
    vendor     = 'Realtek Semiconductor Co., Ltd.'
  re0@pci0:6:0:0: class=0x020000 card=0x3577103c chip=0x813610ec rev=0x05 hdr=0x00
    vendor     = 'Realtek Semiconductor Co., Ltd.'
    device     = 'RTL8101E/RTL8102E PCI Express Fast Ethernet controller'
    class      = network
    subclass   = ethernet
  none2@pci0:7:0:0:       class=0x028000 card=0x1636103c chip=0x53901814 rev=0x00 hdr=0x00
    vendor     = 'Ralink corp.'
    class      = network



ifconfig settings
=================

We are assuming that the wifi adaptor has been found and that a driver
is assigned, We now want to connect to the Access Point (AP).

I do recommend reading the ifconfig man pages.  It is really useful.



Scan for AP's
-------------

The first thing to do is see if the adaptor can find the AP ::

  $ ifconfig wlan0 up
  $ ifconfig wlan0 list scan


In a NY hotel room I get ::

  pbrian_laptop# ifconfig rum0 list scan
  SSID            BSSID              CHAN RATE   S:N     INT CAPS
  Buckingham_...  00:c0:02:0f:ac:67    8   54M -89:-95  100 ES

             ^^^

Err, why the ... try -v option to view SSID's that are longer than usual.::

  pbrian_laptop# ifconfig -v rum0 list scan
  SSID                              BSSID              CHAN RATE   S:N     INT CAPS
  Buckingham_Hotel                  00:c0:02:0f:ac:67    8   54M -89:-95  100 ES



unencrypted
-----------

So, this is an unencrypted link, with an SSID and a channel.

/etc/rc.conf ::

  ifconfig_rum0="ssid Buckingham_Hotel channel 8 authmode open DHCP"

(authmode - pretty much everyone uses open. When we are in an infrastructure mode (ie using Access Points that create an infrastucture the clients hang off, we need to say we are in infrastructure mode and then choose an Authentication mode.  It is usually open (with WEP) or wpa).  The alternative to infrastructure mode is ad-hoc - its like the OLPC idea of grid connections. Anyway, use open for now)

And, hey presto I get a connection to the AP in the hotel.  And a web page wanting 12.95 a day for access...
But it worked.

So next, encrypted links

WEP
---

WEP needs a shared key - one that is known to the client and the AP.  Unfortunately most people never change the key and it can take only a few hundren megabytes of traffic to break the encryption, so WEP is not actually secure, just secure enough to prevent your neighbours from seeing what you surf [#]_

::

  ifconfig_rum0="ssid HOME channel 6 authmode open wepmode on weptxkey 1 wepkey 0xyyyyyyyyyyyyyyyyyyyyyyyyy DHCP"

WEP key is a 26 digit hex (0x prefix tells us that.  If you get "String too long" errors, put 0x in to explain this is a hex string).  Now "weptxkey 1" - there are several "slots" to use in the shared key - basically the AP has several shared keys it could use, you need to tell it which slot you are thinking of.  Weptkey is the means.  Ifconfig man suggests that using

::

  wepkey 1:0xyyyyyyyyyyyy

but this does not work for me,  Stick to being explicit.

So, this connects happily to my HOME AP.

Note on DHCP and ifconfig
~~~~~~~~~~~~~~~~~~~~~~~~~

usually I can easily transliterate the following::

  ifconfig_rum0="ssid HOME channel 6 authmode open wepmode on weptxkey 1 wepkey 0xyyyyyyyyyyyyyyyyyyyyyyyyyy inet 192.16.1.10 netmask 255.255.255.0"

  in /etc/rc.conf can also be set up during run time

  ifconfig rum0 ssid HOME channel 6 authmode open wepmode on weptxkey 1 wepkey 0xyyyyyyyyyyyyyyyyyyyyyyyyyy inet 192.16.1.10\
 netmask 255.255.255.0

however, the following raises an error ::

  ifconfig rum0	  ssid HOME channel 6 authmode open wepmode on weptxkey 1 wepkey 0xyyyyyyyyyyyyyyyyyyyyyyyyyy DHCP

while this, in /etc/rc.conf is fine ::

  ifconfig_rum0="ssid HOME channel 6 authmode open wepmode on weptxkey 1 wepkey 0xyyyyyyyyyyyyyyyyyyyyyyyyyy DHCP"


testing /etc settings
~~~~~~~~~~~~~~~~~~~~~

Change settings in /etc/rc.conf, then run

::

  pbrian_laptop# /etc/rc.d/netif start


All Change
==========

The above was very useful.  Back in the day.  However things have moved on and now the approach is to use wpa security.

in /etc/rc.conf::


    wlan_load="YES"

    #making wep /wpa work
    wlan_wep_load="YES"
    wlan_ccmp_load="YES"
    wlan_tkip_load="YES"

    wlans_rum0="wlan0"
    ifconfig_wlan0="WPA DHCP"

this essentially replaces the ifconfig calls earlier in rc.conf.
All of FreeBSD wifi is handled by a super driver - wlan.
We tell this that we want to use the rum0 driver, and refer to it as wlan0.

using WPA security
------------------

As noted above, WEP security was essentially broken, and advice from respected security advisors such as Bruce Schneier was to run open wifi.[*]_





discussion of settings
----------------------

SSID
  Here we state the SSID of the base station we want to connect to.  (SSID
  *can* refer to more than one base station (usually if a company wants to give
  a seamless experiece in a wide area - in this case we can use BSSID which is a
  sort of mac address for base stations)

channel
  We can set the channel to use.  Not always necessary but can be found from the
  data in "ifconfig rum0 list scan"

authmode
  open / shared.  In general WEP is considered not secure.  Shared
  authentication less so.  Use Open for trivial home surfing and watch your SSL
  padlock

wepmode
  on / off
  Kind of obvious

weptxkey
  wep keys need a "slot" - the key itself is known to the client and the AP, but
  each needs to know which slot they are in.  this is seen in ifconfig as

::

  ifconfig
  	status: associated
	ssid HOME channel 6 (2437 Mhz 11g) bssid 00:14:6c:d4:e4:e4
	authmode OPEN privacy ON *deftxkey 1* wepkey 1:104-bit txpower 50
	bmiss 7 scanvalid 60 bgscan bgscanintvl 300 bgscanidle 250

defttxkey - weptkey is deprecated in favour of this term

wepkey
  the key itself, use 0x12345 if 12345 is the HEX version of key

DHCP
  obvious

NB
 - if usng ifconfig on comamnd line put DHCP in early not at end of string.


Well, thats about it for now folks.  This will be an oft-revisited entry I
think.

.. [#] Like scuttlebutt, but comes from reading Google found entries on whatever
   subject you are looking for.  I just made it up cos it sounded good, but
   there are clearly some other interpretations.  I just cannot stop hearing
   David Schwimmer singing "I like big butts ...".  Sad or what.

.. [#] THis is not the same as SSL being broken.  If your neighbour breaks your
   WEP key its as if he has plugged into your wired switch/hub.  He can read all
   your packets.  He can see which porn sites you look at, but if you use SSL to
   enter your credit card details, he cannot get the important information.
   (You do use SSL pages when buying your porn don't you :-).  And when did you
   stop beating your wife ?

.. [#] http://www.schneier.com/blog/archives/2011/04/security_risks_7.html,

.. [#] http://www.schneier.com/blog/archives/2008/01/my_open_wireles.html
