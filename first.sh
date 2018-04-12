#!/bin/bash
#SBATCH --job-name=first
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b
#SBATCH --ntasks=1
##SBATCH --cpus-per-task=4
#SBATCH --mem=24gb
#SBATCH --time=90:00:00
#SBATCH --output=first_%j.log
#SBATCH --array=1-9,22-27,33-35,38-42,50-51,61-80,82-122


date;hostname;pwd

echo -e "This is array task number ${SLURM_ARRAY_TASK_ID}"
run=${SLURM_ARRAY_TASK_ID}

#rm -rf oea_sams
#rm -rf orphan_sams
#rm -rf histogram${run}
#rm -rf genesams${run}
#rm -rf run_this_file
#rm -rf sth.txt

mkdir oea_sams
mkdir orphan_sams
mkdir histogram${run}
mkdir genesams${run}


python createRuns.py  ${run}
echo "CreateRuns done!"
python extractOea.py  ${run}
echo "ExtractOea done!"
python genename_length.py  ${run}
echo "Genename_Length done!"
python create_all_gene_sam.py ${run}
echo "Create_all_gene_sam done!"
date
