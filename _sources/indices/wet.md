# Wet Days

The number of wet days (DD) is the largest number of days with daily precipitation amount more than 1 mm (or depending on the rain days criteria of the country), within a certain time. Usually the process counts the number of days within a year to measure the wet condition.

### How it works

Calculate the number of rain days based on the threshold in a year.

Option for rain day's threshold: 1, 2.5, 5, 10 or 20 milimeters of rainfall per day

```
IF todayRAIN > 1 THEN WD == 1
```

WD derived from IMERG data

### About the data

| Characteristic  | Description  |
|---|---|
| Function  | Display daily WD  |
| Variable  | WD  |
| Geographic coverage  | Global 60N-60S, 180W-180E |
| Spatial resolution  | 0.1 degree ~ 11.1 km at equator  |
| Temporal resolution  | Daily  |
| Format  | GeoTIFF  |
| Unit  | Number of day  |

### Symbology

The threshold and the symbology for the WD can follow below color codes and image.

| Threshold  | Hex  | RGB  |
|---|---|---|---|
| <50  | `#ffffcc` ![#ffffcc](https://via.placeholder.com/15/ffffcc/000000?text=+)  | rgb(255,255,204)  |
| 51 - 100  | `#c2e699` ![#c2e699](https://via.placeholder.com/15/c2e699/000000?text=+)  | rgb(194,230,153)  |
| 101 - 150  | `#78c679` ![#78c679](https://via.placeholder.com/15/78c679/000000?text=+)  | rgb(120,198,121)  |
| 151 - 200  | `#31a354` ![#31a354](https://via.placeholder.com/15/31a354/000000?text=+)  | rgb(49,163,84)  |
| >201  | `#006837` ![#006837](https://via.placeholder.com/15/006837/000000?text=+)  | rgb(0,104,55)  |

### Data access

Global WD data available at DEC S3: `s3://wbgdecinternal-ntl/climate/products/wetdays-imerg`