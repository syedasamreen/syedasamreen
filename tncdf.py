import netCDF4
import pandas as pd
import xlsxwriter

precip_nc_file = '/home/syedasamreen/Downloads/ncum.nc'
nc = netCDF4.Dataset(precip_nc_file, mode='r')

nc.variables.keys()

lat = nc.variables['latitude'][:]
lon = nc.variables['longitude'][:]
apcp = nc.variables['APCP_sfc']
time_var = nc.variables['time']
dtime = netCDF4.num2date(time_var[:],time_var.units)
temp = np.zeros(52 * 57, dtype=np.float32)
temp[:ppt_arr.size] = ppt_arr
prec[:] = temp
print(lat.shape)
print(lon.shape)
print(apcp.shape)
print(time_var.shape)
# a pandas.Series designed for time series of a 2D lat,lon grid
precip_ts = pd.Series(apcp, index=dtime)

precip_ts.to_excel('precip.xlsx',index=dtime)
# print(precip_ts)

new_list = precip_ts
with xlsxwriter.Workbook('ntcd.xlsx') as workbook:  #generate file test.xlsx
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(new_list):
        worksheet.write_row(row_num, 1, data)