# CHIRPS

Climate Hazards Group InfraRed Precipitation with Station data (CHIRPS) from Climate Hazard Center (CHC), Department of Geography, University of California Santa Barbara - [https://www.chc.ucsb.edu/data/chirps](https://www.chc.ucsb.edu/data/chirps) is a 35+ year quasi-global rainfall data set. Spanning 50°S-50°N (and all longitudes) and ranging from 1981 to near-present, CHIRPS incorporates CHC's in-house climatology, CHPclim, 0.05° resolution satellite imagery, and in-situ station data to create gridded rainfall time series for trend analysis and seasonal drought monitoring. 

To support the activity, GOST utilise CHIRPS's monthly rainfall data.


**About the data**

| Characteristic  | Description  |
|---|---|
| Function  | Displays daily, pentad, dekad, monthly, 2-monthly, 3-monthly and annual rainfall data  |
| Variable  | Total rainfall  |
| Geographic coverage  | Global 50N-50S, 180W-180E |
| Spatial resolution  | 0.05 degree ~ 5.6 km at equator  |
| Temporal resolution  | daily, pentad, dekad, monthly, 2-monthly, 3-monthly and annual  |
| Format  | GeoTIFF, BIL and NetCDF  |
| Unit  | Total mm for given time step, mm/pentad, mm/month, etc.  |
| Reference  | https://wiki.chc.ucsb.edu/CHIRPS_FAQ  |

**Symbology**

The threshold and the symbology for the `monthly` rainfall in milimeters can follow below colorcodes and image.

| Class  | Hex  | RGB  |
|---|---|---|
| 0 - 5  | `#ffffff` ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) | rgb(255, 255, 255)  |
| 5 to 10  | `#69F585` ![#69F585](https://via.placeholder.com/15/69F585/000000?text=+)  | rgb(105, 245, 133)  |
| 10 to 25  | `#00D157` ![#00D157](https://via.placeholder.com/15/00D157/000000?text=+)  | rgb(0, 209, 87)  |
| 25 to 50  | `#00A133` ![#00A133](https://via.placeholder.com/15/00A133/000000?text=+)  | rgb(0, 161, 51)  |
| 50 to 75  | `#4AA6F0` ![#4AA6F0](https://via.placeholder.com/15/4AA6F0/000000?text=+)  | rgb(74, 166, 240)  |
| 75 to 100  | `#2485E8` ![#2485E8](https://via.placeholder.com/15/2485E8/000000?text=+)  | rgb(36, 133, 232)  |
| 100 to 150  | `#1266CC` ![#1266CC](https://via.placeholder.com/15/1266CC/000000?text=+)  | rgb(18, 102, 204)  |
| 150 to 200  | `#A38CF7` ![#A38CF7](https://via.placeholder.com/15/A38CF7/000000?text=+)  | rgb(163, 140, 247)  |
| 200 to 250  | `#7361D6` ![#7361D6](https://via.placeholder.com/15/7361D6/000000?text=+)  | rgb(115, 97, 214)  |
| 250 to 300  | `#402BAD` ![#402BAD](https://via.placeholder.com/15/402BAD/000000?text=+)  | rgb(64, 43, 173)  |
| 300 to 350  | `#FFBF54` ![#FFBF54](https://via.placeholder.com/15/FFBF54/000000?text=+)  | rgb(255, 191, 84)  |
| 350 to 400  | `#FF5E24` ![#FF5E24](https://via.placeholder.com/15/FF5E24/000000?text=+)  | rgb(255, 94, 36)  |
| 400 to 500  | `#E60A14` ![#E60A14](https://via.placeholder.com/15/E60A14/000000?text=+)  | rgb(230, 10, 20)  |
| 500 and above  | `#A8000A` ![#A8000A](https://via.placeholder.com/15/A8000A/000000?text=+)  | rgb(168, 0, 10)  |

![chirps](../img/data-chirps.png)


**Data access**

Official download link from CHIRPS available from: [https://data.chc.ucsb.edu/products/CHIRPS-2.0/](https://data.chc.ucsb.edu/products/CHIRPS-2.0/)

CHIRPS monthly data also available at DEC S3: `s3://wbgdecinternal-ntl/climate/data/chirps`
