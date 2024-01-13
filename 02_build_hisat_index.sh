#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --chdir=../Work
#SBATCH --mail-type=ALL
#SBATCH --time=00:10:00
#SBATCH --mem=10000
#SBATCH --nodes=1
#SBATCH --mail-user=your_email@usf.edu
#SBATCH --job-name=hisat_index
#SBATCH --output=hisat_index.out



module purge
module load apps/hisat2/2.1.0


INPUT_REF_FASTA=../Reference_Data/PlasmoDB-41_Pfalciparum3D7_Genome.fasta
INDEX_FILES_BASE_NAME=PlasmoDB-41_Pfalciparum3D7_Genome



