#!/usr/bin/python3.6 -B
import datetime
from netmiko import ConnectHandler
from devices import allthethings 
from pathlib import Path

# Imports above provide the following functions:
# get timestamp, SSH to devices, Import all the devices form file, and check to see if file 
# that we want to write to exists. 
#
# This gives us a timestamp we will need for our filenames
now = datetime.datetime.now()

#
# Cycles through all the devices stored in devices.py
# Then does the following: 
# 1) grabs the hostname to use for filename variable
# 2) performs a show run stores in output variable
# 3) Checks to see if the file exists in yyyymmdd format. If yes, uses yyyymmddhhmmss. 
# 4) writes output to file
# 5) Get's robot-beer for job well done
#

for things in allthethings:
	try: 
		net_connect = ConnectHandler(**things)
		output = net_connect.send_command('show run | inc hostname')
		hostname = output[9:]
		output = net_connect.send_command('show run')
		vlan = net_connect.send_command('show vlan')
		filecheck = Path('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d"))
		if filecheck.exists():
			saveoutput = open('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d%H%M%S"), "w")
		else:
			saveoutput = open('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d"), "w")
	
		saveoutput.write(output)
		saveoutput.write("\n--------\n")
		saveoutput.write(vlan)
		saveoutput.close
	except:
		print("Skipping " + things['ip'] + " couldn't connect")
