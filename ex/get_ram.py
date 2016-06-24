#!/usr/bin/python

"""
git pull
git add <filename>
git commit -m "message"
git pull
git push
"""

import psutil
import pprint
import os

ram = psutil.virtual_memory()

ramOS_info = {}

def get_ramOS_partitions():
	index = 0
	for ram in os:
		total_ram = ram[index]
		free_ram = ram[1]
		swap_space = psutil.swap_memory()[2]
		os_version = 
		kernel_version = os.uname()[2]
		hostname = os.uname()[1]

		ramOS_info = {"total_ram": total_ram,
			      "free_ram": free_ram, 
			      "swap_space": swap_space, 
			      "os_version": os_version,
			      "kernel_version": kernel_version,
			      "hostname": hostname}
		
		return ramOS_info

pprint.pprint(get_ramOS_partitions())
