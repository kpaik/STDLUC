import os
import pandas as pd
import glob
os.chdir("C:\Users\kpaik\Desktop\Play Files\Suffolk")
path = "C:\Users\kpaik\Desktop\Play Files\Suffolk"

file_names = []
data_frames = []
for filename in os.listdir(path):
    name = os.path.splitext(filename)[0]
    file_names.append(name)
    df = pd.read_csv(filename)
    df.rename(columns={0: name}, inplace=True)
    data_frames.append(df)
	
header = ["OID","PROP_ID","LOC_ID","BLDG_VAL","LAND_VAL","OTHER_VAL","TOTAL_VAL","FY","LOT_SIZE","LS_DATE","LS_PRICE","USE_CODE","SITE_ADDR","ADDR_NUM","FULL_STR","LOCATION","CITY","ZIP","OWNER1","OWN_ADDR","OWN_CITY","OWN_STATE","OWN_ZIP","OWN_CO","LS_BOOK","LS_PAGE","REG_ID","ZONING","YEAR_BUILT","BLD_AREA","UNITS","RES_AREA","STYLE","STORIES","NUM_ROOMS","LOT_UNITS","TOWN_ID"]	
combined = pd.concat(data_frames)
combined.to_csv("new.csv", columns = header, index=False)




