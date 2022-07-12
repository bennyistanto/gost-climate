# Input Data and Specification

SPI and SPEI requires monthly precipitation and potential evapotranspiration data, and there are many source providing global high-resolution gridded monthly precipitation data:

* [CHIRPS](https://chc.ucsb.edu/data/chirps)
* [IMERG](https://disc.gsfc.nasa.gov/datasets/GPM_3IMERGM_06/summary?keywords=IMERG)
* [FLDAS](https://disc.gsfc.nasa.gov/datasets/FLDAS_NOAH01_C_GL_M_001/summary?keywords=FLDAS)
* [TerraClimate](https://data.nkn.uidaho.edu/dataset/monthly-climate-and-climatic-water-balance-global-terrestrial-surfaces-1958-2015)
* [CRU](https://catalogue.ceda.ac.uk/uuid/89e1e34ec3554dc98594a5732622bce9)

and monthly potential evapotranspiration data:

* [TerraClimate](https://data.nkn.uidaho.edu/dataset/monthly-climate-and-climatic-water-balance-global-terrestrial-surfaces-1958-2015)

For better result, SPI and SPEI required minimum 30-years of data.

We provide 4 different approach to prepare precipitation data ready to use as SPI input. For learning matters, you may follow all the approach. Or you can choose which one is suit for you depend on the data source and format:

* [Monthly IMERG in netCDF](../monthly-imerg-netcdf/)
* [Monthly CHIRPS in GeoTIFF](../monthly-chirps-geotiff/)
* [Monthly CHIRPS in netCDF](../monthly-chirps-netcdf/)
* [Monthly TerraClimate in netCDF](../monthly-terraclimate-netcdf/)

If you are prefer to use your own dataset also fine, you can still follow this guideline and adjust some steps and code related to filename, unit, format and structure.

The [climate-indices](https://pypi.org/project/climate-indices/) python package enables the user to calculate SPI using any gridded netCDF dataset. However, there are certain specifications for input files that vary based on input type.

* Variable name on precipitation `--var_name_precip`, usually TerraClimate data use `ppt` as name while other precipitation data like CHIRPS using `precip` and IMERG using `precipitation` as a variable name. To make sure, check using command `ncdump -h file.nc` then adjust it in the script if needed.

* Variable name on potential evapotranspiration `--var_name_pet`, usually TerraClimate data use `pet` as name.

* Precipitation unit must be written as `millimeters`, `milimeter`, `mm`, `inches`, `inch` or `in`.

* Potential evapotranspiration unit must be written as `millimeters`, `milimeter`, `mm`, `inches`, `inch` or `in`.

* Data dimension and order must be written as `lat`, `lon`, `time` (Windows machine required this order) or `time`, `lat`, `lon` (Works tested on Mac/Linux and Linux running on WSL).