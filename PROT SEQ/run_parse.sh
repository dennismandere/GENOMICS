#!/bin/bash

#SBATCH --chdir=/home/b/bizhao/result
#SBATCH --job-name=run_parse
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10000
#SBATCH -t 00:10:00
#SBATCH -o run.out
#SBATCH -e run.err
#SBATCH --mail-user=bizhao@mail.usf.edu
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

source ~/.bash_profile
module purge
module add apps/miniconda/3.6.1

conda activate prot_study
python format_results.py P01160.fasta asaq.pred P01160.pssm P01160.txt
