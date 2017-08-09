==========
Free Wi-Fi
==========

==========

It is increasingly hard to find wifi hardware that supports
free-as-in-speech drivers - that is finding a USB wifi dongle for your
laptop is becoming impossible.  So I went to the `FSF approved
<https://www.fsf.org/resources/hw/endorsement/tehnoetic>`_ company
`Tehnoetic <https://tehnoetic.com/>`_ and put down some hard-earned
for a mini-dongle and a high gain dongle and antenna that assuredly will
be using a chipset that has a free driver.


Excitedly I am sitting in a cafe about to plug them in, and why not blog about it.

Plugging in the mini-dongle, I get

::

   [  502.208147] usb 5-3: new high-speed USB device number 5 using ehci-pci
   [  502.356966] usb 5-3: New USB device found, idVendor=0cf3, idProduct=9271
   [  502.356981] usb 5-3: New USB device strings: Mfr=16, Product=32, SerialNumber=48
   [  502.356991] usb 5-3: Product: UB93
   [  502.356999] usb 5-3: Manufacturer: ATHEROS
   [  502.357007] usb 5-3: SerialNumber: 12345
   [  502.770802] usb 5-3: ath9k_htc: Firmware htc_9271.fw requested
   [  502.770879] usb 5-3: firmware: failed to load htc_9271.fw (-2)
   [  502.770891] usb 5-3: Direct firmware load failed with error -2
   [  502.770898] usb 5-3: Falling back to user helper
   [  502.771133] usbcore: registered new interface driver ath9k_htc
   [  502.775096] usb 5-3: ath9k_htc: USB layer deinitialized

Hmmm.

Lets start by confirming what `dmesg` tells us - what is the USB device.

::

   Bus 005 Device 005: ID 0cf3:9271 Atheros Communications, Inc. AR9271 802.11n

OK. So its the AR9271 chipset, which apparently uses the ath9k_htc driver.
Aha the online blurb (on my iPhone!) tells me 'firmware is required'

Great, I need a binary firmware (presumably on the Atheros chipset) to run my free driver.
This is silly guys. Its the 21C!  I really am worried about the state of wifi support in the
F/OSS world.

So , I dutifully tether my iPhone with my old-and-not-free dongle, and `apt-get install firmware-atheros`

::

   [ 1915.380977] usb 5-3: Manufacturer: ATHEROS
   [ 1915.380985] usb 5-3: SerialNumber: 12345
   [ 1915.381969] usb 5-3: ath9k_htc: Firmware htc_9271.fw requested
   [ 1915.400560] usb 5-3: firmware: direct-loading firmware htc_9271.fw
   [ 1915.682688] usb 5-3: ath9k_htc: Transferred FW: htc_9271.fw, size: 51272
   [ 1915.920587] ath9k_htc 5-3:1.0: ath9k_htc: HTC initialized with 33 credits
   [ 1916.195731] ath9k_htc 5-3:1.0: ath9k_htc: FW Version: 1.3
   [ 1916.195744] ath: EEPROM regdomain: 0x65
   [ 1916.195751] ath: EEPROM indicates we should expect a direct regpair map
   [ 1916.195760] ath: Country alpha2 being used: 00
   [ 1916.195770] ath: Regpair used: 0x65
   [ 1916.200591] ath: EEPROM regdomain: 0x833a
   [ 1916.200600] ath: EEPROM indicates we should expect a country code
   [ 1916.200606] ath: doing EEPROM country->regdmn map search
   [ 1916.200612] ath: country maps to regdmn code: 0x37
   [ 1916.200617] ath: Country alpha2 being used: GB
   [ 1916.200621] ath: Regpair used: 0x37
   [ 1916.200626] ath: regdomain 0x833a dynamically updated by country IE
   [ 1916.202135] ieee80211 phy2: Atheros AR9271 Rev:1
   [ 1916.520638] systemd-udevd[3209]: renamed network interface wlan0 to wlan3

horaah - it loads the firmware OK. And renames wlan for some reason.
Ok, `udev` is the Linux device manager, and it is the one responsible for loading the firmware
and generally dealing with devices attached to the system buses.

udev generates rules (/lib/udev/rules.d/...) and those rules are stored in (/etc/udev/rules.d/70-persistent-net.rules) and they show me

::

   # USB device 0x:0x (rt73usb)
   SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="00:22:75:fd:d7:8a", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="wlan*", NAME="wlan2"

   # USB device 0x:0x (ath9k_htc)
   SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="60:02:b4:99:94:c5", ATTR{dev_id}=="0x0", ATTR{type}=="1", KERNEL=="wlan*", NAME="wlan3"


So the rules are written each time a new wlan device is found, and the
match is based on the, obviously now i think about it, MAC address of
the device.

Killing off the previous rules and re-plugging does the needful and I have wlan0 back.
I then rerun my tethering script and all is well with the world.  uploading this blog post ... now !
