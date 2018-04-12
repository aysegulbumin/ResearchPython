import fileinput
import sys
count=0
newline=""
sample_number=str(sys.argv[1])
with open('genesname_length'+sample_number+'.txt', 'w') as file0:
	for line0 in fileinput.FileInput("megares_database_v1.01.fasta", inplace=1):
		print line0,
		count = count+1 
		if(count==1):
			length=int(len(line0))
			newline=newline+line0[:length-1]
		if(count==2):
			count=0
			newline=newline+"\t"
			newline=newline+ str(len(line0))
			newline=newline+"\n"
			file0.write(newline)
			newline=""

			

