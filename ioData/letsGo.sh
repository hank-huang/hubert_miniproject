#!/bin/bash
for fileName in /cis/home/hliu/Dataset_Project/Biocard/MRICloud_output/correct_stats_text/*; do
	awk 'NR==248,NR==523{print $3}' "$fileName"  > "$(basename $fileName)"
done
