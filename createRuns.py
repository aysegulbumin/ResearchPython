import sys
import fileinput

'''
#!/bin/bash
#!/bin/bash
#SBATCH --job-name=trial
#SBATCH --mail-type=ALL
#SBATCH --qos=boucher-b
#SBATCH --mail-user=aysegul.bumin@ufl.edu
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=40gb
#SBATCH --time=90:00:00
#SBATCH --output=%j.out
date;hostname;pwd
'''
sample_number=str(sys.argv[1])
with open("run_this"+sample_number+".sh", "w") as text_file:
	my_string="#!/bin/bash\n"
	my_string=my_string+"#!/bin/bash\n"
	my_string=my_string+"#SBATCH --job-name=CreateHistogramArray\n"+"#SBATCH --mail-type=ALL\n"+"#SBATCH --qos=boucher-b\n"+"#SBATCH --mail-user=aysegul.bumin@ufl.edu\n"
	my_string=my_string+"#SBATCH --ntasks=1\n"+"#SBATCH --nodes=1\n"+"#SBATCH --cpus-per-task=1\n"+"#SBATCH --mem=40gb\n"+"#SBATCH --time=90:00:00\n"+"#SBATCH --output=histogram%j.out\n"+"date;hostname;pwd\n"
	text_file.write(my_string)
