#!/bin/bash 
 #SBATCH --job-name=all_Opera 
#SBATCH --mail-type=END,FAIL 
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --qos=boucher-b 
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=4 
#SBATCH --mem=24gb 
#SBATCH --time=90:00:00 
#SBATCH --error=Opera_all.err
#SBATCH --output=Opera_all.log
#SBATCH --array=1
date;hostname;pwd 
run=${SLURM_ARRAY_TASK_ID}

module load gcc/5.2.0 opera/2.0.6
head -1000 /ufrc/boucher/aysegul.bumin/work/histogram24/total24.fa > /ufrc/boucher/aysegul.bumin/work/histogram24/head24.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram24/head24.fa	--illumina-read1  /orange/boucher/shared/data/24fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/24rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram24/head24.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram24/head24.fa /ufrc/boucher/aysegul.bumin/work/histogram24/head24.map  /ufrc/boucher/aysegul.bumin/work/output_Opera24
echo 'Done with Opera24'
head -388986 /ufrc/boucher/aysegul.bumin/work/histogram24/total24.fa > /ufrc/boucher/aysegul.bumin/work/histogram24/head24.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram24/head24.fa    --illumina-read1  /orange/boucher/shared/data/24fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/24rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram24/head24.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram24/head24.fa /ufrc/boucher/aysegul.bumin/work/histogram24/head24.map  /ufrc/boucher/aysegul.bumin/work/output_Opera24
echo 'Done with Opera24'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram27/total27.fa > /ufrc/boucher/aysegul.bumin/work/histogram27/head27.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram27/head27.fa	--illumina-read1  /orange/boucher/shared/data/27fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/27rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram27/head27.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram27/head27.fa /ufrc/boucher/aysegul.bumin/work/histogram27/head27.map  /ufrc/boucher/aysegul.bumin/work/output_Opera27
echo 'Done with Opera27'
head -423798 /ufrc/boucher/aysegul.bumin/work/histogram27/total27.fa > /ufrc/boucher/aysegul.bumin/work/histogram27/head27.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram27/head27.fa    --illumina-read1  /orange/boucher/shared/data/27fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/27rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram27/head27.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram27/head27.fa /ufrc/boucher/aysegul.bumin/work/histogram27/head27.map  /ufrc/boucher/aysegul.bumin/work/output_Opera27
echo 'Done with Opera27'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram103/total103.fa > /ufrc/boucher/aysegul.bumin/work/histogram103/head103.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram103/head103.fa	--illumina-read1  /orange/boucher/shared/data/103fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/103rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram103/head103.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram103/head103.fa /ufrc/boucher/aysegul.bumin/work/histogram103/head103.map  /ufrc/boucher/aysegul.bumin/work/output_Opera103
echo 'Done with Opera103'
head -522184 /ufrc/boucher/aysegul.bumin/work/histogram103/total103.fa > /ufrc/boucher/aysegul.bumin/work/histogram103/head103.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram103/head103.fa    --illumina-read1  /orange/boucher/shared/data/103fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/103rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram103/head103.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram103/head103.fa /ufrc/boucher/aysegul.bumin/work/histogram103/head103.map  /ufrc/boucher/aysegul.bumin/work/output_Opera103
echo 'Done with Opera103'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram70/total70.fa > /ufrc/boucher/aysegul.bumin/work/histogram70/head70.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram70/head70.fa	--illumina-read1  /orange/boucher/shared/data/70fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/70rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram70/head70.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram70/head70.fa /ufrc/boucher/aysegul.bumin/work/histogram70/head70.map  /ufrc/boucher/aysegul.bumin/work/output_Opera70
echo 'Done with Opera70'
head -420620 /ufrc/boucher/aysegul.bumin/work/histogram70/total70.fa > /ufrc/boucher/aysegul.bumin/work/histogram70/head70.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram70/head70.fa    --illumina-read1  /orange/boucher/shared/data/70fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/70rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram70/head70.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram70/head70.fa /ufrc/boucher/aysegul.bumin/work/histogram70/head70.map  /ufrc/boucher/aysegul.bumin/work/output_Opera70
echo 'Done with Opera70'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram73/total73.fa > /ufrc/boucher/aysegul.bumin/work/histogram73/head73.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram73/head73.fa	--illumina-read1  /orange/boucher/shared/data/73fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/73rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram73/head73.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram73/head73.fa /ufrc/boucher/aysegul.bumin/work/histogram73/head73.map  /ufrc/boucher/aysegul.bumin/work/output_Opera73
echo 'Done with Opera73'
head -441144 /ufrc/boucher/aysegul.bumin/work/histogram73/total73.fa > /ufrc/boucher/aysegul.bumin/work/histogram73/head73.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram73/head73.fa    --illumina-read1  /orange/boucher/shared/data/73fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/73rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram73/head73.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram73/head73.fa /ufrc/boucher/aysegul.bumin/work/histogram73/head73.map  /ufrc/boucher/aysegul.bumin/work/output_Opera73
echo 'Done with Opera73'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram118/total118.fa > /ufrc/boucher/aysegul.bumin/work/histogram118/head118.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram118/head118.fa	--illumina-read1  /orange/boucher/shared/data/118fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/118rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram118/head118.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram118/head118.fa /ufrc/boucher/aysegul.bumin/work/histogram118/head118.map  /ufrc/boucher/aysegul.bumin/work/output_Opera118
echo 'Done with Opera118'
head -249502 /ufrc/boucher/aysegul.bumin/work/histogram118/total118.fa > /ufrc/boucher/aysegul.bumin/work/histogram118/head118.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram118/head118.fa    --illumina-read1  /orange/boucher/shared/data/118fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/118rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram118/head118.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram118/head118.fa /ufrc/boucher/aysegul.bumin/work/histogram118/head118.map  /ufrc/boucher/aysegul.bumin/work/output_Opera118
echo 'Done with Opera118'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram122/total122.fa > /ufrc/boucher/aysegul.bumin/work/histogram122/head122.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram122/head122.fa	--illumina-read1  /orange/boucher/shared/data/122fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/122rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram122/head122.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram122/head122.fa /ufrc/boucher/aysegul.bumin/work/histogram122/head122.map  /ufrc/boucher/aysegul.bumin/work/output_Opera122
echo 'Done with Opera122'
head -191946 /ufrc/boucher/aysegul.bumin/work/histogram122/total122.fa > /ufrc/boucher/aysegul.bumin/work/histogram122/head122.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram122/head122.fa    --illumina-read1  /orange/boucher/shared/data/122fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/122rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram122/head122.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram122/head122.fa /ufrc/boucher/aysegul.bumin/work/histogram122/head122.map  /ufrc/boucher/aysegul.bumin/work/output_Opera122
echo 'Done with Opera122'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram2/total2.fa > /ufrc/boucher/aysegul.bumin/work/histogram2/head2.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram2/head2.fa	--illumina-read1  /orange/boucher/shared/data/2fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/2rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram2/head2.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram2/head2.fa /ufrc/boucher/aysegul.bumin/work/histogram2/head2.map  /ufrc/boucher/aysegul.bumin/work/output_Opera2
echo 'Done with Opera2'
head -561968 /ufrc/boucher/aysegul.bumin/work/histogram2/total2.fa > /ufrc/boucher/aysegul.bumin/work/histogram2/head2.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram2/head2.fa    --illumina-read1  /orange/boucher/shared/data/2fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/2rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram2/head2.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram2/head2.fa /ufrc/boucher/aysegul.bumin/work/histogram2/head2.map  /ufrc/boucher/aysegul.bumin/work/output_Opera2
echo 'Done with Opera2'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram61/total61.fa > /ufrc/boucher/aysegul.bumin/work/histogram61/head61.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram61/head61.fa	--illumina-read1  /orange/boucher/shared/data/61fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/61rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram61/head61.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram61/head61.fa /ufrc/boucher/aysegul.bumin/work/histogram61/head61.map  /ufrc/boucher/aysegul.bumin/work/output_Opera61
echo 'Done with Opera61'
head -333628 /ufrc/boucher/aysegul.bumin/work/histogram61/total61.fa > /ufrc/boucher/aysegul.bumin/work/histogram61/head61.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram61/head61.fa    --illumina-read1  /orange/boucher/shared/data/61fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/61rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram61/head61.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram61/head61.fa /ufrc/boucher/aysegul.bumin/work/histogram61/head61.map  /ufrc/boucher/aysegul.bumin/work/output_Opera61
echo 'Done with Opera61'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram74/total74.fa > /ufrc/boucher/aysegul.bumin/work/histogram74/head74.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram74/head74.fa	--illumina-read1  /orange/boucher/shared/data/74fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/74rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram74/head74.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram74/head74.fa /ufrc/boucher/aysegul.bumin/work/histogram74/head74.map  /ufrc/boucher/aysegul.bumin/work/output_Opera74
echo 'Done with Opera74'
head -427942 /ufrc/boucher/aysegul.bumin/work/histogram74/total74.fa > /ufrc/boucher/aysegul.bumin/work/histogram74/head74.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram74/head74.fa    --illumina-read1  /orange/boucher/shared/data/74fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/74rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram74/head74.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram74/head74.fa /ufrc/boucher/aysegul.bumin/work/histogram74/head74.map  /ufrc/boucher/aysegul.bumin/work/output_Opera74
echo 'Done with Opera74'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram77/total77.fa > /ufrc/boucher/aysegul.bumin/work/histogram77/head77.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram77/head77.fa	--illumina-read1  /orange/boucher/shared/data/77fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/77rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram77/head77.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram77/head77.fa /ufrc/boucher/aysegul.bumin/work/histogram77/head77.map  /ufrc/boucher/aysegul.bumin/work/output_Opera77
echo 'Done with Opera77'
head -328954 /ufrc/boucher/aysegul.bumin/work/histogram77/total77.fa > /ufrc/boucher/aysegul.bumin/work/histogram77/head77.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram77/head77.fa    --illumina-read1  /orange/boucher/shared/data/77fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/77rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram77/head77.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram77/head77.fa /ufrc/boucher/aysegul.bumin/work/histogram77/head77.map  /ufrc/boucher/aysegul.bumin/work/output_Opera77
echo 'Done with Opera77'
cd ..


