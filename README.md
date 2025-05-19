# Vibrio_SNPs
Parse BLAST XML and extract single-nucleotide polymorphisms from high-identity, full-length alignments of Vibrio cholerae assemblies

# Input data
Assembled genomes are required as input.

The "vibrio_snps.sh" shell script looks for fasta assemblies within directory set as workspace

# Command to run vibrio_snps.sh
set workspace=<your folder>

set run_name=<directory that contains the "Vibrio cholerae assemblies" folder>

For example: if assembling multiple Illumina genomes 
run_name="250516_VH012345_Name_Vibrio_B1" 

workspace="/user_name/Vibrio/${run_name}"

```
bash ~/vibrio_scripts_and_blast_database/vibrio_snps.sh $workplace $run_name
```

# Conda environments needed. 
These paths would need to be edited in the "vibrio_snps.sh" shell script to reflect the paths of your conda environments.

~/anaconda/anaconda3_2021-05-01/bin/activate

~/anaconda/anaconda3_2021-05-01/envs/blast

~/anaconda/anaconda3_2021-05-01/conda/envs/biopython

