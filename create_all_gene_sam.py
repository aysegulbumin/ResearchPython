import sys
import fileinput
#import numpy as np

num=0

sample_number=str(sys.argv[1])


for each_line in fileinput.FileInput("genesname_length"+sample_number+".txt", inplace=1):
        print each_line,
        my_gene=str(each_line.split("\t")[0])

	with open("run_this"+str(sample_number)+".sh", "a") as text_file:
		text_file.write("\n")
		my_string="python array.py "
		my_string=my_string+ "gene"+str(num)+".sam" +"\t"+ sample_number
		text_file.write(my_string)
		text_file.write("\n")
                my_string="python postprocess.py "
                my_string=my_string+ "gene"+str(num)+".sam" +"\t"+ sample_number
                text_file.write(my_string)


        with open("./genesams"+str(sample_number)+"/"+'gene'+str(num)+'.sam', 'w') as file0:
                for line0 in fileinput.FileInput("all"+sample_number+".sam", inplace=1):
                        print line0,
                        #if(str(line0.split("\t")[2])==my_gene):
                        if(my_gene[1:] in str(line0)):
                                file0.write(line0)

     
        num=num+1
     

with open("run_this"+str(sample_number)+".sh", "a") as text_file:
                text_file.write("\n")
                text_file.write("python genelistcreate.py "+sample_number+"\n")
		text_file.write("date")
