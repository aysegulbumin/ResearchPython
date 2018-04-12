import sys
import fileinput
import re

sample_number=str(sys.argv[1])
previous=0
w, h = 5000, 4;
My_Matrix= [[0 for x in range(w)] for y in range(h)]
file22=open("write.txt","w")

count=0
d = "|,!?/&-:;@'..."
tel = { }
for line in fileinput.FileInput("H1s.txt", inplace=1):
        print line,
        count=count+1
        myline=line.split("\t")[0]
	#del tel['initial']
	if count==1:
		
		start=int(line.split("\t")[1])
		end=int(line.split("\t")[2])
		tel[myline]=[[start,end]]
		
	else:
		start=int(line.split("\t")[1])
		end=int(line.split("\t")[2])
		if(myline in tel.keys() ):
			tel[myline].append([start,end])
		else:
			tel[myline]=[[start,end]]
count=0
for line in fileinput.FileInput("H2s.txt", inplace=1):
        print line,
        count=count+1
        myline=line.split("\t")[0]
	#del tel['initial']
	if count==1:
		start=int(line.split("\t")[1])
		end=int(line.split("\t")[2])
		tel[myline]=[[start,end]]
	else:
		start=int(line.split("\t")[1])
		end=int(line.split("\t")[2])
		if(myline in tel.keys() ):
			tel[myline].append([start,end])
		else:
			tel[myline]=[[start,end]]
count2=0
for x in tel.keys():
	#print "These are the names of the genes"
	#print x
	count2=count2+1
	fil=open("sam"+str(count2)+".sam","w")
	for line2 in fileinput.FileInput("/ufrc/boucher/aysegul.bumin/work/all"+str(sample_number)+".sam",inplace=1):
		print line2,
		line4=line2
		iline=''.join(w for w in re.split("["+"\\".join(d)+"]", line4.split("\t")[2]) if w)
		iline=iline.replace(" ","")
		iline=iline.replace("\n","")
		
		if(x in iline):
			fil.write(line2)
			



def add_toMatrix(line,start,end):
        global My_Matrix
	'''        
	file22.write("\nstart\n")
        file22.write(str(start))
        file22.write("\t >= \t")
        file22.write(line.split("\t")[3])
        file22.write("\n"+str(end))
        file22.write("\t >= \t")
        file22.write(str((len(str(line.split("\t")[9]))+int(line.split("\t")[3]))))
       	'''
	if(int(start) <= int(line.split("\t")[3]) and (len(str(line.split("\t")[9]))+int(line.split("\t")[3]))<=int(end) ):
        #THERE MAY BE SOME ISSUE IN THIS IF STATEMENT CHECK PLEASE
        #OnLy add the reads that are in range of the H1
              	#file22.write("entered\n")
                start2 = int(line.split('\t')[3])
                end2= start2+ len(str(line.split("\t")[9]))
                for i in range(start2,end2):
                        if(str(line.split("\t")[9])[i-start2]=="A"):
                                        My_Matrix[0][i]=My_Matrix[0][i]+1
                        elif(str(line.split("\t")[9])[i-start2]=="C"):
                                        My_Matrix[1][i]=My_Matrix[1][i]+1
                        elif(str(line.split("\t")[9])[i-start2]=="G"):
                                        My_Matrix[2][i]=My_Matrix[2][i]+1
                        elif(str(line.split("\t")[9])[i-start2]=="T"):
                                        My_Matrix[3][i]=My_Matrix[3][i]+1
                        else:
                                print "ERROR"


def create_contig(line):
                global My_Matrix
                temp_contig=""
                max=0
                max_base=-1 #0 denotes A , 1 denotes C , 2 denotes G and 3 denotes T
                for i in range(0,3500):
                        for j in range(0,4):
                                if(My_Matrix[j][i]>max):
                                        max=My_Matrix[j][i]
                                        if(max!=0):
                                                max_base=j
                        if(max_base==0):
                                temp_contig+="A"
                        if(max_base==1):
                                temp_contig+="C"
                        if(max_base==2):
                                temp_contig+="G"
                        if(max_base==3):
                                temp_contig+="T"
                        max=0
                        max_base=-1
                return temp_contig
count3=0
fil4=open("contiglist","w")
for name in tel.keys():
	count3=count3+1
	fil3=open("contig"+str(count3),"w")
	fil4.write("contig"+str(count3)+"\n")
	for arr in tel[name]:
		#print "printingArray"
		#print arr
		start=arr[0]
		end=arr[1]
		for i in  fileinput.FileInput("sam"+str(count3)+".sam",inplace=1):			
			print	i,
			'''
			print "\n"
			print i 
			print "hello	"
			'''			
			add_toMatrix(i,start,end)
	line="not necessary"
	contig=create_contig(line)
	#print "done"
	fil3.write(">OEA_contig"+str(count3)+"\tlength\t"+str(len(str(contig)))+"\tgenename\t"+str(name[0:10])+" \n")
	fil3.write(str(contig))
	fil3.write("\n")	

'''

print 'B:'
print tel['B'][0][0]
print tel['B'][0][1]


print 'A:'
print tel['A'][0][0]
print tel['A'][0][1]
print tel['A'][1][0]
print tel['A'][1][1]
'''
