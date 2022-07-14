# Dry Days

The number of dry days (DD) is the largest number of days with daily precipitation amount less than 1 mm (or depending on the rain days criteria of the country), within a certain time. Usually the process counts the number of days within a year to measure the dry condition.

**How it works**

Calculate the number of rain days based on the threshold in a year.

Option for rain day's threshold: 1, 2.5, 5, 10 or 20 milimeters of rainfall per day

```
IF todayRAIN > 1 THEN DD == 0
```

DD derived from IMERG data

**About the data**

| Characteristic  | Description  |
|---|---|
| Function  | Display daily DD  |
| Variable  | DD  |
| Geographic coverage  | Global 60N-60S, 180W-180E |
| Spatial resolution  | 0.1 degree ~ 11.1 km at equator  |
| Temporal resolution  | Daily  |
| Format  | GeoTIFF  |
| Unit  | Number of day  |

**Symbology**

The threshold and the symbology for the DD can follow below color codes and image.

| Threshold  | Hex  | RGB  |
|---|---|---|---|
| <50  | `#ffffd4` ![#ffffd4](https://via.placeholder.com/15/ffffd4/000000?text=+)  | rgb(255,255,212)  |
| 51 - 100  | `#fed98e` ![#fed98e](https://via.placeholder.com/15/fed98e/000000?text=+)  | rgb(254,217,142)  |
| 101 - 150  | `#fe9929` ![#fe9929](https://via.placeholder.com/15/fe9929/000000?text=+)  | rgb(254,153,41)  |
| 151 - 200  | `#d95f0e` ![#d95f0e](https://via.placeholder.com/15/d95f0e/000000?text=+)  | rgb(217,95,14)  |
| >201  | `#993404` ![#993404](https://via.placeholder.com/15/993404/000000?text=+)  | rgb(153,52,4)  |

**Data access**

Global DD data available at DEC S3: `s3://wbgdecinternal-ntl/climate/products/drydays-imerg`