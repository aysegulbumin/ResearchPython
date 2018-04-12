#!/bin/bash 
 #SBATCH --job-name=automate 
#SBATCH --mail-type=END,FAIL 
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=4 
#SBATCH --mem=24gb 
#SBATCH --time=90:00:00 
#SBATCH --output=automate.log
#SBATCH --array=1
date;hostname;pwd 
run=${SLURM_ARRAY_TASK_ID}

cat output_idba24/contig24.fa	contig1	contigs24.fa 
cat output_idba24/contigs24.fa       contig2  | tee   contigs24.fa 
cat output_idba24/contigs24.fa       contig3  | tee   contigs24.fa 
cat output_idba24/contigs24.fa       contig4  | tee   contigs24.fa 
cat output_idba27/contigs27.fa       contig1  | tee   contigs27.fa 
cat output_idba27/contigs27.fa       contig2  | tee   contigs27.fa 
cat output_idba27/contigs27.fa       contig3  | tee   contigs27.fa 
cat output_idba103/contigs103.fa       contig1  | tee   contigs103.fa 
cat output_idba103/contigs103.fa       contig2  | tee   contigs103.fa 
cat output_idba103/contigs103.fa       contig3  | tee   contigs103.fa 
cat output_idba103/contigs103.fa       contig4  | tee   contigs103.fa 
cat output_idba103/contigs103.fa       contig5  | tee   contigs103.fa 
cat output_idba103/contigs103.fa       contig6  | tee   contigs103.fa 
cat output_idba103/contigs103.fa       contig7  | tee   contigs103.fa 
cat output_idba103/contigs103.fa       contig8  | tee   contigs103.fa 
cat output_idba70/contigs70.fa       contig1  | tee   contigs70.fa 
cat output_idba70/contigs70.fa       contig2  | tee   contigs70.fa 
cat output_idba70/contigs70.fa       contig3  | tee   contigs70.fa 
cat output_idba70/contigs70.fa       contig4  | tee   contigs70.fa 
cat output_idba70/contigs70.fa       contig5  | tee   contigs70.fa 
cat output_idba70/contigs70.fa       contig6  | tee   contigs70.fa 
cat output_idba70/contigs70.fa       contig7  | tee   contigs70.fa 
cat output_idba73/contigs73.fa       contig1  | tee   contigs73.fa 
cat output_idba73/contigs73.fa       contig2  | tee   contigs73.fa 
cat output_idba118/contigs118.fa       contig1  | tee   contigs118.fa 
cat output_idba118/contigs118.fa       contig2  | tee   contigs118.fa 
cat output_idba118/contigs118.fa       contig3  | tee   contigs118.fa 
cat output_idba118/contigs118.fa       contig4  | tee   contigs118.fa 
cat output_idba122/contigs122.fa       contig1  | tee   contigs122.fa 
cat output_idba122/contigs122.fa       contig2  | tee   contigs122.fa 
cat output_idba122/contigs122.fa       contig3  | tee   contigs122.fa 
cat output_idba2/contigs2.fa       contig1  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig2  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig3  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig4  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig5  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig6  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig7  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig8  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig9  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig10  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig11  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig12  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig13  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig14  | tee   contigs2.fa 
cat output_idba2/contigs2.fa       contig15  | tee   contigs2.fa 
cat output_idba61/contigs61.fa       contig1  | tee   contigs61.fa 
cat output_idba61/contigs61.fa       contig2  | tee   contigs61.fa 
cat output_idba74/contigs74.fa       contig1  | tee   contigs74.fa 
cat output_idba74/contigs74.fa       contig2  | tee   contigs74.fa 
cat output_idba77/contigs77.fa       contig1  | tee   contigs77.fa 
cat output_idba77/contigs77.fa       contig2  | tee   contigs77.fa 
cat output_idba7/contigs7.fa       contig1  | tee   contigs7.fa 
cat output_idba7/contigs7.fa       contig2  | tee   contigs7.fa 
cat output_idba7/contigs7.fa       contig3  | tee   contigs7.fa 
cat output_idba7/contigs7.fa       contig4  | tee   contigs7.fa 
cat output_idba7/contigs7.fa       contig5  | tee   contigs7.fa 
cat output_idba7/contigs7.fa       contig6  | tee   contigs7.fa 
cat output_idba7/contigs7.fa       contig7  | tee   contigs7.fa 
cat output_idba7/contigs7.fa       contig8  | tee   contigs7.fa 
date
