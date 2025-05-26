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

# Citations

The following conda environments were used:

BLAST: "Camacho, C., Coulouris, G., Avagyan, V., Ma, N., Papadopoulos, J., Bealer, K., and Madden, T.L. (2009). BLAST+: architecture and applications. BMC Bioinformatics, 10, 421."

BioPython: "Cock, P. J., Antao, T., Chang, J. T., Chapman, B. A., Cox, C. J., Dalke, A., … others. (2009). Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics, 25(11), 1422–1423."
