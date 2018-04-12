#!/bin/bash 
 #SBATCH --job-name=automate 
#SBATCH --mail-type=END,FAIL 
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=4 
#SBATCH --mem=24gb 
#SBATCH --time=90:00:00 
#SBATCH --output=cat.log
#SBATCH --array=1
date;hostname;pwd 
run=${SLURM_ARRAY_TASK_ID}

rm -rf    histogram24/contigs24.fa 
rm -rf    histogram24/total24.fa 
touch       histogram24/contigs24.fa 
cat output_idba24/contig.fa	histogram24/contig1 	histogram24/contigs24.fa 
cat histogram24/contigs24.fa       histogram24/contig2  | tee   histogram24/contigs24.fa 
cat histogram24/contigs24.fa       histogram24/contig3  | tee   histogram24/contigs24.fa 
cat histogram24/contigs24.fa       histogram24/contig4  | tee   histogram24/contigs24.fa 
cat output_idba24/contig.fa       histogram24/contig1       histogram24/contigs24.fa > histogram24/total24.fa
rm -rf    histogram27/contigs27.fa 
rm -rf    histogram27/total27.fa 
touch       histogram27/contigs27.fa 
cat output_idba27/contig.fa	histogram27/contig1 	histogram27/contigs27.fa 
cat histogram27/contigs27.fa       histogram27/contig2  | tee   histogram27/contigs27.fa 
cat histogram27/contigs27.fa       histogram27/contig3  | tee   histogram27/contigs27.fa 
cat output_idba27/contig.fa       histogram27/contig1       histogram27/contigs27.fa > histogram27/total27.fa
rm -rf    histogram103/contigs103.fa 
rm -rf    histogram103/total103.fa 
touch       histogram103/contigs103.fa 
cat output_idba103/contig.fa	histogram103/contig1 	histogram103/contigs103.fa 
cat histogram103/contigs103.fa       histogram103/contig2  | tee   histogram103/contigs103.fa 
cat histogram103/contigs103.fa       histogram103/contig3  | tee   histogram103/contigs103.fa 
cat histogram103/contigs103.fa       histogram103/contig4  | tee   histogram103/contigs103.fa 
cat histogram103/contigs103.fa       histogram103/contig5  | tee   histogram103/contigs103.fa 
cat histogram103/contigs103.fa       histogram103/contig6  | tee   histogram103/contigs103.fa 
cat histogram103/contigs103.fa       histogram103/contig7  | tee   histogram103/contigs103.fa 
cat histogram103/contigs103.fa       histogram103/contig8  | tee   histogram103/contigs103.fa 
cat output_idba103/contig.fa       histogram103/contig1       histogram103/contigs103.fa > histogram103/total103.fa
rm -rf    histogram70/contigs70.fa 
rm -rf    histogram70/total70.fa 
touch       histogram70/contigs70.fa 
cat output_idba70/contig.fa	histogram70/contig1 	histogram70/contigs70.fa 
cat histogram70/contigs70.fa       histogram70/contig2  | tee   histogram70/contigs70.fa 
cat histogram70/contigs70.fa       histogram70/contig3  | tee   histogram70/contigs70.fa 
cat histogram70/contigs70.fa       histogram70/contig4  | tee   histogram70/contigs70.fa 
cat histogram70/contigs70.fa       histogram70/contig5  | tee   histogram70/contigs70.fa 
cat histogram70/contigs70.fa       histogram70/contig6  | tee   histogram70/contigs70.fa 
cat histogram70/contigs70.fa       histogram70/contig7  | tee   histogram70/contigs70.fa 
cat output_idba70/contig.fa       histogram70/contig1       histogram70/contigs70.fa > histogram70/total70.fa
rm -rf    histogram73/contigs73.fa 
rm -rf    histogram73/total73.fa 
touch       histogram73/contigs73.fa 
cat output_idba73/contig.fa	histogram73/contig1 	histogram73/contigs73.fa 
cat histogram73/contigs73.fa       histogram73/contig2  | tee   histogram73/contigs73.fa 
cat output_idba73/contig.fa       histogram73/contig1       histogram73/contigs73.fa > histogram73/total73.fa
rm -rf    histogram118/contigs118.fa 
rm -rf    histogram118/total118.fa 
touch       histogram118/contigs118.fa 
cat output_idba118/contig.fa	histogram118/contig1 	histogram118/contigs118.fa 
cat histogram118/contigs118.fa       histogram118/contig2  | tee   histogram118/contigs118.fa 
cat histogram118/contigs118.fa       histogram118/contig3  | tee   histogram118/contigs118.fa 
cat histogram118/contigs118.fa       histogram118/contig4  | tee   histogram118/contigs118.fa 
cat output_idba118/contig.fa       histogram118/contig1       histogram118/contigs118.fa > histogram118/total118.fa
rm -rf    histogram122/contigs122.fa 
rm -rf    histogram122/total122.fa 
touch       histogram122/contigs122.fa 
cat output_idba122/contig.fa	histogram122/contig1 	histogram122/contigs122.fa 
cat histogram122/contigs122.fa       histogram122/contig2  | tee   histogram122/contigs122.fa 
cat histogram122/contigs122.fa       histogram122/contig3  | tee   histogram122/contigs122.fa 
cat output_idba122/contig.fa       histogram122/contig1       histogram122/contigs122.fa > histogram122/total122.fa
rm -rf    histogram2/contigs2.fa 
rm -rf    histogram2/total2.fa 
touch       histogram2/contigs2.fa 
cat output_idba2/contig.fa	histogram2/contig1 	histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig2  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig3  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig4  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig5  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig6  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig7  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig8  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig9  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig10  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig11  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig12  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig13  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig14  | tee   histogram2/contigs2.fa 
cat histogram2/contigs2.fa       histogram2/contig15  | tee   histogram2/contigs2.fa 
cat output_idba2/contig.fa       histogram2/contig1       histogram2/contigs2.fa > histogram2/total2.fa
rm -rf    histogram61/contigs61.fa 
rm -rf    histogram61/total61.fa 
touch       histogram61/contigs61.fa 
cat output_idba61/contig.fa	histogram61/contig1 	histogram61/contigs61.fa 
cat histogram61/contigs61.fa       histogram61/contig2  | tee   histogram61/contigs61.fa 
cat output_idba61/contig.fa       histogram61/contig1       histogram61/contigs61.fa > histogram61/total61.fa
rm -rf    histogram74/contigs74.fa 
rm -rf    histogram74/total74.fa 
touch       histogram74/contigs74.fa 
cat output_idba74/contig.fa	histogram74/contig1 	histogram74/contigs74.fa 
cat histogram74/contigs74.fa       histogram74/contig2  | tee   histogram74/contigs74.fa 
cat output_idba74/contig.fa       histogram74/contig1       histogram74/contigs74.fa > histogram74/total74.fa
rm -rf    histogram77/contigs77.fa 
rm -rf    histogram77/total77.fa 
touch       histogram77/contigs77.fa 
cat output_idba77/contig.fa	histogram77/contig1 	histogram77/contigs77.fa 
cat histogram77/contigs77.fa       histogram77/contig2  | tee   histogram77/contigs77.fa 
cat output_idba77/contig.fa       histogram77/contig1       histogram77/contigs77.fa > histogram77/total77.fa
rm -rf    histogram7/contigs7.fa 
rm -rf    histogram7/total7.fa 
touch       histogram7/contigs7.fa 
cat output_idba7/contig.fa	histogram7/contig1 	histogram7/contigs7.fa 
cat histogram7/contigs7.fa       histogram7/contig2  | tee   histogram7/contigs7.fa 
cat histogram7/contigs7.fa       histogram7/contig3  | tee   histogram7/contigs7.fa 
cat histogram7/contigs7.fa       histogram7/contig4  | tee   histogram7/contigs7.fa 
cat histogram7/contigs7.fa       histogram7/contig5  | tee   histogram7/contigs7.fa 
cat histogram7/contigs7.fa       histogram7/contig6  | tee   histogram7/contigs7.fa 
cat histogram7/contigs7.fa       histogram7/contig7  | tee   histogram7/contigs7.fa 
cat histogram7/contigs7.fa       histogram7/contig8  | tee   histogram7/contigs7.fa 
cat output_idba7/contig.fa       histogram7/contig1       histogram7/contigs7.fa > histogram7/total7.fa
date
