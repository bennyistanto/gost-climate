# Temperature Condition Index

The Temperature Condition Index (TCI) compares the current Land Surface Temperature (LST) to the range of values observed in the same period in previous years. The TCI is expressed in % and gives an idea where the observed value is situated between the extreme values (minimum and maximum) in the previous years. TCI used to determine stress on vegetation caused by temperatures and excessive wetness. Conditions are estimated relative to the maximum and minimum temperatures and modified to reflect different vegetation responses to temperature.  

**How it works**

The TCI is calculated using the equation, 

`TCI = 100 * (LSTmax - LST)(LSTmax - LSTmin)`

where:

`LST` is the current value of LST.<br>
`LSTmin` is the long-term minimum value of LST.<br>
`LSTmax` is the long-term maximum value of LST.<br>

LST max and min derived from MODIS data.  

**About the data**

| Characteristic  | Description  |
|---|---|
| Function  | a proxy for Vegetation Health Index calculation  |
| Variable  | TCI  |
| Geographic coverage  | Global (monthly) and Regional (16-days)  |
| Spatial resolution  | 5.6 km (MOD11C3) and 1 km (MOD11A2) at equator  |
| Temporal resolution  | Monthly and 16-days  |
| Format  | GeoTIFF  |
| Unit  | Percent (%)  |

**Data access**

Global TCI data available at DEC S3: 