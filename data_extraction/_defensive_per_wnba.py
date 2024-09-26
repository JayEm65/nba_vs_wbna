import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_and_parse(url):
    """
    Fetch and parse the HTML content from the given URL.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        BeautifulSoup: Parsed HTML content.
    """
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched the webpage: {url}")
    else:
        raise Exception(f"Failed to fetch the webpage: {response.status_code}")
    return BeautifulSoup(response.content, 'html.parser')

def extract_and_clean_relevant_data(soup, relevant_columns):
    """
    Extract relevant table data from the parsed HTML and clean it.

    Args:
        soup (BeautifulSoup): Parsed HTML content.
        relevant_columns (list): List of relevant columns to keep.

    Returns:
        DataFrame: Cleaned DataFrame with relevant columns.
    """
    table = soup.find('table')
    headers = [th.text.strip() for th in table.find('thead').find_all('th')]
    columns_indices = {header: index for index, header in enumerate(headers) if header in relevant_columns}

    rows = []
    for tr in table.find('tbody').find_all('tr'):
        cells = tr.find_all('td')
        if len(cells) < len(relevant_columns):
            continue  # Skip rows with incomplete data
        row = {}
        for header in relevant_columns:
            index = columns_indices[header]
            if index < len(cells):
                value = cells[index].text.strip().split('\n')[0]
                row[header] = value
            else:
                row[header] = None
        rows.append(row)
    
    df = pd.DataFrame(rows, columns=relevant_columns)
    return df

def calculate_and_save_defensive_per(url, output_file):
    """
    Fetch, parse, extract, clean WNBA Defensive Player data, calculate D-PER, and save to CSV.

    Args:
        url (str): The URL to fetch player data from.
        output_file (str): The path to save the final CSV file.

    Returns:
        None
    """
    soup_defensive = fetch_and_parse(url)
    relevant_columns_defensive = ["Player", "DRB", "BLK", "STL"]
    defensive_df = extract_and_clean_relevant_data(soup_defensive, relevant_columns_defensive)

    print("Initial DataFrame after extracting relevant columns (Defensive):")
    print(defensive_df.head())
    
    defensive_df = defensive_df.dropna(subset=["DRB", "BLK", "STL"])
    defensive_df["DRB"] = pd.to_numeric(defensive_df["DRB"], errors="coerce")
    defensive_df["BLK"] = pd.to_numeric(defensive_df["BLK"], errors="coerce")
    defensive_df["STL"] = pd.to_numeric(defensive_df["STL"], errors="coerce")
    defensive_df = defensive_df.dropna(subset=["DRB", "BLK", "STL"])

    top_50_defensive_df = defensive_df.nlargest(50, "DRB")
    top_50_defensive_df["D-PER"] = (top_50_defensive_df["DRB"] + top_50_defensive_df["BLK"] + top_50_defensive_df["STL"]) / 3
    top_50_defensive_df["D-PER"] = top_50_defensive_df["D-PER"].round(1)

    final_columns_defensive = ["Player", "DRB", "BLK", "STL", "D-PER"]
    top_50_defensive_df = top_50_defensive_df[final_columns_defensive]

    top_50_defensive_df.to_csv(output_file, index=False)
    print(f"Top 50 Defensive data with D-PER saved to '{output_file}'")
    print("Final Cleaned Defensive DataFrame with D-PER:")
    print(top_50_defensive_df.head())