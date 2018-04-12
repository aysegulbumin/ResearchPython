import sys 
import fileinput
import re
gene_sam_file=str(sys.argv[1])
sample_number=str(sys.argv[2])
length_of_gene=0
gene_len=0

myline=""
once=0
array=[0]*4500

fil=open("sth.txt","a")

def get_length(name_of_gene):
        global length_of_gene
	global gene_len
        for line in fileinput.FileInput("genesname_length"+sample_number+".txt", inplace=1):
                print line,
		if(name_of_gene in line):
			#fil.write("name of gene "+ name_of_gene)
			#fil.write("\n")
			#fil.write("line "+ line + "\n")
			length_of_gene=int(line.split("\t")[1])
			#fil.write("length of gene"+ str(length_of_gene)+"\n")
			gene_len= length_of_gene
def add_toMatrix(line):
	global array
	start = int(line.split('\t')[3])#starts at position
	end= start+ int(len(str(line.split("\t")[9])))#ends at position + length 
	for i in range(start,end):
		array[i]=array[i]+1


#file2= open('./histogram'+str(sample_number)+"/"+myline+'.txt', 'a')
for line in fileinput.FileInput("./genesams"+str(sample_number)+"/"+gene_sam_file, inplace=1):
	print line ,
	once=once+1
	if(once==1):
		myline=str(line.split('\t')[2]) #Take the gene's name
		get_length(myline)#get length of that particular gene
		#array=[0]*gene_len
	add_toMatrix(line)
if(myline!=""):
	d="|,.!?/&-:;@'..."
	iline=''.join(w for w in re.split("["+"\\".join(d)+"]", myline) if w)
	iline=iline.replace(" ","")
	file2= open('./histogram'+str(sample_number)+"/"+ iline +'.txt', 'a')
else:
	file2= open('./histogram'+str(sample_number)+"/"+myline +'.txt', 'a')
file3=open('./histogram'+str(sample_number)+"/"+'array'+myline[0:10], 'a')
#file3.write(myline+"\n")
count=0
vans=0
for x in array :
	if(count<gene_len):
		file2.write(str(count+1)+"\t"+str(x)+"\n")#+myline+"\n")
		file3.write(str(x)+" ")
	count=count+1
file3.write("\n")
if(gene_len==0):
	file3.write("-1 ")
	file2.write("-1 ")


#file2.write("\t"+myline)
#file2.write("\n")
