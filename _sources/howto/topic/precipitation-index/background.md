# Precipitation Index

The Standardized Precipitation Index ([SPI](https://library.wmo.int/doc_num.php?explnum_id=7768)) is a drought index first developed by T. B. McKee, N.J. Doesken, and J. Kleist and in 1993 ([McKee et al. 1993](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#McKee1993)). The SPI is used for estimating wet or dry condition based on `precipitation` variable. This wet or dry condition can be monitored by the SPI on a variety of time scales from subseasonal to interannual scales. 

The SPI is expressed as standard deviations that the observed precipitation would deviate from the long-term mean, for a normal distribution and fitted probability distribution for the actual precipitation record. Since precipitation is not normally distributed, a transformation is first applied, followed by fitting to a normal distribution.

The Standardized Precipitation-Evapotranspiration Index ([SPEI](https://spei.csic.es)) is an extension of the widely used SPI. The SPEI is designed to take into account both `precipitation` and `potential evapotranspiration` (PET) in determining drought. Thus, unlike the SPI, the SPEI captures the main impact of increased temperatures on water demand. The SPEI can measure drought severity according to its intensity and duration, and can identify the onset and end of drought episodes. The SPEI allows comparison of drought severity through time and space, since it can be calculated over a wide range of climates, as can the SPI. 

The idea behind the SPEI is to compare the highest possible evapotranspiration (what we call the evaporative demand by the atmosphere) with the current water availability. Thus, precipitation (accumulated over a period of time) in the SPEI stands for the water availability, while ETo stands for the atmospheric water demand. 

## Calculation

The SPI calculation is based on the long-term precipitation record for a particular location and long-term period (longer than 30 years is desirable). The calculation method is comprised of a transformation of one frequency distribution (e.g., gamma) to another frequency distribution (normal, or Gaussian). The first step to calculate SPI is to adequately choose a particular probability distribution (e.g., gamma distribution, incomplete beta distribution (McKee et al. ([1993](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#McKee1993), [1995](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#McKee1995))), and Pearson III distribution (Guttman ([1998](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#Guttman1998), [1999](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#Guttman1999)))) that reliably fits the long-term precipitation time series and conduct fitting to that distribution. 

Gamma distribution has been widely used, as the gamma distribution has been understood as the reliable fit to the precipitation distribution. The fitting can be achieved through the maximum likelihood estimation of the gamma distribution parameters. The percentile value from this probability distribution is then transformed to the corresponding value in the new probability distribution. As a result, the probability that the rainfall is less than or equal to any rainfall amount will be the same as the probability that the new variate is less than or equal to the corresponding value of that rainfall amount. The normal distribution is usually used for this another transformation so that the mean and standard deviation of the SPI for a certain station and long-term period is zero and one, respectively ([Edwards and McKee 1997](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#Edwards1997)). 

The SPEI is really simple to calculate, and is based on the original SPI calculation procedure. The SPI is calculated using monthly precipitation as the input data. The SPEI uses the monthly difference between precipitation and PET. This represents a simple climatic water balance which is calculated at different time scales to obtain the SPEI.

Positive SPI values indicate wet condition greater than median precipitation, whereas negative values the dry condition less than median precipitation. More detailed description of the steps required to calculate the SPI is provided in [Lloyd-Hughes and Saunders (2002)](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#Lloyd2002).

Negative SPEI values represent rainfall deficit and less than median precipitation, and high potential epotranspiration (Dry), starts when the SPEI value is equal or below -1.0. Whereas positive SPEI values indicate rainfall surplus and greater than median precipitation, and low potential epotranspiration (Wet), starts when the SPEI value is equal or above 1.0, and ends when the value becomes negative.


## Interpretation

Since the SPI/SPEI values are obtained from the standard normal distribution, the unit of the SPI/SPEI can be “standard deviations”. The following table summarizes the cumulative probabilities for various SPI/SPEI values and possible interpretation of wet (or dry) conditions using the resulting SPI/SPEI values.

| SPI/SPEI | Cumulative Probability | Interpretation |
| ----- | ----- | -----|
| -3.0 | 0.0014 | Extremely dry |
| -2.5 | 0.0062 | Extremely dry |
| -2.0 | 0.0228 | Extremely dry (SPI < -2.0) |
| -1.5 | 0.0668 | Severly dry (-2.0 < SPI < -1.5) |
| -1.0 | 0.1587 | Moderately dry (-1.5 < SPI < -1.0) |
| -0.5 | 0.3085 | Near normal |
| 0.0 | 0.5000 | Near normal |
| 0.5 | 0.6915 | Near normal |
| 1.0 | 0.8413 | Moderately wet (1.0 < SPI < 1.5) |
| 1.5 | 0.9332 | Severly wet (1.5 < SPI < 2.0) |
| 2.0 | 0.9772 | Extremely wet (2.0 < SPI) |
| 2.5 | 0.9938 | Extremely wet |
| 3.0 | 0.9986 | Extremely wet |

The SPI maps can be interpreted at various time scales. This in turn indicates that the SPI is useful in both short-term and long-term applications. These time scales reflect the impact of drought on the availability of the different water resources. For instance, soil moisture conditions respond to precipitation anomalies on a relatively short scale. Groundwater, streamflow, and reservoir storage reflect the longer-term precipitation anomalies. For these reasons, SPI was originally calculated for 3–, 6–,12–, 24–, and 48–month time scales ([McKee et al. (1993)](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html#McKee1993)). A separate SPI value can be calculated for a selection of time scales, covering the last months (e.g., 3, 6, 12, 24, and 48 months), and ending on the last day of the latest month.

Source: [https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html](https://gmao.gsfc.nasa.gov/research/subseasonal/atlas/SPI-html/SPI-description.html)

![NormalCurve](../../../img/pi-background-normalcurve.png)

SPI labels and their relationship to the normal curve. The intensity implied by each label corresponds to the degree of removal from mean conditions (i.e., SPI=0). The percentages printed within the regions bounded by the dashed lines indicate the probability for SPI values to fall within that region only. (Source: [J. Keyantash](https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi))


## Strengths and Limitations

* Used for estimating meteorological conditions based on precipitation alone.

* Wet or dry conditions can be monitored on a variety of time scales from sub seasonal to interannual.

* Can be compared across regions with markedly difference climates.

* Does not consider the intensity of precipitation and its potential impacts on runoff, streamflow, and water availability.

* Expressed as the number of standard deviations from the long term mean, for a normally distributed random variable, and fitted probability distribution for the actual precipitation record.

* SPI values < 1 indicate a condition of drought, the more negative the value the more severe the drought condition. SPI values > +1 indicate wetter conditions compared to a climatology.


## Example

Expressed as the number of standard deviations from the long-term mean, for a normally distributed random variable, and fitted probability distribution for the actual precipitation record

SPI values < -1 indicate a condition of drought, the more negative the value the more severe the drought condition. SPI values > +1 indicate wetter conditions compared to a climatology

[https://drought.unl.edu/droughtmonitoring/SPI.aspx](https://drought.unl.edu/droughtmonitoring/SPI.aspx)

* SPI 1-month
	
	Similar to a map displaying the percent of normal precipitation for a month. Reflects relatively short term conditions. Its application can be related closely with short term soil moisture and crop stress.

	![SPI1](../../../img/pi-background-spi-01.png)

* 3 month
	
	Provides a comparison of the precipitation over a specific 3 month period with the precipitation totals from the same 3 month period for all the years included in the historical record. Reflects short and medium term moisture conditions and provides a seasonal estimation of precipitation.

	![SPI3](../../../img/pi-background-spi-02.png)

* 6 month

	Compares the precipitation for that period with the same 6 month period over the historical record. A 6 month SPI can be very effective in showing the precipitation over distinct seasons and may be associated with anomalous streamflow and reservoir levels.

	![SPI6](../../../img/pi-background-spi-03.png)

* 9 month

	Provides an indication of precipitation patterns over a medium time scale. SPI values below 1.5 for these time scales are usually a good indication that significant impacts are occurring in agriculture and may be showing up in other sectors as well.

	![SPI9](../../../img/pi-background-spi-04.png)

* 12 month

	Reflects long term precipitation patterns. Longer SPIs tend toward zero unless a specific trend is taking place. SPIs of these time scales are probably tied to streamflow, reservoir levels, and even groundwater levels at the longer time scales. In some locations of the country, the 12 month SPI is most closely related with the Palmer Index, and the two indices should reflect similar conditions.

	![SPI12](../../../img/pi-background-spi-05.png)


## References

### Journal

* Guttman, N. B., 1999: Accepting the Standardized Precipitation Index: A calculation algorithm. J. Amer. Water Resour. Assoc., 35(2), 311-322. [Link](https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi)
* Lloyd Hughes, B., and M. A. Saunders, 2002: A drought climatology for Europe. Int. J. Climatol., DOI:10.1002/joc.846 [Link](https://rmets.onlinelibrary.wiley.com/doi/epdf/10.1002/joc.846)
* McKee, T.B., N. J. Doesken, and J. Kliest, 1993: The relationship of drought frequency and duration to time scales. In Proceedings of the 8th Conference of Applied Climatology, 17 22 January, Anaheim, CA. American Meterological Society, Boston, MA. 179-18. [Link](https://www.droughtmanagement.info/literature/AMS_Relationship_Drought_Frequency_Duration_Time_Scales_1993.pdf)
* Guttman, N. B., 1998: Comparing the Palmer Drought Index and the Standardized Precipitation Index. J. Amer. Water Resources Assoc., 34(1), 113-121.
* Edwards, D. C., and T. B. McKee, 1997: Characteristics of 20th century drought in the United States at multiple time scales. Climatology Report No. 97-2, Colorado State Univ., Ft. Collins, CO. 
* McKee, T. B., N. J. Doesken, and J. Kleist, 1995: Drought monitoring with multiple time scales. Ninth Conference on Applied Climatology, American Meteorological Society, Jan15-20, 1995, Dallas TX, pp.233-236.


### Website

* Keyantash, John & National Center for Atmospheric Research Staff (Eds). "The Climate Data Guide: Standardized Precipitation Index (SPI)." Retrieved from [https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi](https://climatedataguide.ucar.edu/climate-data/standardized-precipitation-index-spi)
* National Drought Mitigation Center (NDMC) at the University of Nebraska Lincoln. [Link](https://drought.unl.edu/droughtmonitoring/SPI.aspx)
* World Meteorological Organization (WMO), 2012: Standardized Precipitation Index User Guide. [Link](https://library.wmo.int/doc_num.php?explnum_id=7768)
* Climate Indices in Python [https://climate-indices.readthedocs.io/en/latest/](https://climate-indices.readthedocs.io/en/latest/)
* Climate Engine - [https://app.climateengine.org/climateEngine](https://app.climateengine.org/climateEngine)
* NASA ARSET on Application of GPM IMERG Reanalysis for Assessing Extreme Dry and Wet Periods. [Link](https://appliedsciences.nasa.gov/join-mission/training/english/arset-applications-gpm-imerg-reanalysis-assessing-extreme-dry-and-wet)
* CHIRPS, Climate Hazard Centre UCSB - [https://chc.ucsb.edu/data/chirps](https://chc.ucsb.edu/data/chirps)
* IMERG, Integrated Multi-satellitE Retrievals for GPM - [https://gpm.nasa.gov/data/imerg](https://gpm.nasa.gov/data/imerg)
* TerraClimate, Climatology Lab UCMERCED - [https://www.climatologylab.org/terraclimate.html](https://www.climatologylab.org/terraclimate.html)