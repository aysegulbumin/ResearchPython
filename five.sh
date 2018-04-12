#!/bin/bash
#SBATCH --job-name=five
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b
#SBATCH --ntasks=1
##SBATCH --cpus-per-task=4
#SBATCH --mem=250gb
#SBATCH --time=90:00:00
#SBATCH --output=five%j.log
#SBATCH --array=100
#24,27,103,70,73,118,122,2,61,74,77,7
#-9,22-27,33-35,38-42,50-51,61-80,82-122


date;hostname;pwd

echo -e "This is array task number ${SLURM_ARRAY_TASK_ID}"
run=${SLURM_ARRAY_TASK_ID}


module load seqtk
echo "seqtk starts"

seqtk subseq /orange/boucher/shared/data/${run}fnoncow.fastq frontname${run}.txt > f_${run}.fastq
echo "1"
seqtk subseq /orange/boucher/shared/data/${run}rnoncow.fastq reversename${run}.txt > r_${run}.fastq

echo "2"

echo "seqtk done"

echo "idba starts"

module load idba-ud

fq2fa --merge --filter f_${run}.fastq r_${run}.fastq  ${run}.fasta

echo "fq2fa done"

mkdir output_idba${run}

idba_ud -r ${run}.fasta -o output_idba${run}

echo "idba done"

cd output_idba${run}

cp contig.fa contig${run}.fa

cd ..

echo "Done"











date
