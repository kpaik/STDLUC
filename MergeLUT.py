import os
import pandas as pd
import glob
os.chdir("J:\EPPR\PopProgram\Projects\LUCA 2020 Prep\MAGIS L3 Updates\Land Use Codes\Excel versions\Barnstable")
path = "J:\EPPR\PopProgram\Projects\LUCA 2020 Prep\MAGIS L3 Updates\Land Use Codes\Excel versions\Barnstable"



files_in_dir = [f for f in os.listdir(path) if f.endswith('csv')]

file_names = []
data_frames = []

for filename in files_in_dir:
	df = pd.read_csv(filename, converters={'USE_CODE': lambda x: str(x), 'MCD': lambda x: str(x)})
    name = os.path.splitext(filename)[0]
    file_names.append(name)
    df.rename(columns={0: name}, inplace=False)
    data_frames.append(df)
	
headers = ["MCD_NAME","MCD","USE_CODE","USE_DESC","STD_LUC","CATEGORY","RESID_INC","RECHECK"]	
combined = pd.concat(data_frames)
combined.to_csv("Combined.csv", columns = headers, index=False)
