# Network-Backup
This is a script to login to network devices, pull the configuration, and backup.  This is running off Python 3.6 and Netmiko. 

Warning that a lot of this is me learning to code, while working on a project. This uses the Netmiko library to handle SSH connections between network devices. ( https://github.com/ktbyers/netmiko ) 

Currently the script has two files.  The main script, and devices.py. 
The goal is to imput all device information into devices.py, and then let the script do it's thing.  Current version will run through all devices, grab a "show run" and "show vlan" and output it to a file under the backupfiles subdirectory. 

Things on my to do list: 
1) Split functions between switches and routers so that router backups aren't plagued with "Ambiguous Command" when it tries to do a show vlan on it. 

2) Since a "show run" on a cisco switch doesn't actually show the vlan database configuration, I have the script run a "show vlan" instead so that one could manually input vlan info if necessary.  However I'd like to format the show vlan output into a script that creates said vlan's into a script to easily input back into a switch if say, you brought in a new switch that had no vlan info. 

3) Obscuring or Encrypting passwords.  Right now the passwords are in plain text, at best I can obscure it with base64 or something, but that sounds really really bad.  Ideally you should be creating a backup user with limited access to only pull "show run" and "show vlan"

4) Hella testing.  This thing is like a day old?   So here is what I have personally validated: 
CentOS 7 with Python 3.6 and pip3.6 install of Netmiko. 
Cisco 1921 Router running IOS 15.1
Cisco 3560 Switch running IOS 12.2

5) Better error reporting. Currently it just says it couldn't connect, but doesn't differentiate between legitimatey not being able to connect and the script got whatever the robot equivilant of being kidnapped by mole-people is.   So at some point I'll create useful error messages.  I also plan to create a faillog so failures are documented instead of displayed on screen. 

This is ultimately being made for an environment with Cisco ASA's, and Nexus switches along with standard IOS devices, likely running on Windows.  Ideally I would like to allow it to pull PFsense configurations as well, but that is likely going to be a different function.  
