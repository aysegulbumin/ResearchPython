import sys 
import fileinput
from random import randint
import re

#length_of_s=int(sys.argv[1])
n_many_times=int(sys.argv[1])
coefficient=int(sys.argv[2])#for now it is 2 
lthreshold=int(sys.argv[3])#for now it is 200
fl=int(sys.argv[4])#for now it is 200
fr=int(sys.argv[5])#for now it is 200
#find mean
#l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
#print reduce(lambda x, y: x + y, l) / len(l)
#print(randint(0, 9))
#-------------------------THIS PART IS COPIED--------------------------

def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data,mymean):
    """Return sum of square deviations of sequence data."""
    c = mymean
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof, mymean):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        return 0
    ss = _ss(data,mymean)
    pvar = ss/(n-ddof)
    return pvar**0.5

#------------------------------------------------------------------------
def find_mean(some_Array):
	return reduce(lambda x, y: x+y,some_Array) / float(len(some_Array))
meanArray=[]
deviationArray=[]
arrayCount=[0]*4500
array=[]
count2=0
count=0
bigmean=0
deviation=0
array2=[]
letterarray=[]
indexarray=[]
countones=0
countzeros=0
previous=0
countie=0
genes=dict()
d = "|,.!?/&-:;@'..."

def find_bigmean(some_Array,line):
	l=len(some_Array)
	c=0
	#ten percent of the length of the array
	length_of_s=int(l/10)
	total=0
	if(l-100-length_of_s<100 or l<100 or l<l-100-length_of_s):
		return 0
	else:
		for i in range(0,n_many_times):
			random=randint(100,l-100-length_of_s)
			total=total+ find_mean(array[random:random+length_of_s])
		return total/ n_many_times
for line2 in fileinput.FileInput("genesname_length.txt",inplace=1):
	print line2,
	name_gene=line2.split("\t")[0]
	name_gene=''.join(w for w in re.split("["+"\\".join(d)+"]", name_gene) if w)
	name_gene=name_gene.replace(" ","")
	name_gene=name_gene.replace("\n","")
	name_gene=name_gene.replace(">","")
	value_gene=int(line2.split("\t")[1])
	genes.update({name_gene:value_gene})
	

	
	
	
	
for line in fileinput.FileInput("genelist", inplace=1):
	print line,
	if("post.txt" not in line[0:len(line)-1]):
		#nothing
	
		for line2 in fileinput.FileInput(str(line[:len(line)-1])+".txt", inplace=1):
			print line2,
			array.append(int(line2.split(",")[1]))
			count=count+1
		bigmean=find_bigmean(array,line)
		deviation=stddev(array,0,bigmean)
		#printing operations
		#some extra calculations follows
		for x in array:
			if(x <=bigmean+deviation ):
				array2.append(0)
			else:
				array2.append(1)
		fil2=open("highlows.txt","a")
		fil3=open("n"+str(line)+".txt","w")
		#fil2.write("name"+"\t"+str(line[:len(line)-1])+"\n")
		fil2.write("sequence\t")
		countthis=0
		for y in array2 :
			fil2.write(str(y) +" ")
			fil3.write(str(countthis+1)+",")
			countthis=countthis+1
			if(previous==y and y==0):
				fil3.write(str(10)+"\n")
				countzeros=countzeros+1
				previous=y
			elif(previous==y and y==1):
				if(letterarray[-1]=="H"):
					fil3.write(str(0)+"\n")
				else:
					fil3.write(str(10)+"\n")
				countones=countones+1
				previous=y
			elif(previous!=y and y==1):
				fil3.write(str(10)+"\n")
				if(countzeros>=lthreshold):
					letterarray.append("L")#low and long enough
					indexarray.append(countie)
				else:	
					letterarray.append("X") #not long enough but low
					indexarray.append(countie)
				previous=y
				countones=1
				countzeros=0
			elif(previous!=y and y==0):
				if(countones>=fl):
					fil3.write(str(0)+"\n")
					letterarray.append("H")#high and long enough
					indexarray.append(countie)
				else:	
					fil3.write(str(10)+"\n")
					letterarray.append("Y") #not long enough but high				
					indexarray.append(countie)
				countzeros=1
				countones=0
				previous=y
			else:
				letterarray.append("N") #not known
			countie=countie+1 
		countie=0
		fil2.write("\n")
		fil2.write("letters\t")
		for a in letterarray:
			fil2.write(str(a)+" ")
		fil2.write("\n")
		fil2.write("name"+"\t"+str(line[:len(line)-1])+"\n")
		fil2.write("indices\t")
		for a in indexarray:
			fil2.write(str(a)+" ")	
		fil2.write("\n")					
		arrayCount[count2]=count
		meanArray.append(bigmean)
		deviationArray.append(deviation)
		
		buckets = []
		bucket_range=genes.get(str(line[4:len(line)-1]))#in order to understand how many items to add to the bucket dictionary is used look up the name and it will give the size so that many times append the coverage to the mean 
		for i in xrange(0,bucket_range):
			buckets.append(bigmean+0.3)
		countH=0
		for x in letterarray:
			
			if( x== 'H'):
				if(countH==0):
					start_ones=0
				else:
					start_ones=indexarray[countH-1]
				end_ones=indexarray[countH]
				for i in range(start_ones,end_ones):#when there is a H region then the coverage there should be set to zero to visualize better in the graph
					buckets[i]=0
			countH=countH+1					
		
		fil4=open("cov"+str(line[4:len(line)-1])+".txt","w")
		countt=0
		for m in buckets:
			countt=countt+1
			fil4.write(str(countt)+","+str(m)+"\n")
		fil4.close()
		
		buckets=0
		count=0
		count2=count2+1
		array=[]
		letterarray=[]
		array2=[]
		indexarray=[]
		previous=0
