=================================
Basics of routing on your own LAN
=================================


.. sidebar:: historical note

   Well this might be a little out of date :-)

I wanted to add my laptop to marshallfamily SSID ::

  ifconfig_ath0="ssid marshallfamily wepmode on weptxkey 1 wepkey 1:xxxxxxx"


  ifconfig ath0 ssid marshallfamily wepmode on weptxkey 1 wepkey 1:xxxxxxx

but cannot seem to connect it and bind to ip address


so force it ::

  ifconfig ath0 192.168.1.3 netmask 255.255.255.0

then force a default route to the router that this connects too ::

  net add default 192.168.1.1
