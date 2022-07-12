# Monthly TerraClimate in netCDF format

This section will explain on how to download TerraClimate's precipitation (ppt) and potential evapotranspiration (pet) monthly data in netCDF format and prepare it as input for SPI/SPEI calculation.

## 0. Working Directory

For this tutorial, we are working on these folder `/Users/gost/temp/terraclimate/spei/` (applied to Mac/Linux machine) or `Z:/temp/terraclimate/spei/` (applied to Windows machine) directory. I have some folder inside this directory:

1. `downloads`
	1. `ppt`
		1. `nc_original`
		2. `nc_merge`
		3. `nc_tiles`
		4. `nc_subset`
		5. `nc_llt` Place to put netCDF's ppt data that will use as an input
	2. `pet`
		1. `nc_original`
		2. `nc_merge`
		3. `nc_tiles`
		4. `nc_subset`
		5. `nc_llt` Place to put netCDF's pet data that will use as an input

	Place to put downloaded TerraCLimate data, and pre-process temporary files.

2. `output` 
	1. `nc_original` Output folder for SPEI calculation
		1. `gamma`
		2. `pearson`
	2. `nc_tll` Temporary for nc files from NCO arrange dimension process
	3. `nc_merge` Merging nc from separate tiles into single global layer (if you are following the global analysis procedures)
	4. `geotiff`
		1. `gamma` Final output of SPEI, generate by CDO and GDAL

Feel free to use your own preferences for this setting/folder arrangements.


## 1. Preparing input

SPEI requires monthly precipitation and potential evapotranspiration data, for better result, SPEI required minimum 30-years of data.

If you are prefer to use your own dataset also fine, you can still follow this guideline and adjust some steps and code related to filename, unit, format and structure.


### 1.1. Input requirement

