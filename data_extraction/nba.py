from .common import fetch_and_parse, extract_table_data, save_to_csv

def extract_nba_player_salaries(url, output_file):
    soup = fetch_and_parse(url)
    df = extract_table_data(soup, 'td')
    save_to_csv(df, output_file)

def extract_nba_team_salaries(url, output_file):
    soup = fetch_and_parse(url)
    df = extract_table_data(soup, 'td')
    save_to_csv(df, output_file)