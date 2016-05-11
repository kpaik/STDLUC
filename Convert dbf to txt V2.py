import os
import csv
import sys
from simpledbf import Dbf5


os.chdir('C:\Users\kpaik\Desktop\Batch')
path = 'C:\Users\kpaik\Desktop\Assessor Test'
path2 = unicode(path,sys.getfilesystemencoding())

all_files = os.listdir(path2)
dbfs = [f for f in all_files if f.endswith('dbf')]


for dbf in dbfs:
    data = Dbf5(dbf)
    data.to_csv(os.path.join(path2, dbf[:-3] + 'csv'))

