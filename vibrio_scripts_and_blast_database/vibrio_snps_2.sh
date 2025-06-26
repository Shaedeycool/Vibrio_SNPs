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

mv ${workspace}/Vibrio_SNPs/vibrio_scripts_and_blast_database/Control-04 ${workspace}/${runname}/assemblies
mv ${workspace}/Vibrio_SNPs/vibrio_scripts_and_blast_database/Control-05 ${workspace}/${runname}/assemblies

cd ${workspace}/${runname}

mkdir vibrio_cholerae_snps

output_dir="vibrio_cholerae_snps"

for file in assemblies/*/*_assembly.fasta; do
## Extract sample name from the filename (e.g., YA00570981)
    sample=$(basename "$file" | cut -d'_' -f1)

## Define input and output file paths
    input_file="$file"
    output_file="${sample}_blast_output.xml"

## Run blastn
    blastn -query "$input_file" -db ${workspace}/Vibrio_SNPs/vibrio_scripts_and_blast_database/db/vcO1_markers/vcO1_markers -out $output_dir/"$output_file" -outfmt 5
done


for file in $output_dir/*_blast_output.xml; do
## Extract sample name from the filename (e.g., YA00570981)
    sample=$(basename "$file" | cut -d'_' -f1)

## Define input and output file paths
    input_file="$file"
    output_file="${sample}_blast_output.txt"

## Run your Python script
    python ${workspace}/Vibrio_SNPs/vibrio_scripts_and_blast_database/xml2snp_2.py -i "$input_file" -o $output_dir/"$output_file"
done

## Run Python script to make a complete table
python ${workspace}/Vibrio_SNPs/vibrio_scripts_and_blast_database/snp_merge.py

cp ${output_dir}/vch_snp_table.xlsx .
mv vch_snp_table.xlsx Vibrio_cholerae_assembly_results.xlsx
