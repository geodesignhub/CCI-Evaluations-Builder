# Geodesignhub CCI Evaluation Maps Builder
This program uses ESA CCI landcover data from [ESA CCI viewer](http://maps.elie.ucl.ac.be/CCI/viewer/) to develop Evaluation maps for [Geodesignhub](https://www.geodesignhub.com/). It uses simple rules to parse the existing data and build evaluation maps that can be used directly on Geodesignhub as evaluation maps. CCI data is available at 300m resolution at a worldwide so this tool can be used to make evaluation maps only any site across the world. It is recommended that you use this for slightly larger sites. 

Making evaluation maps is the most time consuming part of a Geodesign study, using this script it can be automated. The following evaluation maps are generated: 

* Urban (URB / Housing (HSG) + Industry (IND) + Commerce(COM))
* Agriculture (AG)
* Industrial (IND)
* Forests (FOR)
* Hydrology (HYDRO)
* Green Infrastructure (GI)

Find out more about evaluation maps at the [Making Evaluations Maps](https://community.geodesignhub.com/t/making-evaluation-maps/62) in our community page. 

If you are new to Geodesignhub, please see our course at [Teachable.com](https://geodesignhub.teachable.com/p/geodesign-with-geodesignhub/)  

## Copyright
The data is &copy; ESA Climate Change Initiative - Land Cover led by UCLouvain (2017)

## Installation
Use the requirements.txt file to install libraries that are required for the tool, Python 3 enviornment is recommended: 

```
pip install -r requirements.txt
```

## 3-Step process
**1. Download raw data**

1. Go to [ESA CCI viewer](http://maps.elie.ucl.ac.be/CCI/viewer/download.php) to order and download the CCI raster data and clip it to your area of interest in QGIS or other software.
2. Convert the clipped area to Vector by using the `Polygonize` command for e.g. in QGIS
2. Put this file in the ```working``` folder 
3. Update the ```config.py``` file to update the location of Area of Interest

**2. Update config.py**

1. Set the boundary parameter to set the `aoifile` attribute to a publiclly available boundary of the study area. 

**3. Upload Evaluations**

1. Run the `CCI-evaluations-generator.py` script and check the `output` folder for the Evaluation GeoJSON that can be uploaded to Geodesignhub for your project. 
2. If you are familiar with 

