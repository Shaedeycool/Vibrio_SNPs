import pandas as pd
import glob


# Define path to your Excel files
files = glob.glob("vibrio_cholerae_snps/*_data.csv")

# Read all Excel files into a list of DataFrames
df_1 = [pd.read_csv(file) for file in files]

# Merge DataFrames based on column names (outer join to keep all columns)
merged_df = pd.concat(df_1, axis=0, ignore_index=True, sort=False)

# Create dictionary to rename value names of grouped_by_sample
#rename_map = {'dbj|AB012956.1|' : 'wbfo139',  'gb|KP187623.1|' : 'tcpA_ElTor',  'gb|M33514.1|' : 'tcpA_Classic',  'gb|KC152957.1|' : 'wbeO1_ElTor',  'gb|KF498634.1|' : 'toxR',  'gb|AF463401.1|' : 'ctxA',  'gb|JF284685.1|' :  'wbeT_ElTor'}
rename_map = {'dbj|AB012956.1|' : 'wbfo139',  'gb|KP187623.1|' : 'tcpA_ElTor',  'gb|M33514.1|' : 'tcpA_Classic',  'gb|KC152957.1|' : 'wbeO1_ElTor',  'gb|KF498634.1|' : 'toxR',  'gb|AF463401.1|' : 'ctxA'}

# Define DataFrame column names
#df_columns = ['sampleID', 'dbj|AB012956.1|',  'gb|KP187623.1|',  'gb|M33514.1|',  'gb|KC152957.1|',  'gb|KF498634.1|',  'gb|AF463401.1|',  'gb|JF284685.1|']
df_columns = ['sampleID', 'dbj|AB012956.1|',  'gb|KP187623.1|',  'gb|M33514.1|',  'gb|KC152957.1|',  'gb|KF498634.1|',  'gb|AF463401.1|']

# Create empty DataFrame with defined column names
df_2 = pd.DataFrame(columns=df_columns)

# Find common columns between dataframes to merge on
common_columns = df_2.columns.intersection(merged_df.columns)

# Merge on all of those shared columns
final_df = pd.merge(merged_df, df_2, on=list(common_columns), how='outer')

# Replace NaN with undetected
final_df = final_df.fillna("undetected")

# Rename columns using dictionary
df_3 = final_df.rename(columns=rename_map)

# Save to a complete table
df_3.to_csv("vibrio_cholerae_snps/vch_snp_table.txt", sep = '\t', index = None)

