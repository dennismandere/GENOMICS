#!/bin/bash

#SBATCH --chdir=/home/b/bizhao/mmseqs2
#SBATCH --job-name=run_mmseq
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

mmseqs createdb dataset/ref_protein_seq.fasta dataset/refDB
