import os

# path = "/home/niranjan/FinalProject/john_GET/"
# path2 = "/home/niranjan/FinalProject/john_GET_ft/"
# path = "/home/niranjan/FinalProject/simjohn_GET/"
# path2 = "/home/niranjan/FinalProject/simjohn_GET_ft/"
# path = "/home/niranjan/FinalProject/john_tcp/"
# path2 = "/home/niranjan/FinalProject/john_tcp_ft/"
path = "/home/niranjan/FinalProject/Naveen_tcp/"
path2 = "/home/niranjan/FinalProject/Naveen_tcp_ft/"

def main():
	for filename in os.listdir(path):
		current_file=os.path.join(path,filename)
		current_file_size = os.path.getsize(current_file)
		print current_file
		fp1=open(current_file,'r')
		new_file=path2+filename
		fp2=open(new_file,'w')
		logfile=fp1.readlines()
		
		times=[]
		for line in logfile:
			line=line.strip('\n')
			line=line.split(',')
			times.append(line[0])
		print times
		x=len(times)
		for i in range(0,x):
			h=times[i].split('.')
			# print h[0]
			fp2.write(h[0])
			fp2.write('\n')

		fp1.close()
		fp2.close()	
		
		
if __name__ == '__main__':
	main()		