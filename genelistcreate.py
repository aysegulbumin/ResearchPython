import sys
import fileinput

#File path = new File("./histogram100");
#File[] files = path.listFiles();
#fil=open("files.txt","w")
#for i in files:
#	fil.write(str(i) +"\n")


import os
import glob
sample_number=str(sys.argv[1])
path = './histogram'+sample_number
fil=open("./histogram"+sample_number+"/"+"genelist","w")
for infile in glob.glob( os.path.join(path, 'post*.txt') ):
	fil.write(infile[len(path)+1:len(infile)-4]+"\n")
    #print "current file is: " + infile
