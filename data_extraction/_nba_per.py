import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

def extraction_webscrapping(url, output_file, header_tag, keep_columns=None):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched the webpage: {url}")
    else:
        raise Exception(f"Failed to fetch the webpage: {response.status_code}")

    soup = BeautifulSoup(response.content, 'html.parser')
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

    # Drop unnecessary columns
    df.drop(columns=['Team', 'Pos'], inplace=True, errors='ignore')

    output_path = os.path.join('csv', output_file)
    df.to_csv(output_path, index=False)
    print(f"Data successfully scraped and saved to {output_file}")

def load_and_extract_all(csv_file, value_column, col_rename):
    df = pd.read_csv(os.path.join('csv', csv_file))
    df.rename(columns={value_column: col_rename}, inplace=True)
    return df

def calculate_per():
    df_assists = load_and_extract_all('assists_2024.csv', 'Value', 'AST')
    df_player_stats = load_and_extract_all('player-stat_2024.csv', 'Value', 'PTS')
    df_OR = load_and_extract_all('rebounds-offensive.csv', 'Value', 'ORB')
    df_DRB = load_and_extract_all('rebounds-defensive.csv', 'Value', 'DRB')
    df_BLK = load_and_extract_all('blocks.csv', 'Value', 'BLK')
    df_STL = load_and_extract_all('steals.csv', 'Value', 'STL')

    for df in [df_assists, df_player_stats, df_OR, df_DRB, df_BLK, df_STL]:
        df['Player'] = df['Player'].str.strip()

    df_offense = df_player_stats.merge(df_assists, on="Player", how='outer').merge(df_OR, on="Player", how='outer')
    df_defense = df_DRB.merge(df_BLK, on="Player", how='outer').merge(df_STL, on="Player", how='outer')

    df_offense['O_PER'] = ((df_offense['PTS'].fillna(0) + df_offense['AST'].fillna(0) + df_offense['ORB'].fillna(0)) / 3).round(1)
    df_defense['D_PER'] = ((df_defense['DRB'].fillna(0) + df_defense['BLK'].fillna(0) + df_defense['STL'].fillna(0)) / 3).round(1)

    top_50_offensive = df_offense.sort_values(by='O_PER', ascending=False).head(50)
    top_50_defensive = df_defense.sort_values(by='D_PER', ascending=False).head(50)

    top_50_offensive.to_csv('nba_top_50_offensive_per.csv', index=False)
    top_50_defensive.to_csv('nba_top_50_defensive_per.csv', index=False)

    print("Top 50 Offensive PER data saved to 'nba_top_50_offensive_per.csv'.")
    print("Top 50 Defensive PER data saved to 'nba_top_50_defensive_per.csv'.")

def extract_and_calculate_per():
    urls_and_files = [
        ("https://www.teamrankings.com/nba/player-stat/points", 'player-stat_2024.csv', 'th', ['Player', 'Value']),
        ("https://www.teamrankings.com/nba/player-stat/assists", 'assists_2024.csv', 'th', ['Player', 'Value']),
        ("https://www.teamrankings.com/nba/player-stat/rebounds-offensive", 'rebounds-offensive.csv', 'th', ['Player', 'Value']),
        ("https://www.teamrankings.com/nba/player-stat/rebounds-defensive", 'rebounds-defensive.csv', 'th', ['Player', 'Value']),
        ("https://www.teamrankings.com/nba/player-stat/blocks", 'blocks.csv', 'th', ['Player', 'Value']),
        ("https://www.teamrankings.com/nba/player-stat/steals", 'steals.csv', 'th', ['Player', 'Value'])
    ]

    # Perform data extraction
    for url, output_file, header_tag, keep_columns in urls_and_files:
        extraction_webscrapping(url, output_file, header_tag, keep_columns)

    # Perform PER calculations
    calculate_per()

if __name__ == "__main__":
    extract_and_calculate_per()