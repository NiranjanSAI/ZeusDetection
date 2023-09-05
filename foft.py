import os 

path = "/home/niranjan/FinalProject/john_ft/"
def main():
	for filename in os.listdir(path):
		current_file=os.path.join(path,filename)
		#current_file_size = os.path.getsize(current_file)
		print current_file
		fp1=open(current_file,'r')
		
		
if __name__ == '__main__':
	main()		