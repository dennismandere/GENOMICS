#!/bin/bash

#SBATCH --chdir=/home/d/dennismandere
#SBATCH --job-name=saving_and_displaying
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

wget -c 'https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE77565&format=file&file=GSE77565%5FEvolloci%5Finteracting%5Fregion%5Fenhctrl%5FFBD1%5FFDR%2Ebed%2Egz' -O hiC_GSE77565.gz
gunzip hiC_GSE77565.gz
cat hiC_GSE77565|awk '$6 < 1e-10 {print $0}' > hiC_GSE77565.fdr.pick
:

