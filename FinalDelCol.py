import os
import pandas as pd
import glob
os.chdir("J:\EPPR\PopProgram\Projects\LUCA 2020 Prep\MAGIS L3 Updates\Assessor Data\Excel versions\Berkshire")
path = "J:\EPPR\PopProgram\Projects\LUCA 2020 Prep\MAGIS L3 Updates\Assessor Data\Excel versions\Berkshire"


files_in_dir = [f for f in os.listdir(path) if f.endswith('csv')]

file_names = []
data_frames = []

for filename in files_in_dir:
	df = pd.read_csv(filename)
    name = os.path.splitext(filename)[0]
    file_names.append(name)
    df.rename(columns={0: name}, inplace=False)
    data_frames.append(df)
	if 'CAMA_ID' in df.columns:
		df.drop('CAMA_ID', axis=1, inplace=True)
	
headers = ["PROP_ID","LOC_ID","BLDG_VAL","LAND_VAL","OTHER_VAL","TOTAL_VAL","FY","LOT_SIZE","LS_DATE","LS_PRICE","USE_CODE","SITE_ADDR","ADDR_NUM","FULL_STR","LOCATION","CITY","ZIP","OWNER1","OWN_ADDR","OWN_CITY","OWN_STATE","OWN_ZIP","OWN_CO","LS_BOOK","LS_PAGE","REG_ID","ZONING","YEAR_BUILT","BLD_AREA","UNITS","RES_AREA","STYLE","STORIES","NUM_ROOMS","LOT_UNITS","TOWN_ID"]	
combined = pd.concat(data_frames)
combined.to_csv("new3.csv", columns = headers, index=False)




