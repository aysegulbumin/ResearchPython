import fileinput
import sys

sample_number=str(sys.argv[1])
fil_first=open("front_orphan"+sample_number+".sam","w")
fil_second=open("reverse_orphan"+sample_number+".sam","w")
fil_third=open("frontname"+sample_number+".txt","w")
fil_four=open("reversename"+sample_number+".txt","w")
fil_=open("NUMBER","w")
count=0
with open('all'+sample_number+'.sam', 'w' ) as files2:
	with open('firstmapped'+sample_number+'.sam', 'w' ) as file2:
		with open('secondmapped'+sample_number+'.sam', 'w' ) as file3:
			for line in fileinput.FileInput("./sam_files/align"+sample_number+".sam", inplace=1):
				print line ,
				if( line[0]!="@") :
					count=count+1
					line=line
					if(int (line.split("\t")[1])==73):
						file2.write(line)
						files2.write(line)
					if(int (line.split("\t")[1]) == 137):
						file3.write(line)
						files2.write(line)
					if(int (line.split("\t")[1])==65):
						files2.write(line)
					if(int (line.split("\t")[1]) == 129):
						files2.write(line)					
			#			file2.write("The MAPQ is as follows: \n")	
			#			file2.write(line.split("\t")[4])
			#			file2.write("\n")
					if(int (line.split("\t")[1])== 77):
						fil_first.write(line)
						fil_third.write(line.split("\t")[0]+"/1\n")
					if(int (line.split("\t")[1])== 141):
                                                fil_second.write(line)
						fil_four.write(line.split("\t")[0]+"/2\n")
fil_.write(str(count))
