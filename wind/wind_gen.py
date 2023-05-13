"""
Requires: {@code xarray}, {@code dask}, {@code netCDF4}, and {@code bottleneck}
<p>
Code source: https://gist.github.com/copernicusmarinegist/b57417225d0d4ea47c5d6200f9d8cac3
Data source: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00842
Data download: https://www.ncei.noaa.gov/thredds/ncss/uv/monthly/2011/uv201109.nc/dataset.html

@author Jonathan Uhler
"""


import xarray
import os


# https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00842
nc_file_dir = os.getcwd()
nc_file_name = "2011_uv201109.nc"
nc_file_path = nc_file_dir + "/" + nc_file_name

csv_file_dir = os.getcwd()
csv_file_name = "uv_wind.csv"
csv_file_path = csv_file_dir + "/" + csv_file_name

dataset = xarray.open_dataset(nc_file_path)
dataframe = dataset.to_dataframe()

dataframe.to_csv(csv_file_path)
