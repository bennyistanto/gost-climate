#!/usr/bin/env python
# coding: utf-8

# -------------------------------------------------------------------------------------------------------------
# ## CHIRPS GeoTIFF to single netCDF
# 
# Convert CHIRPS GeoTIFF in a folder to single NetCDF file with time dimension enabled that is CF-Compliant
# http://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html
#  
# Based on Rich Signell's answer on StackExchange: https://gis.stackexchange.com/a/70487
# This script was tested using CHIRPS monthly data. Adjustment is needed if using other timesteps data for CHIRPS
# NCO (http://nco.sourceforge.net) must be installed before using this script
#  
# Modified by
# Benny Istanto, GOST/DECAT, bistanto@worldbank.org
# 
# -------------------------------------------------------------------------------------------------------------
# 

# In[1]:


#!/usr/bin/env python
import numpy as np
import datetime as dt
import os
from osgeo import gdal
import netCDF4
import re


# In[2]:


ds = gdal.Open('/Users/benny/Documents/GitHub/gost-climate/book/howto/topic/precipitation-index/exercise/input_tif/java_chirps-v2.0.1981.01.tif') # Data location


# In[3]:


a = ds.ReadAsArray()
nlat,nlon = np.shape(a)

b = ds.GetGeoTransform() #bbox, interval
lon = np.arange(nlon)*b[1]+b[0]
lat = np.arange(nlat)*b[5]+b[3]

basedate = dt.datetime(1980,1,1,0,0,0)


# In[4]:


# Create NetCDF file
nco = netCDF4.Dataset('java_cli_chirps_1months_1981_2020.nc','w',clobber=True) # Output name


# In[5]:


# Create dimensions, variables and attributes:
nco.createDimension('lon',nlon)
nco.createDimension('lat',nlat)
nco.createDimension('time',None)

timeo = nco.createVariable('time','f4',('time'))
timeo.units = 'days since 1980-1-1 00:00:00'
timeo.standard_name = 'time'
timeo.calendar = 'gregorian'
timeo.axis = 'T'

lono = nco.createVariable('lon','f4',('lon'))
lono.units = 'degrees_east'
lono.standard_name = 'longitude'
lono.long_name = 'longitude'
lono.axis = 'X'

lato = nco.createVariable('lat','f4',('lat'))
lato.units = 'degrees_north'
lato.standard_name = 'latitude'
lato.long_name = 'latitude'
lato.axis = 'Y'


# In[6]:


# Create container variable for CRS: lon/lat WGS84 datum
crso = nco.createVariable('crs','i4')
crso.long_name = 'Lon/Lat Coords in WGS84'
crso.grid_mapping_name='latitude_longitude'
crso.longitude_of_prime_meridian = 0.0
crso.semi_major_axis = 6378137.0
crso.inverse_flattening = 298.257223563


# In[7]:


# Create float variable for precipitation data, with chunking
pcpo = nco.createVariable('precip', 'f4',  ('time', 'lat', 'lon'),zlib=True,fill_value=-9999.)
pcpo.units = 'mm'
pcpo.standard_name = 'convective precipitation rate'
pcpo.long_name = 'Climate Hazards group InfraRed Precipitation with Stations'
pcpo.time_step = 'month'
pcpo.missing_value = -9999.
pcpo.geospatial_lat_min = -8.8
pcpo.geospatial_lat_max = -5.05
pcpo.geospatial_lon_min = 105.05
pcpo.geospatial_lon_max = 116.25
pcpo.grid_mapping = 'crs'
pcpo.set_auto_maskandscale(False)


# In[8]:


# Additional attributes
nco.Conventions='CF-1.6'
nco.title = "CHIRPS v2.0"
nco.history = "created by Climate Hazards Group. University of California at Santa Barbara"
nco.version = "Version 2.0"
nco.comments = "time variable denotes the first day of the given month."
nco.website = "https://www.chc.ucsb.edu/data/chirps"
nco.date_created = "2022-06-01"
nco.creator_name = "Benny Istanto"
nco.creator_email = "bistanto@worldbank.org"
nco.institution = "The World Bank"
nco.note = "The data is developed to support regular updating procedure for SPI analysis. This activities will support The World Bank to assess extreme dry and wet periods as part of The World Bank's Climate Analytics"


# In[9]:


# Write lon,lat
lono[:]=lon
lato[:]=lat

pat = re.compile('java_chirps-v2.0.[0-9]{4}\.[0-9]{2}')
itime=0


# In[10]:


# Step through data, writing time and data to NetCDF
for root, dirs, files in os.walk('/Users/benny/Documents/GitHub/gost-climate/book/howto/topic/precipitation-index/exercise/input_tif/'):
    dirs.sort()
    files.sort()
    for f in files:
        if re.match(pat,f):
            # read the time values by parsing the filename
            year=int(f[17:21])
            mon=int(f[22:24])
            date=dt.datetime(year,mon,1,0,0,0)
            print(date)
            dtime=(date-basedate).total_seconds()/86400.
            timeo[itime]=dtime
           # precipitation
            pcp_path = os.path.join(root,f)
            print(pcp_path)
            pcp=gdal.Open(pcp_path)
            a=pcp.ReadAsArray()  #data
            pcpo[itime,:,:]=a
            itime=itime+1

nco.close()


# In[ ]:




