#!/bin/bash

#SBATCH --chdir=/home/d/dennismandere/ChipSeqAnalysis
#SBATCH --job-name=MotifCalling
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10000
#SBATCH -t 00:30:00
#SBATCH -o run.out
#SBATCH -e run.err
#SBATCH --mail-user=dennismandere@usf.edu
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

source ~/.bash_profile
module purge
#module add apps/miniconda/3.6.1 #this line should be removed only in Charley's environment

conda activate macs2
findMotifsGenome.pl MACSpeaks_peaks.narrowPeak refGenome/GCF_000005845.2_ASM584v2_genomic.fna motif_result/ -size 100
