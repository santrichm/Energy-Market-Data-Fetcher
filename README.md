# Energy Market Data Fetcher

## Description
This project fetches market data from the [hupx.hu](https://hupx.hu/en/market-data/id/market-data) website for any given date. The retrieved data is saved in an Excel file with two sheets: one for hourly data and another for quarterly hours.

## Features
- Fetches market data for specified dates
- Saves data in Excel format for easy access and analysis
- Handles errors for missing data or issues with fetching

## Requirements
- Python 3.7+
- requests
- pandas
- beautifulsoup4
- xlsxwriter

## Installation
1. Clone this repository:

       git clone https://github.com/santrichm/Energy-Market-Data-Fetcher.git
       cd Energy-Market-Data-Fetcher
   
3. Install the required packages:

        pip install requests pandas beautifulsoup4 xlsxwriter


## Usage

To run the script, execute the following command:


    python HUPX.py

This will fetch the market data for the previous day and today, saving the results in files named 
      
      market_data_YYYY-MM-DD.xlsx.

  
##Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.


##License

This project is licensed under the MIT License.
