import xarray as xr
local_storage = '/home/syedasamreen/'
netcdf_dir = local_storage
csv_flout = netcdf_dir  + '.csv'
netcdf_flname = '/home/syedasamreen/Downloads/ncn/ncum_imdaa_reanl_HR_APCP-sfc_2006010100-2006123123.nc'
ds = xr.open_dataset(netcdf_flname)
df = ds.to_dataframe()
df.to_csv(csv_flout)
#df.to_excel('ntcd2.xlsx',index = False,engine='xlsxwriter')
df.dropna()
print(df.head())

