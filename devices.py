#
# Put devices in as shown below. 
# Then place in the "allthethings" list at the bottom. 
#
# Main script will call this file, and import "allthethings" 
# and cycle through all the item, then close.  
#
# device_type keys can be found here:
# https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
#
# Script Currently supports cisco_ios and presumably cisco_nxos & cisco_asa
# 
# brocade_fastiron, & juniper_junos testing will likely happen soon. 
#

c3560 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.19.17',
        'username': 'backupuser',
        'password': 'hellasecure',
}

c4506 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.19.18',
        'username': 'backupuser',
        'password': 'hellasecure',
}

c1951 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.19.19',
        'username': 'backupuser',
        'password': 'hellasecure',
}

#
# I'm playing with classes of objects.  Currently script uses 'allthethings'
# but I will be splitting from vlan & novlan shortly. Eventually it will split
# off further when we get to non-cisco devices
#

vlan = [c3560, c4506]
novlan = [c1951]
allthethings = vlan + novlan 
