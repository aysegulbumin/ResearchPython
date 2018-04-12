import sys
import fileinput
import os
import glob
sample_number=str(sys.argv[1])
path = './histogram'+sample_number
#fil=open("./histogram"+sample_number+"/"+"list","w")
fil=open("./histogram"+sample_number+"/"+"uniqueness","w")
fil2=open("./histogram"+sample_number+"/"+"not_uniqueness","w")
for infile in glob.glob( os.path.join(path, 'res1_*.psl') ):
        #fil.write(infile[len(path)+1:len(infile)]+"\n")
	count=0
	for line in fileinput.FileInput("./histogram"+sample_number+"/"+infile[len(path)+1:len(infile)], inplace=1):
        	print line,
		count=count+1
		if (count>5):
			#fil.write("match"+line.split("\t")[0] +"\t target size"++ "\n")
			if(int(line.split("\t")[0]) <= 0.8 * (int(line.split("\t")[10]))):
				fil.write("Unique")
			else:
				fil2.write("NotUnique")

			
