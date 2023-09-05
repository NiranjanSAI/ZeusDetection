import os
# path = "/home/niranjan/FinalProject/john_GET/"
# path = "/home/niranjan/FinalProject/john_tcp/"
# path = "/home/niranjan/FinalProject/john_POST/"
path = "/home/niranjan/FinalProject/Naveen_tcp/"

def main():
	for file in os.listdir(path):
		current_file=os.path.join(path,file)
		fp1=open(current_file,'r')
		logfile=fp1.readlines()
		print file
		outgoing=0
		incoming=0
		for line in logfile:
			if line.split(",")[2] =="172.20.114.97":
				outgoing+=1
		
			elif line.split(",")[3] =="172.20.114.97":
				incoming+=1
		ratio = outgoing/float(incoming)	
		print ratio
		print outgoing
		print incoming
		break
			
if __name__=='__main__':
	main()