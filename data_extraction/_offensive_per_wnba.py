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

def calculate_and_save_offensive_per(url, output_file):
    """
    Fetch, parse, extract, clean WNBA Offensive Player data, calculate O-PER, and save to CSV.

    Args:
        url (str): The URL to fetch player data from.
        output_file (str): The path to save the final CSV file.

    Returns:
        None
    """
    soup_offensive = fetch_and_parse(url)
    relevant_columns_offensive = ["Player", "PTS", "AST", "ORB"]
    offensive_df = extract_and_clean_relevant_data(soup_offensive, relevant_columns_offensive)

    print("Initial DataFrame after extracting relevant columns (Offensive):")
    print(offensive_df.head())
    
    offensive_df = offensive_df.dropna(subset=["PTS", "AST", "ORB"])
    offensive_df["PTS"] = pd.to_numeric(offensive_df["PTS"], errors="coerce")
    offensive_df["AST"] = pd.to_numeric(offensive_df["AST"], errors="coerce")
    offensive_df["ORB"] = pd.to_numeric(offensive_df["ORB"], errors="coerce")
    offensive_df = offensive_df.dropna(subset=["PTS", "AST", "ORB"])

    top_50_offensive_df = offensive_df.nlargest(50, "PTS")
    top_50_offensive_df["O-PER"] = (top_50_offensive_df["PTS"] + top_50_offensive_df["AST"] + top_50_offensive_df["ORB"]) / 3
    top_50_offensive_df["O-PER"] = top_50_offensive_df["O-PER"].round(1)

    final_columns_offensive = ["Player", "PTS", "AST", "ORB", "O-PER"]
    top_50_offensive_df = top_50_offensive_df[final_columns_offensive]

    top_50_offensive_df.to_csv(output_file, index=False)
    print(f"Top 50 Offensive data with O-PER saved to '{output_file}'")
    print("Final Cleaned Offensive DataFrame with O-PER:")
    print(top_50_offensive_df.head())