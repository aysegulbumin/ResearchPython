import sys 
import fileinput


fil2=open("blat2.sh","w")
fil2.write("#!/bin/bash \n #SBATCH --job-name=blat2 \n #SBATCH --mail-type=END,FAIL \n#SBATCH --mail-user=aysegul.bumin@ufl.edu\n #SBATCH --qos=boucher-b \n#SBATCH --ntasks=1 \n #SBATCH --cpus-per-task=4 \n #SBATCH --mem=24gb \n #SBATCH --time=90:00:00 \n #SBATCH --output=blat2.log\n #SBATCH --array=1\n date;hostname;pwd \n")
count=0
for line in fileinput.FileInput("fastalist", inplace=1):
	print line,
	count=count+1
	fil2.write("module load blat \n blat "+"/ufrc/boucher/aysegul.bumin/work/output_Opera"+sample_number+"/scaffoldSeq.fasta"+" s"+str(line[:-1])+".fasta  "+ "Amr2scaff"+str(count)+".psl\n"  )
	fil2.write("\n")

fil2.write("date\n")
