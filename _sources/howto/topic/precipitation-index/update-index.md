# Updating the index

**Example: Monthly CHIRPS in GeoTIFF format**

What if the new data is coming? Should we re-run again for the whole periods, 1981 to date (case on CHIRPS data)? That's not practical as it requires large storage and time processing if you do for bigger coverage (global or regional analysis).

So far, updating the SPI process is easy if we used CHIRPS in GeoTIFF format. Below are some reason:

* Downloading new CHIRPS data in [netCDF](https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/netcdf/) is painful, because we need to download whole package data (6.4 GB and start from Jan 1981 to date) eventhough we only need the latest month.

* CHIRPS data in [GeoTIFF](https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_monthly/tifs/) provides 1 month 1 GeoTIFF file, only take what you need!

* IMERG included data over the sea, and easiest way to clipped netCDF data is using bounding box. This approach will not have a problem if all of our area interest is in land.


## SPI

Updating SPI up to SPI-72, we should have data at least 6 years back (2015) from the latest (Jun 2022). In order to avoid computation for the whole periods (1981-2022), we will process data data only for year 2015 to 2022.

After that, we continue the process following [Monthly CHIRPS in GeoTIFF](../monthly-chirps-geotiff) to do conversion process to netCDF format from bunch of GeoTIFF file in a folder with time dimension enabled.

Then the next step demonstrates how distribution fitting parameters can be saved as NetCDF. This fittings NetCDF can then be used as pre-computed variables in subsequent SPI computations. Initial command computes both distribution fitting values and SPI for various month scales.

The distribution fitting variables are written to the file specified by the `--save_params` option.

The below command also computes SPI but instead of computing the distribution fitting values it loads the pre-computed fitting values from the NetCDF file specified by the `--load_params` option.

See below code:

``` bash
spi --periodicity monthly --scales 1 2 3 6 9 12 24 36 48 60 72 --calibration_start_year 1981 --calibration_end_year 2020 --netcdf_precip ./input_nc/java_cli_chirps_1months_2014_2021.nc --var_name_precip precip --output_file_base ./output_nc/java_CHIRPS --multiprocessing all --load_params ./fitting/java_CHIRPS_fitting.nc
```

![pi-update-01](../../../img/pi-update-spi.png)


## SPEI

How about updating the SPEI? Currently is not possible to update SPEI following above approach, as the SPEI code does not have capability to save distribution fitting variable.

Updating the SPEI will required to involved all the data from the start until end of mentioned calibration year, in other words, repeat the calculation from the beginning.