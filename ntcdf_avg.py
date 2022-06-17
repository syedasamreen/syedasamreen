import pandas as pd
# df = pd.read_csv('/home/syedasamreen/Downloads/ncum_imdaa_reanl_HR_PRES-sfc_2006010100-2006123123.nc.csv',parse_dates=True,index_col="time")
# df1=df.groupby(['latitude','longitude']).resample('D').mean()
# print(df1)
import os
import glob
os.chdir("/home/syedasamreen/2001_files")
extension = 'csv'
all_file=[i for i in glob.glob('*.{}'.format(extension))]
con_csv = pd.concat([pd.read_csv(f) for f in all_file])
com_csv=con_csv.to_csv("combined_csv.csv", index = False,encoding = 'UTF-8')
df = pd.read_csv("/home/syedasamreen/2001_files/combined_csv.csv",parse_dates=True,index_col="time")
na_fill = df.fillna(0)
df1=na_fill.groupby(['latitude','longitude']).resample('D').mean()
print(df1)
