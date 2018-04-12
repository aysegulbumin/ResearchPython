import fileinput
import sys
result=[]
file2=[]
sample_number=str(sys.argv[1])
with open('ordered_oea'+sample_number+'.sam', 'w') as file:
	for line2 in fileinput.FileInput("oea"+sample_number+".sam", inplace=1):
		print line2 ,
	file2= sorted(open("oea"+sample_number+".sam").readlines(), key=lambda line: int(line.split('\t')[3]))
	for eachline in file2:
		file.write(eachline)
		#file.write("\n")
