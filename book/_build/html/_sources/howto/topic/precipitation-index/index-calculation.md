# Index calculation

Before starting the calculatio, please make sure below points:

* [x] You are still inside `climate_indices` environment to start working on SPI/SPEI calculation.  
* [x] Variable name on precipitation `--var_name_precip`, usually TerraClimate data use `ppt` as name while other precipitation data like CHIRPS using `precip` and IMERG using `precipitation` as a variable name. To make sure, check using command `ncdump -h file.nc` then adjust it (along with folder location, input and output filenames) in SPI/SPEI script if needed.  
* [x] Variable name on potential evapotranspiration `--var_name_pet`, usually TerraClimate data use `pet` as name.  
* [x] Precipitation and potential evapotranspiration unit must be written as `millimeters`, `milimeter`, `mm`, `inches`, `inch` or `in`.  
* [x] Data dimension and order must be written as `lat`, `lon`, `time` (Windows machine required this order) or `time`, `lat`, `lon` (Works tested on Mac/Linux and Linux running on WSL).  

Let's start the calculation!  


## SPI 

* In order to pre-compute fitting parameters for later use as inputs to subsequent SPI calculations, I can save both gamma and Pearson distribution fitting parameters to NetCDF, and later use this file as input for SPI calculations over the same calibration period.  

* In your Terminal, run the following code then parallelization will occur utilizing all CPUs.  

	``` bash
	spi --periodicity monthly --scales 1 2 3 6 9 12 24 36 48 60 72 --calibration_start_year 2000 --calibration_end_year 2020 --netcdf_precip /input_nc/java_cli_imerg_1months_2000_2020.nc --var_name_precip precipitation --output_file_base /output_nc/spi_imerg/java_IMERG --multiprocessing all --save_params /fitting/java_IMERG_fitting.nc --overwrite
	```

* If you does not have plan to save the fitting parameters, you can run the following code.  

	``` bash
	process_climate_indices --index spi --periodicity monthly --scales 1 2 3 6 9 12 24 36 48 60 72 --calibration_start_year 2000 --calibration_end_year 2020 --netcdf_precip /input_nc/java_cli_imerg_1months_2000_2020.nc --var_name_precip precipitation --output_file_base /output_nc/spi_imerg/java_IMERG --multiprocessing all
	```

* Above code is example for calculating SPI 1 to 72-months. It's ok if you think you only need some of them. Example: you are interested to calculate SPI 1 - 3-months, then adjust above code into `--scales 1 2 3` .  

* The above command will compute SPI (both gamma and Pearson Type III distributions) from an input precipitation dataset (in this case, IMERG precipitation dataset). The input dataset is monthly rainfall accumulation data and the calibration period used will be Jun-2000 through Dec-2020. The index will be computed at `1`,`2`,`3`,`6`,`9`,`12`,`24`,`36`,`48`,`60` and `72-month` timescales. The output files will be `<out_dir>/java_IMERG_spi_gamma_xx.nc`, and `<out_dir>/java_IMERG_spi_pearson_xx.nc`.  

	The output files will be:

	Gamma

	1. 1-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_1_month.nc`</br>
	2. 2-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_2_month.nc`</br>
	3. 3-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_3_month.nc`</br>
	4. 6-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_6_month.nc`</br>
	5. 9-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_9_month.nc`</br>
	6. 12-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_12_month.nc`</br>
	7. 24-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_24_month.nc`</br>
	8. 36-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_36_month.nc`</br>
	9. 48-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_48_month.nc`</br>
	10. 60-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_60_month.nc`</br>
	11. 72-month: `/output_nc/spi_imerg/java_IMERG_spi_gamma_72_month.nc`</br>

	Pearson

	1. 1-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_1_month.nc`</br>
	2. 2-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_2_month.nc`</br>
	3. 3-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_3_month.nc`</br>
	4. 6-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_6_month.nc`</br>
	5. 9-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_9_month.nc`</br>
	6. 12-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_12_month.nc`</br>
	7. 24-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_24_month.nc`</br>
	8. 36-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_36_month.nc`</br>
	9. 48-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_48_month.nc`</br>
	10. 60-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_60_month.nc`</br>
	11. 72-month: `/output_nc/spi_imerg/java_IMERG_spi_pearson_72_month.nc`</br>


## SPEI

