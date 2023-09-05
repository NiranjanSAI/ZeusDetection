import os 


path = "/home/niranjan/FinalProject/john_GET"

def main():
	#i=0

	for filename in os.listdir(path):
		strings= filename.split('.')
		dst = strings[0]+"_get."+strings[1]
		
		os.rename(os.path.join(path,filename),os.path.join(path,dst))
		#i+=1
		print strings


if __name__ == '__main__':
	main()