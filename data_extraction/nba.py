from .common import fetch_and_parse, extract_table_data, save_to_csv

def extract_nba_player_salaries(url, output_file):
    """
    Extracts NBA player salary data from the specified URL and saves it to a CSV file.

    Args:
        url (str): The URL to fetch player salary data from.
        output_file (str): The path to the CSV file to save the extracted data.

    Returns:
        None
    """
    # Fetch and parse HTML content:
    soup = fetch_and_parse(url)
    
    # Extract table data containing player salaries:
    df = extract_table_data(soup, 'td')
    
    # Save DataFrame to CSV file:
    save_to_csv(df, output_file)

def extract_nba_team_salaries(url, output_file):
    """
    Extracts NBA team salary data from the specified URL and saves it to a CSV file.

    Args:
        url (str): The URL to fetch team salary data from.
        output_file (str): The path to the CSV file to save the extracted data.

    Returns:
        None
    """
    # Fetch and parse HTML content:
    soup = fetch_and_parse(url)
    
    # Extract the table data containing team salaries:
    df = extract_table_data(soup, 'td')
    
    # Save DataFrame to CSV file:
    save_to_csv(df, output_file)