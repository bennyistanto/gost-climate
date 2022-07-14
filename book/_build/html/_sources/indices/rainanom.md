# Rainfall anomaly

The objective of rainfall anomaly is to evaluate the quality of monthly rainfall over the country. This is achieved through analysis of anomalies, i.e. a comparison against a reference. The classic reference is the long-term average.  

Rainfall anomaly is generated based on dekad data. The model will calculate the accumulated rainfall and other climate indices of precipitation based on that data during the most recent dekad which has been aggregated from pentad estimates. Every month has three dekads, such that the first two dekads have 10 days (i.e., 1-10, 11-20), and the third is comprised of the remaining days of the month (21-28 or 21-29 or 21-30 or 21-31. Therefore, the length of the third dekad of each month is not consistent and varies from 8-11 days, depending on the length of the month.  

**About the data**

| Characteristic  | Description  |
|---|---|
| Function  | Displays dekad and monthly rainfall anomaly data  |
| Variable  | Rainfall anomaly  |
| Geographic coverage  | Global 50N-50S, 180W-180E |
| Spatial resolution  | 0.05 degree ~ 5.6 km at equator  |
| Temporal resolution  | dekad, 1-month, 3-month, 6-month, 9-month and 12-month, rolling by dekad.  |
| Format  | GeoTIFF  |
| Unit  | Percent (%) and milimeters  |

* **Ratio anomaly**

	The anomaly is calculated based on percentage of the average.  

	`Anomaly (%) = 100 * rainfall/mean_rainfall`

	where `rainfall` is current rainfall and `mean_rainfall` is long-term average of rainfall.  

	Rainfall anomaly derived from CHIRPS data.  

	**Symbology**

	The threshold and the symbology for the ratio anomaly can follow below colorcodes and image.  

	| Class  | Hex  | RGB  |
	|---|---|---|
	| 20% and below  | `#d73027` ![#d73027](https://via.placeholder.com/15/d73027/000000?text=+) | rgb(215,48,39)  |
	| 20 to 50%  | `#f46d43` ![#f46d43](https://via.placeholder.com/15/f46d43/000000?text=+)  | rgb(244,109,67)  |
	| 50 to 70%  | `#fdae61` ![#fdae61](https://via.placeholder.com/15/fdae61/000000?text=+)  | rgb(253,174,97)  |
	| 70 to 90%  | `#fee090` ![#fee090](https://via.placeholder.com/15/fee090/000000?text=+)  | rgb(254,224,144)  |
	| 90 to 110%  | `#ffffbf` ![#ffffbf](https://via.placeholder.com/15/ffffbf/000000?text=+)  | rgb(255,255,191)  |
	| 110 to 130%  | `#e0f3f8` ![#e0f3f8](https://via.placeholder.com/15/e0f3f8/000000?text=+)  | rgb(224,243,248)  |
	| 130 to 150%  | `#abd9e9` ![#abd9e9](https://via.placeholder.com/15/abd9e9/000000?text=+)  | rgb(171,217,233)  |
	| 150 to 180%  | `#74add1` ![#74add1](https://via.placeholder.com/15/74add1/000000?text=+)  | rgb(116,173,209)  |
	| 180% and above  | `#4575b4` ![#4575b4](https://via.placeholder.com/15/4575b4/000000?text=+)  | rgb(69,117,180)  |


* **Difference anomaly**

	The anomaly is calculated based on difference of the average.  

	`Anomaly (mm) = rainfall - mean_rainfall`

	where `rainfall` is current rainfall and `mean_rainfall` is long-term average of rainfall.  

	Difference anomaly derived from CHIRPS data.  


**Data access**

Global rainfall anomaly data available at DEC S3: 