* In your Terminal, run the following code then parallelization will occur utilizing all CPUs.  

	``` bash
	process_climate_indices --index spei --periodicity monthly --netcdf_precip /downloads/terraclimate/ppt/nc_merge/stp_cli_terraclimate_ppt_1958_2020.nc --var_name_precip ppt --netcdf_pet /downloads/terraclimate/pet/nc_merge/stp_cli_terraclimate_pet_1958_2020.nc --var_name_pet pet --output_file_base /Users/gost/temp/terraclimate/spei/output/nc_original/spt_cli_spei --scales 1 2 3 6 9 12 18 24 36 48 60 72 --calibration_start_year 1958 --calibration_end_year 2020 --multiprocessing all
	```

* Above code is example for calculating SPEI 1 to 72-months. It's ok if you think you only need some of them. Example: you are interested to calculate SPEI 1 - 3-months or SPEI 12-months, then adjust above code into `--scales 1 2 3` or `--scales 12`.  

* The above command will compute SPEI (both gamma and Pearson Type III distributions) from monthly precipitation dataset and potential evapotranspiration, and the calibration period used will be Jan-1958 through Dec-2020. The index will be computed at `1`,`2`,`3`,`6`,`9`,`12`,`18`,`24`,`36`,`48`,`60` and `72-month` timescales. The output files will be <`out_dir>/stp_cli_spei_gamma_xx.nc`, and `<out_dir>/stp_cli_spei_pearson_xx.nc`.  

	The output files will be:

	Gamma

	1. 1-month: `/output/nc_original/stp_cli_spei_gamma_01.nc`</br>
	2. 2-month: `/output/nc_original/stp_cli_spei_gamma_02.nc`</br>
	3. 3-month: `/output/nc_original/stp_cli_spei_gamma_03.nc`</br>
	4. 6-month: `/output/nc_original/stp_cli_spei_gamma_06.nc`</br>
	5. 9-month: `/output/nc_original/stp_cli_spei_gamma_09.nc`</br>
	6. 12-month: `/output/nc_original/stp_cli_spei_gamma_12.nc`</br>
	7. 18-month: `/output/nc_original/stp_cli_spei_gamma_18.nc`</br>
	8. 24-month: `/output/nc_original/stp_cli_spei_gamma_24.nc`</br>
	9. 36-month: `/output/nc_original/stp_cli_spei_gamma_36.nc`</br>
	10. 48-month: `/output/nc_original/stp_cli_spei_gamma_48.nc`</br>
	11. 60-month: `/output/nc_original/stp_cli_spei_gamma_60.nc`</br>
	12. 72-month: `/output/nc_original/stp_cli_spei_gamma_72.nc`</br>

	Pearson

	1. 1-month: `/output/nc_original/stp_cli_spei_pearson_01.nc`</br>
	2. 2-month: `/output/nc_original/stp_cli_spei_pearson_02.nc`</br>
	3. 3-month: `/output/nc_original/stp_cli_spei_pearson_03.nc`</br>
	4. 6-month: `/output/nc_original/stp_cli_spei_pearson_06.nc`</br>
	5. 9-month: `/output/nc_original/stp_cli_spei_pearson_09.nc`</br>
	6. 12-month: `/output/nc_original/stp_cli_spei_pearson_12.nc`</br>
	7. 18-month: `/output/nc_original/stp_cli_spei_pearson_18.nc`</br>
	8. 24-month: `/output/nc_original/stp_cli_spei_pearson_24.nc`</br>
	9. 36-month: `/output/nc_original/stp_cli_spei_pearson_36.nc`</br>
	10. 48-month: `/output/nc_original/stp_cli_spei_pearson_48.nc`</br>
	11. 60-month: `/output/nc_original/stp_cli_spei_pearson_60.nc`</br>
	12. 72-month: `/output/nc_original/stp_cli_spei_pearson_72.nc`</br>


When the SPEI calculation completed, move arrange all the output by moving SPEI files with gamma to `gamma` folder and with pearson to `pearson` folder.  


## Output translation

For the translation to GeoTIFF as a final output, we will use gamma version.  


## Time processing

For small area of interest, the calculation will fast and don’t take much time. Monthly IMERG data, global coverage 180W - 180E, 60N - 60S, 0.1 deg spatial resolution, it takes almost 9-hours to process SPI 1-72 months.  