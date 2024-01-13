#!/bin/bash

#SBATCH --chdir=/home/d/dennismandere/protein_analysis/MMseqs
#SBATCH --job-name=run_mmseqs
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10000
#SBATCH -t 00:10:00
#SBATCH -o run.out
#SBATCH -e run.err
#SBATCH --mail-user=dennismandere@mail.usf.edu
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL


wget -c https://rest.uniprot.org/uniprotkb/P01160.fasta
mkdir P01160
mmseqs createdb P01160.fasta P01160/P01160
mkdir resultDB
mmseqs search P01160/P01160 dataset/refDB resultDB/resultDb tmp -a
mkdir profileDB
mmseqs result2profile P01160/P01160 dataset/refDB resultDB/resultDb profileDB/profileDb
mmseqs profile2pssm profileDB/profileDb P01160.pssm
