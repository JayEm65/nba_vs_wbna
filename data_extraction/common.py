import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_and_parse(url):
    """
    Fetches the HTML content from the given URL and parses it with BeautifulSoup.

    Args:
        url (str): The URL to fetch the HTML content from.

    Returns:
        BeautifulSoup: Parsed HTML content.
    """
    # Send a GET request to specified URL:
    response = requests.get(url)
    
    # Check if request was successful:
    if response.status_code == 200:
        print(f"Successfully fetched the webpage: {url}")
    else:
        raise Exception(f"Failed to fetch the webpage: {response.status_code}")
    
    # Parse and return HTML content:
    return BeautifulSoup(response.content, 'html.parser')

def extract_table_data(soup, header_tag, keep_columns=None):
    """
    Extracts table data from the parsed HTML and converts it to a pandas DataFrame.

    Args:
        soup (BeautifulSoup): Parsed HTML content.
        header_tag (str): HTML tag used for table headers (e.g., 'th' or 'td').
        keep_columns (list, optional): List of columns to keep. Defaults to None.

    Returns:
        DataFrame: Extracted table data as a pandas DataFrame.
    """
    # Locate table in parsed HTML:
    table = soup.find('table')
    
    # Extract headers from table:
    headers = [th.text.strip() for th in table.find('thead').find_all(header_tag)]
    print(f"Headers found: {headers}")
    
    # Initialize list to store rows of data:
    rows = []
    
    # Iterate over each row in table body:
    for tr in table.find('tbody').find_all('tr'):
        cells = tr.find_all('td')
        row = [cell.text.strip() for cell in cells]
        rows.append(row)
    
    # Create DataFrame from extracted rows:
    df = pd.DataFrame(rows, columns=headers)
    
    # Filter DataFrame to keep specific columns if specified:
    if keep_columns:
        print(f"Filtering to keep columns: {keep_columns}")
        df = df[keep_columns]
    
    return df

def save_to_csv(df, output_file):
    """
    Saves the DataFrame to a CSV file.

    Args:
        df (DataFrame): The DataFrame to save.
        output_file (str): The path to the CSV file to save the data.

    Returns:
        None
    """
    # Save DataFrame to CSV file:
    df.to_csv(output_file, index=False)
    
    # Print success message:
    print(f"Data successfully scraped and saved to {output_file}")