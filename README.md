### Introduction ###
A sample project that integrates various ploting libraries with Django and PostgreSQL. Mainly for my own future reference. With each, I create a bar plot, scatterplot, boxplot, and histogram. 

Each of the Python libraries has some workflow that invloves turning some data types into html and javascript.

The Bokeh receipe is create a figure, pass a source, pass some config args, and render to a `<script>` and `<div>` html tags to be passed as template context. 

D3 is a bit different. By virtue of being JS, it integrates nicely into the DOM but needs an API to call to get the JSON.

#### Thoughts ####

Bokeh's been pretty easy to use. The sources make sense and passing in args to the plotting functions is easy enough. 

#### Data Used ####
##### CSVs #####
* [Chicago Residential Sales](https://datacatalog.cookcountyil.gov/Property-Taxation/Cook-County-Assessor-s-Residential-Sales-Data/5pge-nu6u)
* [Chicago Annual Tax Sale](https://datacatalog.cookcountyil.gov/Property-Taxation/Treasurer-Annual-Tax-Sale/55ju-2fs9)
* [Chicago Scavenger Sale](https://datacatalog.cookcountyil.gov/Property-Taxation/Treasurer-Scavenger-Tax-Sale/ydgz-vkrp)
* [Chicago Community Areas Demographics](https://datahub.cmap.illinois.gov/dataset/community-data-snapshots-raw-data/resource/8c4e096e-c90c-4bef-9cf1-9028d094296e)


##### GIS Layers #####
* [Chicago Community Areas](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6)
* [Cook County Parcels](https://datacatalog.cookcountyil.gov/GIS-Maps/Historical-ccgisdata-Parcels-2016/a33b-b59u)