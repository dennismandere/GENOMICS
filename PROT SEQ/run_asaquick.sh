#!/bin/bash

#SBATCH --chdir=/home/b/bizhao/asaquick/GENN+ASAquick
#SBATCH --job-name=run_asaquick
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

wget -c https://rest.uniprot.org/uniprotkb/P01160.fasta
./asaquick P01160.fasta
