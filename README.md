[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Yi0Zbe2y)
# MAST30034 Project 1 README.md
- Name: `Saleha Khalid`
- Student ID: `1122166`

## README 

**Research Goal:** My research goal is demand analysis based on events in New York

**Timeline:** The timeline for the research area is January 2023 - April 2024.

### Setup Environment
1. Through the terminal or command prompt, change directory to be at the root directory of the project folder
2. Run the following command to install all required python packages:
    ```
    pip3 install -r requirements.txt
    ```

### Download external datasets and shape files
**Events Dataset:**
1. Data is available for download at https://data.cityofnewyork.us/City-Government/NYC-Permitted-Event-Information-Historical/bkfu-528j/about_data
2. Go to Actions > Query data > Start date between 2023-01-01 12:00AM and 2024-05-01 12:00AM > Apply
3. Once query is successful > Export
4. Keep format csv and download
5. Rename file to be nyc_events_raw.csv
6. Ensure that the file is saved under `data/raw` directory

**Weather Dataset:**
1. Data is available for download at https://www.ncei.noaa.gov/access/search/data-search/daily-summaries?bbox=45.006,-79.763,40.506,-71.870&place=State%20or%20Province:40&startDate=2023-01-01T00:00:00&endDate=2023-12-31T23:59:59
2. Download data under NY CITY CENTRAL PARK, NY US (USW00094728.csv)
3. Rename file to be nyc_weather_raw.csv
4. Ensure that the file is saved under `data/raw` directory

**Police Precinct Shape file:**
1. shapefile for precincts downloadable here https://data.cityofnewyork.us/api/geospatial/78dh-3ptz?method=export&format=Shapefile) and csv downloadable here https://data.cityofnewyork.us/api/views/kmub-vria/rows.csv?accessType=DOWNLOAD 
2. Make sure the precincts shape file folder is named `precints`, and is saved in `data/raw` directory, and make sure all the files in that folder have the name `nypp.*` (mainly need `nypp.csv` and `nypp.shp`)

**Taxi Zone Shape file:**
1. Shape file for taxi zones downloaded from: https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip (the same folder was taken from the MAST30034 Tutorial)
2. The `.csv` can be found here: https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
4. Ensure that the taxi zone shape file is a folder named `taxi_zones` and is saved in `data/raw` directory, making sure that the folder has the files `taxi_zones.shp` and `taxi+_zone_lookup.csv`

### Running the required files
To run the pipeline, please visit the `scripts` directory and run the files in order:
1. `download.py`: This downloads the raw yellow taxi data into the `data/landing` directory.

Then from the root directory run the following in order:

2. `taxi_preprocess.ipynb`: This notebook details all preprocessing steps and analysis for yellow taxis and outputs it to the `data/raw/yellow` and `data/curated/taxi` directory.
3. `event_preprocess.ipynb`: This notebook details all preprocessing steps and analysis for nyc events and outputs it to the `data/curated/events` directory
4. `weather_preprocess.ipynb`: This notebook details all preprocessing steps for weather data and outputs it to the `data/curated/weather` directory
5. `mapping.ipynb`: This notebook creates a mapping from taxi zones to precinct (required for modelling and visualization) and outputs it to the `data/curated` directory
6. `visualization.ipynb`: This notebook is used for visualizing the analysis for the curated data
7. `modelling.ipynb`: This notebook is used to fit and evaluate the model
