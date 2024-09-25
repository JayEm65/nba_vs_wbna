from .common import fetch_and_parse, extract_table_data, save_to_csv
import pandas as pd

def extract_wnba_player_salaries(url, output_file):
    soup = fetch_and_parse(url)
    table = soup.find('table')
    
    headers = ["Player", "2024 Salary"]
    rows = []
    
    for tr in table.find('tbody').find_all('tr'):
        cells = tr.find_all('td')
        name = cells[0].text.strip().split('\n')[0]
        salary = cells[1].text.strip().split()[0]
        row = [name, salary]
        rows.append(row)
    
    df = pd.DataFrame(rows, columns=headers)
    save_to_csv(df, output_file)

def extract_wnba_team_salaries(url, output_file):
    soup = fetch_and_parse(url)
    df = extract_table_data(soup, 'th', keep_columns=['Team', 'Total Salaries'])
    save_to_csv(df, output_file)