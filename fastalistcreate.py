import sys
import fileinput

#File path = new File("./histogram100");
#File[] files = path.listFiles();
#fil=open("files.txt","w")
#for i in files:
#       fil.write(str(i) +"\n")


import os
import glob
sample_number=str(sys.argv[1])
path = './histogram'+sample_number
fil=open("./histogram"+sample_number+"/"+"fastalist","w")
for infile in glob.glob( os.path.join(path, 's*.fasta') ):
        fil.write(infile[len(path)+2:len(infile)-6]+"\n")
