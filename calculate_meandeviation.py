import sys 
import fileinput
from random import randint

#length_of_s=int(sys.argv[1])
n_many_times=int(sys.argv[1])
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

def find_bigmean(some_Array,line):
	l=len(some_Array)
	c=0
	#ten percent of the length of the array
	length_of_s=int(l/10)
	total=0
	if(l-100-length_of_s<100 or l<100 or l<l-100-length_of_s):
		filee=open("error.txt","a")
		filee.write("Not in range  " +str(line)+ "\n")
		filee.write("length  " +str(l)+ "\n")
		filee.write("length of s  " +str(length_of_s)+ "\n")
		return 0
	else:
		for i in range(0,n_many_times):
			random=randint(100,l-100-length_of_s)
			total=total+ find_mean(array[random:random+length_of_s])
		return total/ n_many_times
fil3=open("listgene2","a")
	
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
		fil=open("mean"+str(line[4:len(line)-1])+".txt","w")
		fil2=open("meanall_mean.txt","a")
		#fil3=open("listgene2","a")
		fil.write("name"+"\t"+str(line[:len(line)-1])+"\n")
		fil2.write("name"+"\t"+str(line[:len(line)-1])+"\n")
		fil.write("mean"+"\t"+str(bigmean)+"\n")
		fil2.write("mean"+"\t"+str(bigmean)+"\n")
		fil.write("standard_deviation"+"\t"+str(deviation)+"\n")
		fil2.write("standard_deviation"+"\t"+str(deviation)+"\n")
		fil3.write(line[:len(line)-1]+"\t"+str(bigmean)+"\t"+str(deviation)+"\n")		
		#some extra calculations follows
		
		arrayCount[count2]=count
		meanArray.append(bigmean)
		deviationArray.append(deviation)
		
		
		count=0
		count2=count2+1
		array=[0]*4500

