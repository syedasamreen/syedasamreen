import netCDF4
from netCDF4 import Dataset
import pandas as pd
import xlsxwriter

jan = Dataset("/home/syedasamreen/Downloads/ncum.nc")
print(jan.variables.keys())

lon = jan.variables['longitude']
lat = jan.variables['latitude']
time = jan.variables['time']
apcp = jan.variables['APCP_sfc']

for d in jan.dimensions.items():
    print(d)

lon_array = lon[:]
lat_array = lat[:]
time_array = time[:]
apcp_array = apcp[:]

new_list = [['time', 'longitude','latitude','apcp_sfc'],['time', 'longitude','latitude','apcp_sfc'], [lon_array,lat_array,time_array,apcp_array]]

with xlsxwriter.Workbook('ntcd.xlsx') as workbook:  #generate file test.xlsx
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(new_list):
        worksheet.write_row(row_num, 1, data)

#
# print(lon_array)
# print(lat_array)