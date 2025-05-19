import pandas as pd
import glob

# Obtain matching excel file
file_input = glob.glob("Re*/*WGS*.xlsx")[0]

# Read csv file
csv_df = pd.read_csv("vibrio_cholerae_snps/vch_snp_table.txt", sep = '\t')

# Convert csv to excel
csv_df.to_excel("vibrio_cholerae_snps/vch_snp_table.xlsx", index=False)

# Read Excel files
df1 = pd.read_excel("vibrio_cholerae_snps/vch_snp_table.xlsx")
df2 = pd.read_excel(file_input)

# Rename a column
df1 = df1.rename(columns={'sampleID': 'SampleID'})

# Merge on a common column, keeping all columns (outer join)
merged_df = pd.merge(df2, df1, on='SampleID', how='outer')

# Replace NaN with 'undetected'
merged_df = merged_df.fillna("undetected")

# Step 6: Save the final merged DataFrame to a new Excel file
merged_df.to_excel("vibrio_cholerae_snps/merged_output.xlsx", index=False)
