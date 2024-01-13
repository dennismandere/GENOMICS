cut -f '2,3,4,5,9,11' -d ',' proteins_167_161521.csv |sed 's/,/\t/g'|sed 's/"//g'|grep '^NC' > proteins_167_161521.tsv^C

closestBed -a MACSpeaks_peaks.narrowpeak -b refGenome/proteins_167_161521.tsv -d_> MACSpeaks_peaks.narrowPeak.disToGene


closestBed -a MACSpeaks_summits.bed -b refGenome/proteins_167_161521.tsv^C -d > MACSpeaks_summits.disToGene
