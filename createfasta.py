import sys 
import fileinput
import re
d = "|,.!?/&-:;@'..."
one_or_two=str(sys.argv[1])


fil2=open("fasta"+str(one_or_two)+"list.txt","a")

for line in fileinput.FileInput("H"+str(one_or_two)+"s.txt", inplace=1):
        print line,
	
	for line2 in fileinput.FileInput("megares_database_v1.01.fasta", inplace=1):
        	print line2,
		if(line2[0]==">"):
			newline=''.join(w for w in re.split("["+"\\".join(d)+"]", line2) if w)
			newline=newline.replace(" ","")
			newline=newline.replace("\n","")
			if(line.split("\t")[0] in newline):
				flag=1	
				savedline=line2
				savednewline=line.split("\t")[0]
			else:
				flag=0
		if(line2[0]!=">" and flag==1):
			new_seq= line2[int(line.split("\t")[1]):int(line.split("\t")[2])]
			fil=open("s"+savednewline+".fasta", "a")
			
			fil.write(savedline)
			fil.write(new_seq)
			fil.write("\n")
			fil2.write(savednewline+"\n")
			flag=0
						
					
								
		
	
