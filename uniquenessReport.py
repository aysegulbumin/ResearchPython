import sys
import fileinput
import re
sample_numbers=[100,105,108,120,1,3,4,5,22,23,24,25,26,27,33,34,82,83,84,85,86,87,88,89,103,104,106,107,109,110,111,112,113,114,40,41,42,70,71,72,73,101,102,50,51,62,90,91,9,115,116,117,118,119,121,122,2,35,38,39,61,63,64,65,66,67,68,69,6,74,75,76,77,78,79,7,99,98,97,96,95,94,93,92,80]
fil=open("uniquenessReport","w")
fil2=open("notuniquenessReport","w")
for i in sample_numbers:
	for line in fileinput.FileInput("./histogram"+str(i)+"/uniqueness", inplace=1):
        	print line,
		if("Unique" in line):
			fil.write(str(i)+ "\tis Unique\n")
	for line in fileinput.FileInput("./histogram"+str(i)+"/not_uniqueness", inplace=1):
		print line,
        	if("NotUnique" in line):
			fil2.write(str(i)+ "\tis Not Unique\n")
