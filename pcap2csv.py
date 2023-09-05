import os

path = "/home/niranjan/FinalProject/captureJohn"
#filters = " -Y \"http.request.method==\"POST\"\"  " 
filters = " -Y \"http.request.method==\"GET\"  \"  " 

fields =  " -T fields -e frame.time_relative -e frame.time_delta -e ip.src -e ip.dst -E separator=, > "


def main():
	for filename in os.listdir(path):
		strings= filename.split('.')
		os.system("cd FinalProject/CaptureJohn")
		p2c= "tshark -r "+ filename + filters + fields + strings[0]+".csv"
		os.system(p2c)
		os.system("cd")
		print strings

if __name__ == '__main__':
	main()		