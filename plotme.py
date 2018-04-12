import sys
import fileinput
import os
import glob
import subprocess

sample_number=str(sys.argv[1])
path = './histogram'+sample_number
#fil=open("./histogram"+sample_number+"/"+"list","w")

fil2=open("./histogram"+sample_number+"/"+"plotthis.py","w")
fil2.write("import numpy as np\n")
fil2.write("import pylab\n")
fil2.write("import matplotlib.pyplot as plt\n")
fil2.write("\n")


for infile in glob.glob( os.path.join(path, 'Amr2scaff*.psl') ):
        #fil.write(infile[len(path)+1:len(infile)]+"\n")
	count=0

	for line in fileinput.FileInput("./histogram"+sample_number+"/"+infile[len(path)+1:len(infile)], inplace=1):
        	print line,
		count=count+1
		filewritecount=0
		if (count>5):
			#fil.write("match"+line.split("\t")[0] +"\t target size"++ "\n")
			if(int(line.split("\t")[17])==1): #block size, if it is one then draw one second line 
 				fil2.write("#Target size\n")
				filewritecount=filewritecount+1
				fil2.write("x"+str(filewritecount)+","+"y"+str(filewritecount)+"=[0,"+str(line.split("\t")[14])+"],[3,3]\n")
				fil2.write("#Second line\n")
				filewritecount=filewritecount+1
				fil2.write("x"+str(filewritecount)+","+"y"+str(filewritecount)+"=["+str(int(line.split("\t")[15]))+","+ str(int(line.split("\t")[15])+int(line.split("\t")[18].split(",")[0]))+"],[3,3]\n")
				filewritecount=filewritecount+1
				fil2.write("x"+str(filewritecount)+","+"y"+str(filewritecount)+"=[0,0],[5,5]\n")
				fil2.write("plt.plot(x1, y1, color='magenta', marker = 's',linewidth=15.0)\n")
				fil2.write("plt.plot(x2, y2,color='chartreuse', marker = 's',linewidth=15.0)\n")
				fil2.write("plt.plot("+"x"+str(filewritecount)+","+"y"+str(filewritecount)+", marker = 's',linewidth=2)\n")
				output = subprocess.check_output("grep -A 1 '"+str(line.split('\t')[13])+"'  ./output_Opera"+sample_number+"/scaffoldSeq.fasta", shell=True)
				fil3=open("./histogram"+sample_number+"/"+str(line.split('\t')[13])+".fasta","w")
				fil3.write(str(output))
				fil2.write("plt.savefig('"+str(line.split("\t")[13])+"')\n")
				fil2.write("plt.show()\n")
				
			else:#if block size is not one then draw multiple second lines.
				fil2.write("#Target size\n")
				filewritecount=filewritecount+1
				mystring="plt.plot("
				fil2.write("x"+str(filewritecount)+","+"y"+str(filewritecount)+"=[0,"+str(line.split("\t")[14])+"],[3,3]\n")
				
				count2=0
				for i in line.split("\t")[18].split(","):
					if(i!=" " and i!=''):
						fil2.write("#Second line\n")
						filewritecount=filewritecount+1	
						mystring=mystring+"x"+str(filewritecount)+","+"y"+str(filewritecount)+","		
						fil2.write("x"+str(filewritecount)+","+"y"+str(filewritecount)+"=["+str(int(line.split("\t")[20].split(",")[count2]))+","+ str(int(line.split("\t")[20].split(",")[count2])+int(i))+"],[3,3]\n")
						count2=count2+1
				filewritecount=filewritecount+1
				fil2.write("x"+str(filewritecount)+","+"y"+str(filewritecount)+"=[0,0],[5,5]\n")
				mystring=mystring+"color='chartreuse', marker = 's',linewidth=15.0)\n"
				fil2.write("plt.plot(x1, y1, color='magenta', marker = 's',linewidth=15.0)\n")				
				fil2.write(mystring)
				
				fil2.write("plt.plot("+"x"+str(filewritecount)+","+"y"+str(filewritecount)+", marker = 's',linewidth=2)\n")
				output = subprocess.check_output("grep -A 1 '"+str(line.split('\t')[13])+"'  ./output_Opera"+sample_number+"/scaffoldSeq.fasta", shell=True)
				fil3=open("./histogram"+sample_number+"/"+str(line.split('\t')[13])+".fasta","w")
				fil3.write(str(output))
				fil2.write("plt.savefig('"+str(line.split("\t")[13])+"')\n")
				fil2.write("plt.show() \n")
				
					
			
