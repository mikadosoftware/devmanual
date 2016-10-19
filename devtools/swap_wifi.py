#!/usr/bin/python
tmpl = '''
source /etc/network/interfaces.d/*
# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
allow-hotplug eth0
iface eth0 inet dhcp

auto {wlanX}
iface {wlanX} inet dhcp
wpa-ssid "{ssid}"
wpa-psk {password}
pre-up iptables-restore < /etc/iptables.rules
'''

import sys
import subprocess

WLAN = 'wlan1'

def write_apply(networkName=None, tmpl=None, datad=None):
    
    interfacesPath = '/etc/network/interfaces'
    open(interfacesPath,'w').write(tmpl.format(**datad))
    print "{networkName} written".format(networkName=networkName)    
    print subprocess.check_call("ifdown {wlanX}".format(**datad), shell=True)
    print
    print subprocess.check_call("ifup {wlanX}".format(**datad), shell=True)


    
if __name__== '__main__':
    try:
        arg = sys.argv[1:][0]
    except:
        print "no arg,"
        arg = None
    if arg == 'iphone':
        d = {'ssid': '''Paul's iPhone''',
             'password': 'qwerty12',
             'wlanX': WLAN
            }
        write_apply(networkName='iphone', tmpl=tmpl, datad=d)
    elif arg == 'vfast':
        d = {'ssid': 'VFast PB',
             'password': '15056894',
             'wlanX': WLAN
            }
        write_apply(networkName='vfast', tmpl=tmpl, datad=d)
    elif arg == 'enalion':
        d = {'ssid': 'ENALION',
             'password': 'enalion!',
             'wlanX': WLAN
            }
        write_apply(networkName='enalion', tmpl=tmpl, datad=d)        
    else:
        print "Nothing try iphone or vfast or enalion"
        sys.exit(0)

