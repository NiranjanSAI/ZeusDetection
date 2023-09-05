import os
from scipy.fftpack import fft
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

path = "/home/niranjan/FinalProject/john_GET_ft/"
# path = "/home/niranjan/FinalProject/john_tcp_ft/"
# path = "/home/niranjan/FinalProject/Naveen_tcp_ft/"

N=24000*2  #Sampling Time
T=0.01	#Sample Spacing 
fs=500
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
		print max(times)
		x=[]			
		# for i in range(0,N):
		# 	if i in times:
		# 		x.append(times.count(i))
		# 	else:
		# 		x.append(0)	

		for i in range(0,N/60):
			interval=list(range(i+1,i+61))
			icount=0
			for item in interval:
				icount+=times.count(item)
			x.append(icount)	
		y=[]
		for item in x:
			y.append(float(item)/sum(x))


		# ps=np.abs(np.fft.fft(x))**2
		# time_step = 10
		# freqs=np.fft.fftfreq(len(x),time_step)
		# idx=np.argsort(freqs)

		# plt.plot(freqs[idx],ps[idx])
		# plt.grid()
		# plt.show()

		f, Pxx_spec = signal.welch(y, fs, 'flattop', 1024, scaling='spectrum')
		
		plt.subplot(211)
		plt.semilogy(f, np.sqrt(Pxx_spec))
		plt.xlabel('frequency [Hz]')
		plt.ylabel('Linear spectrum [V RMS]')



		plt.subplot(212)	
		plt.psd(x,2000,fs)
		plt.show()
		# f, Pxx_den = signal.periodogram(x, fs)
		# plt.semilogy(f, Pxx_den)
		# plt.xlabel('frequency [Hz]')
		# plt.ylabel('PSD [V**2/Hz]')
		# plt.show()
		
		
if __name__=='__main__':
	main()