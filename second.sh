#!/bin/bash
#SBATCH --job-name=second
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b
#SBATCH --ntasks=1
##SBATCH --cpus-per-task=4
#SBATCH --mem=24gb
#SBATCH --time=90:00:00
#SBATCH --output=second.log
#SBATCH --array=1-9,22-27,33-35,38-42,50-51,61-80,82-122


date;hostname;pwd

echo -e "This is array task number ${SLURM_ARRAY_TASK_ID}"
run=${SLURM_ARRAY_TASK_ID}

cp calculate_meandeviation.py ./histogram${run}
cp calculate_meandeviation2.py ./histogram${run}
cp extractHLH.py ./histogram${run}
cp getH1.py ./histogram${run}
cp getH2.py ./histogram${run}
cp createfasta.py ./histogram${run}
cp blatcreate1.py ./histogram${run}
cp fastalistcreate.py ./histogram${run}
cp isUnique.py ./histogram${run}
cp mega* ./histogram${run}

cd ./histogram${run}
rm -rf post.txt
cd ..
python genelistcreate.py ${run}
cp ./genesname_length${run}.txt ./histogram${run}/genesname_length.txt
cd ./histogram${run}

python calculate_meandeviation.py 100 
echo "Done calculatemean"
python calculate_meandeviation2.py 100 2 200 200 200 
echo "Done calculatemean2"

python extractHLH.py 0 
echo "Done extractHLH"

python getH1.py 0  
echo "Done GETH1"

python getH2.py 0
echo "Done GETH2"

python createfasta.py 1 

echo "Done createfasta1"

python createfasta.py 2 

echo "Done createfasta2"

cd ..


python fastalistcreate.py ${run}
echo "Done fastalistcreate"

cd ./histogram${run}

python blatcreate1.py
echo "Done blatcreate1"






cd ..





date
