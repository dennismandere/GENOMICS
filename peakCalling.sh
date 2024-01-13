#!/bin/bash

#SBATCH --chdir=/home/d/dennismandere/ChipSeqAnalysis/
#SBATCH --job-name=PeakCalling
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10000
#SBATCH -t 00:10:00
#SBATCH -o run.out
#SBATCH -e run.err
#SBATCH --mail-user=dennismandere@usf.edu
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

source ~/.bash_profile
module purge
#module add apps/miniconda/3.6.1
conda activate macs2
macs2 callpeak -t SRR576934.bam -c SRR576938.bam -n MACSpeaks -q 0.05 --gsize 4639675 --keep-dup 1 --nomodel --extsize 400
