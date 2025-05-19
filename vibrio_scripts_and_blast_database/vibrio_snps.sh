#!/bin/bash

if [ $# != 2 ];
 then
        echo "Usage: $0 <WorkDirectory> <RunFolder>"
        exit
fi

workspace=$1
runname=$2
reportsDir=$1"/Results-"$2
workdir=$1/"vibrio_cholerae_snps"

source ~/anaconda/anaconda3_2021-05-01/bin/activate # Edit
conda activate ~/anaconda/anaconda3_2021-05-01/envs/blast # Edit

mkdir vibrio_cholerae_snps

output_dir="vibrio_cholerae_snps"

for file in *_assembly.fasta; do
## Extract sample name from the filename (e.g., YA00570981)
    sample=$(basename "$file" | cut -d'_' -f1)

## Define input and output file paths
    input_file="$file"
    output_file="${sample}_blast_output.xml"

## Run blastn
    blastn -query "$input_file" -db ~/vibrio_scripts_and_blast_database/db/vcO1O139_markers -out $output_dir/"$output_file" -outfmt 5
done

conda activate ~/anaconda/anaconda3_2021-05-01/conda/envs/biopython # Edit


for file in $output_dir/*_blast_output.xml; do
## Extract sample name from the filename (e.g., YA00570981)
    sample=$(basename "$file" | cut -d'_' -f1)

## Define input and output file paths
    input_file="$file"
    output_file="${sample}_blast_output.txt"

## Run your Python script
    python ~/vibrio_scripts_and_blast_database/xml2snp_2.py -i "$input_file" -o $output_dir/"$output_file"
done

## Run Python script to make a complete table
python ~/vibrio_scripts_and_blast_database/snp_merge.py

## Run Python script to combine with original excel file
python ~/vibrio_scripts_and_blast_database/merge_VCH_xlsx.py


## Rename merged_output
#cp $workdir/merged_ouput.xlsx $workdir/${runname}-WGS-typing-report-snps.xlsx
