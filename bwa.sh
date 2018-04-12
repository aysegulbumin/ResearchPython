#!/bin/bash
#SBATCH --job-name=bwa
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b
#SBATCH --ntasks=1
##SBATCH --cpus-per-task=4
#SBATCH --mem=24gb
#SBATCH --time=90:00:00
#SBATCH --output=bwa_%j.log
#SBATCH --array=1-9,22-27,33-35,38-42,50-51,61-80,82-122

date;hostname;pwd
module load bwa
module load samtools
echo -e "This is array task number ${SLURM_ARRAY_TASK_ID}"
run=${SLURM_ARRAY_TASK_ID}



bwa aln /ufrc/boucher/aysegul.bumin/work/database/megares_database_v1.01.fasta /orange/boucher/shared/data/${run}fnoncow.fastq > /ufrc/boucher/aysegul.bumin/work/sai_files/${run}_1.sai

bwa aln /ufrc/boucher/aysegul.bumin/work/database/megares_database_v1.01.fasta /orange/boucher/shared/data/${run}rnoncow.fastq > /ufrc/boucher/aysegul.bumin/work/sai_files/${run}_2.sai

bwa sampe -n 1000 /ufrc/boucher/aysegul.bumin/work/database/megares_database_v1.01.fasta /ufrc/boucher/aysegul.bumin/work/sai_files/${run}_1.sai /ufrc/boucher/aysegul.bumin/work/sai_files/${run}_2.sai /orange/boucher/shared/data/${run}fnoncow.fastq /orange/boucher/shared/data/${run}rnoncow.fastq > /ufrc/boucher/aysegul.bumin/work/sam_files/align${run}.sam


date
