# Monthly TerraClimate in netCDF format

This section will explain on how to download TerraClimate's precipitation (ppt) and potential evapotranspiration (pet) monthly data in netCDF format and prepare it as input for SPI/SPEI calculation.


## Download TerraClimate data

* There are 2 files contains link for downloading `ppt` ([Precipitation](https://github.com/bennyistanto/gost-climate/tree/main/book/howto/topic/precipitation-index/exercise/downloads/ppt/nc_original/data_ppt.sh) and `pet` ([Potential Evapotranspiration](https://github.com/bennyistanto/gost-climate/tree/main/book/howto/topic/precipitation-index/exercise/downloads/pet/nc_original/data_pet.sh)). 

* Download both files and put it in the same location with your working directory.

* Navigate to `downloads/terraclimate/ppt/nc_original` and `downloads/terraclimate/pet/nc_original`folder in the working directory. Download all TerraClimate in netCDF format from Jan 1958 to Dec 2020 using `wget` (this is lot of data, `ppt` +- 7.7GB and `pet` +- 6.4GB, please make sure you have bandwidth and unlimited data package). Paste and Enter below script in your Terminal.

	If you are in `downloads/terraclimate/ppt/nc_original` then execute below command

	```bash
	sh data_ppt.sh
	```
	If you are in `downloads/terraclimate/pet/nc_original` then execute below command

	```bash
	sh data_pet.sh
	```


## Extract data based on area of interest

Next step will be extract data using a bounding box based on area of interest and merge netCDFs into single netCDF

```{note}
Below guideline provide example on how to use CDO and NCO to do some data extraction process, you can choose which one is suits you.
```

* Clip your area of interest using bounding box. We will use Sao Tome and Principe (STP) as the example case.
	
	Example: STP bounding box with format `lon1`,`lon2`,`lat1`,`lat2` is `5.75`,`8.05`,`-0.35`,`2.15`

	Precipitation: Navigate your location to `/downloads/ppt/nc_original`

	| Software | Script |
	| --- | --- |
	| CDO | `for fl in *.nc; cdo sellonlatbox,5.75,8.05,-0.35,2.15 $fl ../nc_subset/"stp_cli_"$fl; done` |
	| NCO | `for fl in *.nc; ncks -d latitude,-0.35,2.15 -d longitude,5.75,8.05 $fl -O ../nc_subset/"stp_cli_"$fl; done` |

	Potential Evapotranspiration: Navigate your location to `/downloads/pet/nc_original`

	| Software | Script |
	| --- | --- |
	| CDO | `for fl in *.nc; cdo sellonlatbox,5.75,8.05,-0.35,2.15 $fl ../nc_subset/"stp_cli_"$fl; done` |
	| NCO | `for fl in *.nc; ncks -d latitude,-0.35,2.15 -d longitude,5.75,8.05 $fl -O ../nc_subset/"stp_cli_"$fl; done` |

* Merge all annual netcdf in a folder into single netcdf.

	Precipitation: make sure you are in `/downloads/ppt/nc_subset`

	| Software | Script |
	| --- | --- |
	| CDO | `cdo mergetime stp_*.nc ../nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc` |
	| NCO | Before merging the data, NCO required all the data has `time`dimension, we will use `ncks` command to make `time` the record dimension/variable used for concatenating files. Then use `ncrcat` to concatenate it. <ul><li>`for fl in *.nc; do ncks -O --mk_rec_dmn time $fl $fl; done`</li><li>`ncrcat -O -h stp_*.nc ../nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc`</li></ul> |

	Potential Evapotranspiration: make sure you are in `/downloads/pet/nc_subset`

	| Software | Script |
	| --- | --- |
	| CDO | `cdo mergetime stp_*.nc ../nc_merge/stp_cli_terraclimate_pet_1958_2020.nc` |
	| NCO | Before merging the data, NCO required all the data has `time`dimension, we will use `ncks` command to make `time` the record dimension/variable used for concatenating files. Then use `ncrcat` to concatenate it. <ul><li>`for fl in *.nc; do ncks -O --mk_rec_dmn time $fl $fl; done`</li><li>`ncrcat -O -h stp_*.nc ../nc_merge/stp_cli_terraclimate_pet_1958_2020.nc`</li></ul> |


## Check variable and attribute
As explain in above step, we need to check the variable and attribute on above result to make sure all meet the requirements. 

* Navigate to `/downloads/ppt/nc_merge` folder in the working directory. Then execute below command.

	```bash
	ncdump -h stp_cli_terraclimate_ppt_1958_2020.nc
	```

	![ncdump ppt](../../../img/pi-terraclimate-ppt.png)

* Navigate to `/downloads/pet/nc_merge` folder in the working directory. Then execute below command.

	```bash
	ncdump -h stp_cli_terraclimate_pet_1958_2020.nc
	```

	![ncdump pet](../../../img/pi-terraclimate-pet.png)

* As you can see from above picture, all the requirement is completed: unit is in `mm`, order dimension for each variables is `lat`, `lon`, `time`, and `time` dimension is in `UNLIMITED`. Once this has completed, the dataset can be used as input to `climate-indices` package for computing SPI/SPEI. 
