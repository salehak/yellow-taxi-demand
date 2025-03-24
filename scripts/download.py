# This code is adapted from "Python_PreReq_Notebook.ipynb" from MAST30034

import os
from urllib.request import urlretrieve

# Change directory to download dataset
output_relative_dir = '../data/'

# Function to download data for a specific year and month range
def download_data(year, months):
    # this is the URL template as of 07/2023
    URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"
    
    # Data output directory is `data/landing/`
    tlc_output_dir = os.path.join(output_relative_dir, 'landing')

    # Create the directory if it does not exist
    os.makedirs(tlc_output_dir, exist_ok=True)

    for month in months:
        # 0-fill i.e 1 -> 01, 2 -> 02, etc
        month = str(month).zfill(2) 
        print(f"Begin month {month} for year {year}")
        
        # Generate URL
        url = f'{URL_TEMPLATE}{year}-{month}.parquet'
        # Generate output location and filename
        output_dir = os.path.join(tlc_output_dir, f'yellow_{year}-{month}.parquet')
        
        try:
            # Download
            urlretrieve(url, output_dir)
            print(f"Completed month {month} for year {year}")
        except Exception as e:
            print(f"Error downloading month {month} for year {year}: {e}")

# Download data for 2023 (all months)
download_data('2023', range(1, 13))

# Download data for 2024 (January to April)
download_data('2024', range(1, 5))
