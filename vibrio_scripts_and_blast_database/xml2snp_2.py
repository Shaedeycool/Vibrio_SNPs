import argparse
from Bio.Blast import NCBIXML
import pandas as pd
import os

# Argument parser
parser = argparse.ArgumentParser(description="Parse BLAST XML and extract SNPs from high-identity, full-length alignments.")
parser.add_argument("-i", "--input", required=True, help="Input file")
parser.add_argument("-o", "--output", required=True, help="Output file")
args = parser.parse_args()

# Get basename without extension and first part befor underscore
basename = os.path.splitext(os.path.basename(args.input))[0]

sample_id = basename.split('_')[0]

#blast_file = "250422_YA00570981_blast.xml"
snp_results = []
grouped_by_sample = {}

with open(args.input) as result_handle:
    blast_records = NCBIXML.parse(result_handle)

    for record in blast_records:
        for alignment in record.alignments:
            for hsp in alignment.hsps:
                identity_pct = (hsp.identities / hsp.align_length) * 100
                match_length_pct = (hsp.align_length / alignment.length) * 100

                # Only consider alignments with >95% identity and near full gene length
                if identity_pct >= 85 and match_length_pct >= 85:
                    query_seq = hsp.query
                    subject_seq = hsp.sbjct
                    query_start = hsp.query_start

                    for i in range(len(query_seq)):
                        q_base = query_seq[i]
                        s_base = subject_seq[i]

                        if q_base != s_base and q_base != '-' and s_base != '-':
                            snp_results.append({
                                'target': alignment.hit_id,
                                'ref': s_base,
                                'position': query_start + i,
                                'alt': q_base
                            })



# Print or save to a dictionary
for snp in snp_results:
    sample = sample_id
    key = snp['target']
    snp_val = f"{snp['ref']}{snp['position']}{snp['alt']}"


    if sample not in grouped_by_sample:
        grouped_by_sample[sample] = {}
    if key not in grouped_by_sample[sample]:
        grouped_by_sample[sample][key] = []
    grouped_by_sample[sample][key].append(snp_val)

####################################################
dfs = []

# Iterate over each sample and its SNP data
for sample, snp_dict in grouped_by_sample.items():
    # Create a DataFrame for each sample
    # Create a dictionary where each target (gene) will be a column
    sample_data = {'sampleID': [sample]}  # Start with the sampleID column

    # Add each target's SNP list to the sample_data dictionary
    for key, snp_list in snp_dict.items():
        sample_data[key] = [", ".join(snp_list)]  # Join SNPs into a comma-separated string

    # Create a DataFrame from this dictionary
    df_sample = pd.DataFrame(sample_data)

    # Add this sample DataFrame to the list of DataFrames
    dfs.append(df_sample)

# Now, save each DataFrame to a separate CSV file
for sample, df in zip(grouped_by_sample.keys(), dfs):
    filename = f"vibrio_cholerae_snps/{sample}_data.csv"
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")

# Optionally, print the DataFrame for a quick look at the results
for df in dfs:
    print(df)

################################################################

