import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from io import StringIO

def fetch_market_data(date):
    formatted_date = date.strftime('%Y-%m-%d')

    url = f'https://hupx.hu/en/market-data/id/market-data?date={formatted_date}'

    response = requests.get(url)
    response.raise_for_status()  

    soup = BeautifulSoup(response.content, 'html.parser')

    tabs = soup.find_all('div', class_='tabs-panel')

    dfs = []
    for tab in tabs:
        table = tab.find('table')
        if table:
            dfs.append(pd.read_html(StringIO(str(table)))[0])

    if len(dfs) != 2:
        raise ValueError(f"couldnt find 2 tables, found {len(dfs)}")

    output_file = f'market_data_{formatted_date}.xlsx'
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    dfs[0].to_excel(writer, sheet_name='Hours', index=False)
    dfs[1].to_excel(writer, sheet_name='Quartelly hours', index=False)

    writer.close()

    print(f'Data saved: {output_file}')

today = datetime.now()
yesterday = datetime.now() - timedelta(1)

fetch_market_data(yesterday)
fetch_market_data(today)