The [climate-indices](https://pypi.org/project/climate-indices/) python package enables the user to calculate SPEI using any gridded netCDF dataset. However, there are certain requirements for input files that vary based on input type.

- Precipitation and potential evapotranspiration unit must be written as `millimeters`, `millimeter`, `mm`, `inches`, `inch` or `in`.

- Data dimension and order must be written as `lat`, `lon`, `time` (Windows machine required this order) or `time`, `lat`, `lon` (Works tested on Mac/Linux and Linux running on WSL). 

- If your study area are big, it's better to prepare all the data following this dimension order: `lat`, `lon`, `time` as all the data will force following this order during SPEI calculation by NCO module. Let say you only prepare the data as is (leaving the order to `lat`, `lon`, `time`), it also acceptable but it will required lot of memory to use re-ordering the dimension, and usually NCO couldn't handle all the process and failed.

*
## Download TerraClimate data

* There are 2 files contains link for downloading `ppt` ([https://github.com/bennyistanto/gost-climate/tree/main/book/howto/topic/precipitation-index/exercise/downloads/ppt/nc_original/data_ppt.sh](https://github.com/bennyistanto/gost-climate/tree/main/book/howto/topic/precipitation-index/exercise/downloads/ppt/nc_original/data_ppt.sh) and `pet` ([https://github.com/bennyistanto/gost-climate/tree/main/book/howto/topic/precipitation-index/exercise/downloads/pet/nc_original/data_pet.sh](https://github.com/bennyistanto/gost-climate/tree/main/book/howto/topic/precipitation-index/exercise/downloads/pet/nc_original/data_pet.sh)), the folder location are exactly the same with the working directory above. 

* Download both files and put it in the same location with your working directory.

* Navigate to `downloads/terraclimate/ppt/nc_original` and `downloads/terraclimate/pet/nc_original`folder in the working directory. Download using `wget` all TerraClimate in netCDF format from Jan 1958 to Dec 2020 (this is lot of data, `ppt` +- 7.7GB and `pet` +- 6.4GB, please make sure you have bandwidth and unlimited data package). Paste and Enter below script in your Terminal.

	If you are in `downloads/terraclimate/ppt/nc_original` then execute below command

	```bash
	sh data_ppt.sh
	```
	If you are in `downloads/terraclimate/pet/nc_original` then execute below command

	```bash
	sh data_pet.sh
	```

> **_NOTE:_**  
> This guideline provide example on how to use CDO and NCO to do some data extraction process,
you can choose which one is suits you.


## Clip data using a bounding box based on area of interest and merge netCDFs into single netCDF

* Clip your area of interest using bounding box. We will use Sao Tome and Principe (STP) as the example case.
	
	Example: (STP) bounding box with format `lon1`,`lon2`,`lat1`,`lat2` is `5.75`,`8.05`,`-0.35`,`2.15`

	Precipitation: Navigate your location to `/downloads/ppt/nc_original`

	CDO script:

	``` bash
	for fl in *.nc; cdo sellonlatbox,5.75,8.05,-0.35,2.15 $fl ../nc_subset/"stp_cli_"$fl; done
	```

	NCO script:

	``` bash
	for fl in *.nc; ncks -d latitude,-0.35,2.15 -d longitude,5.75,8.05 $fl -O ../nc_subset/"stp_cli_"$fl; done
	```

	Potential Evapotranspiration: Navigate your location to `/downloads/pet/nc_original`

	CDO script:

	``` bash
	for fl in *.nc; cdo sellonlatbox,5.75,8.05,-0.35,2.15 $fl ../nc_subset/"stp_cli_"$fl; done
	```

	NCO script:

	``` bash
	for fl in *.nc; ncks -d latitude,-0.35,2.15 -d longitude,5.75,8.05 $fl -O ../nc_subset/"stp_cli_"$fl; done
	```

* Merge all annual netcdf in a folder into single netcdf.

	Precipitation: make sure you are in `/downloads/ppt/nc_subset`

	CDO script:

	```bash
	cdo mergetime stp_*.nc ../nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc
	```

	NCO script:
	Before merging the data, NCO required all the data has `time`dimension, we will use `ncks` command to make `time` the record dimension/variable used for concatenating files.

	```bash
	for fl in *.nc; do ncks -O --mk_rec_dmn time $fl $fl; done
	```

	Then we are ready to concatenate it.

	```bash
	ncrcat -O -h stp_*.nc ../nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc
	```

	Potential Evapotranspiration: make sure you are in `/downloads/pet/nc_subset`

	CDO script:

	```bash
	cdo mergetime stp_*.nc ../nc_merge/stp_cli_terraclimate_pet_1958_2020.nc
	```

	NCO script:
	Before merging the data, NCO required all the data has `time`dimension, we will use `ncks` command to make `time` the record dimension/variable used for concatenating files.

	```bash
	for fl in *.nc; do ncks -O --mk_rec_dmn time $fl $fl; done
	```

	Then we are ready to concatenate it.

	```bash
	ncrcat -O -h stp_*.nc ../nc_merge/stp_cli_terraclimate_pet_1958_2020.nc
	```


## Check variable and attribute
As explain in Step 1.1. Input requirement above, we need to check the variable and attribute on above result to make sure all meet the requirements. 

* Navigate to `/downloads/ppt/nc_merge` folder in the working directory. Then execute below command.

	```bash
	ncdump -h stp_cli_terraclimate_ppt_1958_2020.nc
	```

	![ncdump ppt](./img/ncdump-ppt.png)

* Navigate to `/downloads/pet/nc_merge` folder in the working directory. Then execute below command.

	```bash
	ncdump -h stp_cli_terraclimate_pet_1958_2020.nc
	```

	![ncdump pet](./img/ncdump-pet.png)

* As you can see from above picture, all the requirement is completed: unit is in `mm`, order dimension for each variables is `lat`, `lon`, `time`, and `time` dimension is in `UNLIMITED`. Once this has completed, the dataset can be used as input to `climate-indices` package for computing SPEI. 
