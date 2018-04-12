#!/bin/bash
#SBATCH --job-name=third
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b
#SBATCH --ntasks=1
##SBATCH --cpus-per-task=4
#SBATCH --mem=24gb
#SBATCH --time=90:00:00
#SBATCH --output=third.log
#SBATCH --array=1-9,22-27,33-35,38-42,50-51,61-80,82-122


date;hostname;pwd

echo -e "This is array task number ${SLURM_ARRAY_TASK_ID}"
run=${SLURM_ARRAY_TASK_ID}


cd histogram${run}
sbatch blat1.sh
cd ..
echo "Blat1 is run"











date
