# Working Directory

For this tutorial, we are working on these folder `/precipitation-index/exercise/` (applied to Mac/Linux machine) or `Z:/precipitation-index/exercise/` (applied to Windows machine) directory. We have some folder inside this directory:

1. `downloads`
	1. `imerg`
		1. `imerg_mmhr`
		2. `imerg_mmmonth`
		3. `imerg_originalfiles`
		
	2. `chirps`
		1. `netcdf`
		2. `geotiff`

	3. `terraclimate`
		1. `ppt`
		2. `pet`

	Place to put downloaded IMERG,CHIRPS and TerraClimate data

2. `fitting`

	Place to put fitting parameters output from the calculation

3. `input_nc`
	1. `imerg`
	2. `chirps`
	3. `terraclimate`

	Place to put netCDF data that will use as an input 

4. `input_tif`

	Place to put GeoTIFF file that will use to convert to single netCDF with time dimension enabled

5. `output_nc`
	1. `spi`
	2. `spei`

	Output folder for SPI calculation

6. `output_temp`

	Temporary for nc files from CDO arrange dimension process

7. `output_tif`

	Final output of SPI, generate by CDO and GDAL

8. `subset`

	Place to put shapefile for clipping area of interest

Feel free to use your own preferences for this setting/folder arrangements.