import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched the webpage: {url}")
    else:
        raise Exception(f"Failed to fetch the webpage: {response.status_code}")
    
    return BeautifulSoup(response.content, 'html.parser')

def extract_table_data(soup, header_tag, keep_columns=None):
    table = soup.find('table')
    
    headers = [th.text.strip() for th in table.find('thead').find_all(header_tag)]
    print(f"Headers found: {headers}")
    
    rows = []
    for tr in table.find('tbody').find_all('tr'):
        cells = tr.find_all('td')
        row = [cell.text.strip() for cell in cells]
        rows.append(row)
    
    df = pd.DataFrame(rows, columns=headers)
    
    if keep_columns:
        print(f"Filtering to keep columns: {keep_columns}")
        df = df[keep_columns]
    
    return df

def save_to_csv(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Data successfully scraped and saved to {output_file}")