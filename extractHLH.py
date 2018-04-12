import sys 
import fileinput
 
isHLH=int(sys.argv[1])
#if 1 then looks for HLH regions and if 0 looks for HL or LH regions 
met=0
def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:    return True
    if n == 0:    return False
 
    # If last characters of two strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)
 
    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)

for line in fileinput.FileInput("highlows.txt", inplace=1):
	print line,
	if("letter" in line.split("\t")[0]):
		#d = "|,.!?/&-:;@'..."
		#newline=''.join(w for w in re.split("["+"\\".join(d)+"]", line.split("\t")[0]) if w)
                newline=(line.split("\t")[1]).replace(" ","")
                newline=newline.replace("\n","")
		string1="HLH"
		string2=newline
		m=len(string1)
		n = len(string2)
		if(isHLH):
			fil=open("HLHs.txt","a")
			#fil.write("newline is "+str(newline)+"\n")
#			if isSubSequence(string1, string2, m, n):
			if("HLH" in newline):
				fil.write("sequence\t")
				fil.write(str(newline))
				fil.write("\n")
				met=1
			else:
				met=0
		else:
			fil=open("HLs.txt","a")
                        #fil.write("newline is "+str(newline)+"\n")
#                       if isSubSequence(string1, string2, m, n):
                        if("LH" in newline or "HL"in newline):
                                fil.write("sequence\t")
                                fil.write(str(newline))
                                fil.write("\n")
                                met=1
                        else:
                                met=0
	if(("name" in line.split("\t")[0]) and met==1):
		fil.write(str(line))
	if(("indice" in line.split("\t")[0]) and met==1):
		fil.write(str(line))
		
		#else:
    			#fil.write("NO")
			#fil.write("\n")
		fil.close()			
