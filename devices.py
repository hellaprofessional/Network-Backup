#!/usr/bin/python3.6 -B
#
# Put devices in as shown below. 
# Then place in the appropriate list at the bottom. 
#
# device_type keys can be found here:
# https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
#
# Script Currently supports cisco_ios and cisco_asa. 
# cisco_asa module config, and cisco_nxos testing soon
# 
# brocade_fastiron, & juniper_junos testing will likely happen soon. # Main script will call this file, and import "allthethings" 
# and cycle through all the item, then close.  


c3560 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.19.17',
        'username': 'backupuser',
        'password': 'hellasecure',
}

asa5506 = {
        'device_type': 'cisco_asa',
        'ip': '192.168.19.18',
        'username': 'backupuser',
        'password': 'password',
	'secret': 'enable',
}

c1951 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.19.19',
        'username': 'backupuser',
        'password': 'hellasecure',
}


backupPath = "backupfiles/"
vlan = [c3560]
novlan = [c1951]
asa = [asa5506]
