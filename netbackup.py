#!/usr/bin/python3.6 -B
import datetime
import re
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoAuthenticationException
from netmiko import ConnectHandler
from devices import allthethings, vlan, novlan 
from pathlib import Path

# 
#Currently using the option for placing vlan configuration as a script.  
#You can change it by commenting out #inlineSwitch and uncommenting ciscoSwitch at the bottom of the script
#


# Imports above provide the following functions:
# get timestamp, SSH to devices, Import all the devices form file, and check to see if file 
# that we want to write to exists. 
#
# This gives us a timestamp we will need for our filenames
now = datetime.datetime.now()


# Dir check
dircheck = Path('backupfiles/')
if dircheck.is_dir():
	print("placing files in ./backupfiles")
else:
	print("./backupfiles does not exist, creating...")
	Path('backupfiles/').mkdir(parents=True, exist_ok=True)

#
# Cycles through all the devices stored in devices.py
# Then does the following: 
# 1) grabs the hostname to use for filename variable
# 2) performs a show run stores in output variable
# 3) Checks to see if the file exists in yyyymmdd format. If yes, uses yyyymmddhhmmss. 
# 4) writes output to file
# 5) Get's robot-beer for job well done
#

#
# Process Things that only need a show run. 
#
def ciscoRun(stuff):
	for things in stuff:
		try: 
			net_connect = ConnectHandler(**things)
		except:
			print("Skipping " + things['ip'] + " something happened")
		else:
			output = net_connect.send_command('show run view full | inc hostname')
			hostname = output[9:]
			output = net_connect.send_command('show run view full')
			filecheck = Path('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d"))
			if filecheck.exists():
				saveoutput = open('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d%H%M%S"), "w")
			else:
				saveoutput = open('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d"), "w")
	
			saveoutput.write(output)
			saveoutput.close
			print("backed up " + things['ip'] + " successfully!")


#
# Process Cisco Switches. 
#

def ciscoSwitch(stuff):
	for things in stuff: 
		try:
			net_connect = ConnectHandler(**things)
		except:
			print("Skipping " + things['ip'] + " something happened")
		else:
			output = net_connect.send_command('show run view full | inc hostname')
			hostname = output[9:]
			output = net_connect.send_command('show run view full')
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
			print("backed up " + things['ip'] + " successfully!")


#
# This is similar to ciscoSwitch except that it formats vlan info as a script
# This way pasting the script into a switch will also restore vlan names and descriptions
# Mostly complete, I just need to make some edits to remove the "building configuration..."
# and "Current configuration :" lines from the resulting file so copy / pasting the file into 
# a switch doesn't cause errors
#

def inlineCSwitch(stuff):
	for things in stuff: 
		try:
			net_connect = ConnectHandler(**things)
		except:
			#raise  #for debugging this part. 
			print("Skipping " + things['ip'] + " something happened")
		else:
			vlanSplice = re.compile(r'^\d+\s+\S+\s+active', re.MULTILINE)
			rmBuilding = re.compile(r'Building configuration...\n\nCurrent configuration.*')
			output = net_connect.send_command('show run view full | inc hostname')
			hostname = output[9:]
			output = net_connect.send_command('show run view full')
			outClean = rmBuilding.sub('!', output)
			vlan = net_connect.send_command('show vlan')
			filecheck = Path('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d"))
			if filecheck.exists():
				saveoutput = open('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d%H%M%S"), "w")
			else:
				saveoutput = open('backupfiles/' + hostname + "-" + now.strftime("%Y%m%d"), "w")
			vlanStore = vlanSplice.findall(vlan)
			for item in vlanStore:
				numberName = item.split()
				saveoutput.write("!\nvlan " + numberName[0] + "\n name " + numberName[1] + "\n")
			saveoutput.write(outClean)
			saveoutput.close
			print("backed up " + things['ip'] + " successfully!")


#  you can comment out either inlineCSwitch or ciscoSwitch depending on which output you want. 

ciscoRun(novlan)
inlineCSwitch(vlan)
#ciscoSwitch(vlan)

