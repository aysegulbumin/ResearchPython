#!/bin/bash
#SBATCH --job-name=seven
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b
#SBATCH --ntasks=1
##SBATCH --cpus-per-task=4
#SBATCH --mem=10gb
#SBATCH --time=90:00:00
#SBATCH --output=seven%j.log
#SBATCH --array=1


date;hostname;pwd

echo -e "This is array task number ${SLURM_ARRAY_TASK_ID}"
run=${SLURM_ARRAY_TASK_ID}
python batchcreate.py
sbatch cat.sh











date
