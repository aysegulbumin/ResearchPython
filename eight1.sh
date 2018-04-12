#!/bin/bash
#SBATCH --job-name=eigth
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b
#SBATCH --ntasks=1
##SBATCH --cpus-per-task=4
#SBATCH --mem=50gb
#SBATCH --time=90:00:00
#SBATCH --output=eight%j.log
#SBATCH --array=2


date;hostname;pwd

echo -e "This is array task number ${SLURM_ARRAY_TASK_ID}"
run=${SLURM_ARRAY_TASK_ID}

module load gcc/5.2.0 opera/2.0.6


cp ./histogram${run}/total${run}.fa ./Opera/c.fa

preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/Opera/c.fa  --illumina-read1 /orange/boucher/shared/data/${run}fnoncow.fastq  --illumina-read2 /orange/boucher/shared/data/${run}rnoncow.fastq  --out /ufrc/boucher/aysegul.bumin/work/o${run}

mkdir /ufrc/boucher/aysegul.bumin/work/opera_output${run}

OPERA-LG /ufrc/boucher/aysegul.bumin/work/Opera/c.fa /ufrc/boucher/aysegul.bumin/work/o${run} /ufrc/boucher/aysegul.bumin/work/opera_output${run}

echo "Opera is done"

cd ..









date

