from .common import fetch_and_parse, extract_table_data, save_to_csv
import pandas as pd

def extract_wnba_player_salaries(url, output_file):
    """
    Extracts WNBA player salary data from the specified URL and saves it to a CSV file.

    Args:
        url (str): The URL to fetch player salary data from.
        output_file (str): The path to the CSV file to save the extracted data.

    Returns:
        None
    """
    # Fetch and parse HTML content:
    soup = fetch_and_parse(url)
    
    # Locate table containing relevant data:
    table = soup.find('table')
    
    # Define headers for DataFrame:
    headers = ["Player", "2024 Salary"]
    
    # Initialize a list to store rows of data.
    rows = []
    
    # Iterate over each row in table body:
    for tr in table.find('tbody').find_all('tr'):
        cells = tr.find_all('td')
        name = cells[0].text.strip().split('\n')[0]  # Extract and clean player name.
        salary = cells[1].text.strip().split()[0]  # Extract and clean salary value.
        row = [name, salary]
        rows.append(row)
    
    # Create DataFrame from extracted rows:
    df = pd.DataFrame(rows, columns=headers)
    
    # Save DataFrame to CSV file:
    save_to_csv(df, output_file)

def extract_wnba_team_salaries(url, output_file):
    """
    Extracts WNBA team salary data from the specified URL and saves it to a CSV file.

    Args:
        url (str): The URL to fetch team salary data from.
        output_file (str): The path to the CSV file to save the extracted data.

    Returns:
        None
    """
    # Fetch and parse HTML content:
    soup = fetch_and_parse(url)
    
    # Extract table data with specific columns:
    df = extract_table_data(soup, 'th', keep_columns=['Team', 'Total Salaries'])
    
    # Save DataFrame to CSV file:
    save_to_csv(df, output_file)