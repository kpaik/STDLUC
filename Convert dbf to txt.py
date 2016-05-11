import os
import arcpy
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def dbf2csv(dbfpath, csvpath):
    rows = arcpy.SearchCursor(dbfpath)
    csvFile = csv.writer(open(csvpath, 'wb')) 
    fieldnames = [f.name for f in arcpy.ListFields(dbfpath)]

    allRows = []
    for row in rows:
        rowlist = []
        for field in fieldnames:
            rowlist.append(row.getValue(field))
        allRows.append(rowlist)

    csvFile.writerow(fieldnames)
    for row in allRows:
        csvFile.writerow(row)
    row = None
    rows = None

dbf_dir = 'C:\Users\kpaik\Desktop\Batch'
csv_dir = 'C:\Users\kpaik\Desktop\Assessor Test'
for dbf_file in os.listdir(dbf_dir):
    
    fileName, fileExt = os.path.splitext(dbf_file)  #[0] or [1] for file
    if '.dbf' in fileExt:
       
        dbfpath = os.path.join(dbf_dir, fileName+fileExt)
        csvpath = os.path.join(csv_dir, fileName+'.csv')
        if os.path.exists(dbfpath):
            
            if not os.path.exists(csvpath):
                sys.stdout.write('Export nexrad {0} to {1}')
                dbf2csv(dbfpath, csvpath)
