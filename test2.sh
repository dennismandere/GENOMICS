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

module purgesource
source activate macs2
macs2 callpeak -t SRR576934.bam -c SRR576938.bam -g hs -n text_ex -B -q 0.01