head -1000 /ufrc/boucher/aysegul.bumin/work/histogram7/total7.fa > /ufrc/boucher/aysegul.bumin/work/histogram7/head7.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram7/head7.fa	--illumina-read1  /orange/boucher/shared/data/7fnoncow.fastq	--illumina-read2 /orange/boucher/shared/data/7rnoncow.fastq	--out /ufrc/boucher/aysegul.bumin/work/histogram7/head7.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram7/head7.fa /ufrc/boucher/aysegul.bumin/work/histogram7/head7.map  /ufrc/boucher/aysegul.bumin/work/output_Opera7
echo 'Done with Opera7'
head -351448 /ufrc/boucher/aysegul.bumin/work/histogram7/total7.fa > /ufrc/boucher/aysegul.bumin/work/histogram7/head7.fa 
preprocess_reads.pl --contig /ufrc/boucher/aysegul.bumin/work/histogram7/head7.fa    --illumina-read1  /orange/boucher/shared/data/7fnoncow.fastq     --illumina-read2 /orange/boucher/shared/data/7rnoncow.fastq      --out /ufrc/boucher/aysegul.bumin/work/histogram7/head7.map 
OPERA-LG /ufrc/boucher/aysegul.bumin/work/histogram7/head7.fa /ufrc/boucher/aysegul.bumin/work/histogram7/head7.map  /ufrc/boucher/aysegul.bumin/work/output_Opera7
echo 'Done with Opera7'
cd ..


date
