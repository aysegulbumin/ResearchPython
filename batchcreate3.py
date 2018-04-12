import sys 
import fileinput
import subprocess

fil2=open("all_Opera.sh","w")
fil2.write("#!/bin/bash \n #SBATCH --job-name=all_Opera \n#SBATCH --mail-type=END,FAIL \n#SBATCH --mail-user=aysegul.bumin@ufl.edu\n#SBATCH --qos=boucher-b \n#SBATCH --ntasks=1 \n#SBATCH --cpus-per-task=4 \n#SBATCH --mem=24gb \n#SBATCH --time=90:00:00 \n#SBATCH --error=Opera_all.err\n#SBATCH --output=Opera_all.log\n#SBATCH --array=1")
#for line in fileinput.FileInput("/ufrc/boucher/aysegul.bumin/work/uniquenessReport", inplace=1):
#        print line,
#	fil2.write(str(line.split("\t")[0]) +", ")
	
#here we are arranging the batch file so that it just takes the samples which are unique


fil2.write("\ndate;hostname;pwd \n")
fil2.write("run=${SLURM_ARRAY_TASK_ID}\n")
fil2.write("\n")
fil2.write("module load gcc/5.2.0 opera/2.0.6\n")

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
for line2 in fileinput.FileInput("/ufrc/boucher/aysegul.bumin/work/uniquenessReport", inplace=1):
        print line2,
	line=line2.split("\t")[0]
        #fil2.write(str(line.split("\t")[0]) +", ")
	count=0
	fil2.write("head -1000 /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/total"+line+".fa > /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".fa \n")
        #fil2.write("module load gcc/5.2.0 opera/2.0.6\n")
        fil2.write("preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".fa	--illumina-read1  /orange/boucher/shared/data/"+line+"fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/"+line+"rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".map \n")
	
        fil2.write("OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".fa /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".map  /ufrc/boucher/aysegul.bumin/work/output_Opera"+line+"\n")
	#fil2.write(	"wc -l /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/total"+line+".fa\n" )
	#output = subprocess.Popen(["wc -l /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/total"+line+".fa"], stdout=subprocess.PIPE).communicate()[0]
	output = subprocess.check_output("wc -l /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/total"+line+".fa", shell=True)
	output=output.rstrip()
	fil2.write("echo 'Done with Opera"+line+"'\n")
	

	fil2.write("head -"+output+" > /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".fa \n")
        #fil2.write("module load gcc/5.2.0 opera/2.0.6\n")
        fil2.write("preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".fa    --illumina-read1  /orange/boucher/shared/data/"+line+"fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/"+line+"rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".map \n")

        fil2.write("OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".fa /ufrc/boucher/aysegul.bumin/work/histogram"+line+"/head"+line+".map  /ufrc/boucher/aysegul.bumin/work/output_Opera"+line+"\n")
       
	fil2.write("echo 'Done with Opera"+line+"'\n")
	
	fil2.write("cd ..")
        fil2.write("\n")

        fil2.write("\n")
	
	fil2.write("\n")

fil2.write("date\n")
