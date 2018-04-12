import sys
import fileinput
isHLH=int(sys.argv[1])

fil=open("H2s.txt","w")
all_sequences=[]
all_names=[]
all_indices=[]
indices=[]
H_indices=[]
L_indices=[]
all_H_indices=[]
all_L_indices=[]
all_starts=[]
all_ends=[]
starts=[]
ends=[]
if (isHLH):
        name="HLHs.txt"
else:
        name="HLs.txt"

for line in fileinput.FileInput(name, inplace=1):
        print line,
        if("sequenc" in line.split("\t")[0]):
		all_sequences.append(line.split("\t")[1])	
        if(("name" in line.split("\t")[0]) ):
		all_names.append(line.split("\t")[1])
        	
        if(("indice" in line.split("\t")[0])):
		newline=line.split("\t")[1].replace(" ","-")
		for i in range(0, len(newline.split("-"))):
			indices.append(newline.split("-")[i])
			#fil.write(str(newline.split("-")[i])+"\t")
					
		all_indices.append(indices)
		indices=[]
		#fil.write("\n")
#fil.write("length of the all_seq "+ str(len(all_sequences))+"\n")
#fil.write("length of the all_names "+ str(len(all_names))+"\n")
#fil.write("length of the all_indices "+ str(len(all_indices))+"\n")

for x in all_sequences:
	for i in range(0,len(x)):
		if( x[i]=="H"):
			H_indices.append(i)
		if( x[i]=="L"):
			L_indices.append(i)
	all_H_indices.append(H_indices)
	all_L_indices.append(L_indices)
	H_indices=[]
	L_indices=[]
#fil.write("length of the all_H_indices "+ str(len(all_H_indices))+"\n")
#fil.write("length of the all_L_indices "+ str(len(all_L_indices))+"\n")


for j in range(0, len(all_H_indices)):
	for i in range(0, len(all_H_indices[j])):
		where_x=all_H_indices[j][i]
		#fil.write("where_x "+ str(where_x)+"\n")
		if(where_x==0):
			start=0
			end=all_indices[j][where_x]
		else:
			start=all_indices[j][where_x-1]
			#fil.write("start is"+start+"\n")
			end=all_indices[j][where_x]
		starts.append(start)
		ends.append(end)
	all_starts.append(starts)
	all_ends.append(ends)
	starts=[]
	ends=[]
#fil.write("length of the all_starts "+ str(len(all_starts))+"\n")
#fil.write("length of the all_ends "+ str(len(all_ends))+"\n")

for i1 in range(0, len(all_L_indices)):
	for i2 in range(0, len(all_L_indices[i1])):
			#for i3 in range(0,len(all_L_indices[i1][i2])):

				for j2 in range(0,len(all_H_indices[i1])):

#					if(all_L_indices[i1][i2]<all_H_indices[i1][j2]):
					if(all_L_indices[i1][i2]-all_H_indices[i1][j2]== -1):
							
							fil.write(all_names[i1][4:len(all_names[i1])-1]+"\t")
							fil.write(all_starts[i1][j2]+"\t")
							fil.write(all_ends[i1][j2]+"\n")

fil.close()


