import os
import scipy
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np

# path = "/home/niranjan/FinalProject/john_GET_ft/"
path = "/home/niranjan/FinalProject/john_tcp_ft/"
# path = "/home/niranjan/FinalProject/simjohn_GET_ft/"
# path = "/home/niranjan/FinalProject/Naveen_tcp_ft/"

N=12000*4  #Sampling Time
T=1	#Sample Spacing 
def main():
	print "HEllo"
	for file in os.listdir(path):
		current_file=os.path.join(path,file)
		fp1=open(current_file,'r')
		logfile=fp1.readlines()
		print file
		times=[]
		for line in logfile:
			# print int(line)

			times.append(int(line))
		x=[]	
		# for i in range(0,N):
		# 	x.append(times.count(i)) 	

		for i in range(0,N/60):
			interval=list(range(i+1,i+61))
			icount=0
			for item in interval:
				icount+=times.count(item)
			x.append(icount)	
		print x				
		y=[]
		for item in x:
			y.append(float(item)/sum(x))
		


		
		xf=scipy.fftpack.fft(y)
		len(xf)
		tf = np.linspace(0.0, 1.0/(2.0*T), N/60)
		len(tf)
		plt.plot(tf, 2.0/N * np.abs(xf))
		plt.grid()
		plt.show()
		
		
if __name__=='__main__':
	main()