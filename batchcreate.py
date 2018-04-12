import sys 
import fileinput


fil2=open("cat.sh","w")
fil2.write("#!/bin/bash \n #SBATCH --job-name=automate \n#SBATCH --mail-type=END,FAIL \n#SBATCH --mail-user=aysegul.bumin@ufl.edu\n#SBATCH --qos=boucher-b \n#SBATCH --ntasks=1 \n#SBATCH --cpus-per-task=4 \n#SBATCH --mem=24gb \n#SBATCH --time=90:00:00 \n#SBATCH --output=cat.log\n#SBATCH --array=1")
#for line in fileinput.FileInput("/ufrc/boucher/aysegul.bumin/work/uniquenessReport", inplace=1):
#        print line,
#	fil2.write(str(line.split("\t")[0]) +", ")
	
#here we are arranging the batch file so that it just takes the samples which are unique


fil2.write("\ndate;hostname;pwd \n")
fil2.write("run=${SLURM_ARRAY_TASK_ID}\n")
fil2.write("\n")

#fil2.write("module load seqtk\n")
#fil2.write("seqtk subseq /orange/boucher/shared/data/${run}fnoncow.fastq /ufrc/boucher/aysegul.bumin/work/frontname${run}.txt > f_${run}.fastq \n")
#fil2.write("seqtk subseq /orange/boucher/shared/data/${run}rnoncow.fastq /ufrc/boucher/aysegul.bumin/work/reversename${run}.txt > r_${run}.fastq \n")
#fil2.write("module load idba\n")
#fil2.write("fq2fa --merge --filter f_${run}.fastq r_${run}.fastq  ${run}.fasta\n")
#fil2.write("mkdir output_idba${run} \n")
#fil2.write("idba_ud -r ${run}.fasta -o output_idba${run} \n")
#fil2.write("cp output_idba${run}/contig.fa output_idba${run}/contig${run}.fa \n")
#fil2.write("python sam.py ${run} \n")
count=0
for line in fileinput.FileInput("/ufrc/boucher/aysegul.bumin/work/uniquenessReport", inplace=1):
        print line,
        #fil2.write(str(line.split("\t")[0]) +", ")
	count=0
	for line2 in  fileinput.FileInput("/ufrc/boucher/aysegul.bumin/work/histogram"+str(line.split("\t")[0])+"/contiglist", inplace=1):
		print line2,	
		count=count+1
		if count==1:
			fil2.write("rm -rf    histogram"+str(line.split("\t")[0])+"/contigs"+str(line.split("\t")[0])+".fa \n")
			fil2.write("rm -rf    histogram"+str(line.split("\t")[0])+"/total"+str(line.split("\t")[0])+".fa \n")
			fil2.write("touch       histogram"+str(line.split("\t")[0])+"/contigs"+str(line.split("\t")[0])+".fa \n")

			fil2.write("cat output_idba"+str(line.split("\t")[0])+"/contig.fa	histogram"+str(line.split("\t")[0])+"/"+str(line2.rstrip('\n'))+" 	histogram"+str(line.split("\t")[0])+"/contigs"+str(line.split("\t")[0])+".fa \n")
		else:

			fil2.write("cat histogram"+str(line.split("\t")[0])+"/contigs"+str(line.split("\t")[0])+".fa       histogram"+str(line.split("\t")[0])+"/"+str(line2.rstrip('\n'))+"  | tee   histogram"+str(line.split("\t")[0])+"/contigs"+str(line.split("\t")[0])+".fa \n") #output is redirected to the same file 
	fil2.write("cat output_idba"+str(line.split("\t")[0])+"/contig.fa       histogram"+str(line.split("\t")[0])+"/contig1       histogram"+str(line.split("\t")[0])+"/contigs"+str(line.split("\t")[0])+".fa > histogram"+str(line.split("\t")[0])+"/total"+str(line.split("\t")[0])+".fa\n")
fil2.write("date\n")
