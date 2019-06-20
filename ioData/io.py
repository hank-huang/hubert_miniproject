import pandas as pd

biocard_df = pd.read_excel('/cis/home/hliu/Dataset_Project/Biocard/Demographic_information/BIOCARD_Entorhinal_Cortex_MRI_Measures_08022013_including_thickness.xls', skiprows = 9)

biocard_df.columns = ['SubjectID', 'NIHID', 'StudyID', 'Scan', 'Age@Scan', 'ScanDate', 'Intracranial_Volume', 'LEC_Volume', 'LEC_Thickness', 'REC_Volume', 'REC_Thickness', 'Diagnosis@LastScan', 'ConsensusDiagnosis']

ncf = biocard_df['ConsensusDiagnosis'] == 'ncf'
nci = biocard_df['ConsensusDiagnosis'] == 'nci'
normal = biocard_df['ConsensusDiagnosis'] == 'normal'

df = biocard_df

df.loc[normal | ncf | nci , 'ConsensusDiagnosis'] = 0
df.loc[df.ConsensusDiagnosis != 0 , 'ConsensusDiagnosis'] = 1

df.sort_values(by = ['NIHID'])

import glob, os
os.chdir('/cis/home/hhuang/Hubert/loc')

df_transposeMe = pd.DataFrame()

for f in glob.glob('*.txt'):
	mriCloud = pd.read_table(f, header=None, squeeze=True)
	df_transposeMe[f] = mriCloud

concat_df = df_transposeMe.transpose().sort_index()

concat_df.reset_index(drop=True, inplace=True)
df.reset_index(drop=True, inplace=True)

df_final = pd.concat([df, df_concat], axis = 1)

df_final.drop(['SubjectID', 'NIHID', 'Scan'], axis = 1, inplace=True)

df_final = pd.concat([df_final, pd.get_dummies(df_final['Diagnosis@LastScan'])], axis = 1)

df1_final.drop('Diagnosis@LastScan', inplace=True, axis = 1)
