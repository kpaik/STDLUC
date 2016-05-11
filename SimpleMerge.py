import pandas as pd
import glob
import os


os.chdir("J:\EPPR\PopProgram\Projects\LUCA 2020 Prep\MAGIS L3 Updates\Land Use Codes\Excel versions\Barnstable")
data = glob.glob("*.csv")
df_list = []


for filename in sorted(data):
    df_list.append(pd.read_csv(filename))
	full_df = pd.concat(df_list)

full_df.to_csv('output.csv')