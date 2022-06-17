import xarray as xr
import pandas as pd
netcdf_flname = '/home/syedasamreen/Downloads/Wind Direction-2015.xlsx'
ds = pd.read_excel(netcdf_flname)
print(ds)