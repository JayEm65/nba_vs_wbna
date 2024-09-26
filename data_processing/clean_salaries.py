import pandas as pd

def clean_and_extract_top_salaries(nba_file, wnba_file, output_nba_file, output_wnba_file):
    # Load NBA Player Salaries CSV
    nba_df = pd.read_csv(nba_file)

    # If there are multiple salary columns, select one, assuming '2024 Salary'
    if '2023/24(*)' in nba_df.columns:
        nba_df = nba_df.rename(columns={'2023/24(*)': '2024 Salary'})
    elif '2023/24' in nba_df.columns:
        nba_df = nba_df.rename(columns={'2023/24': '2024 Salary'})

    # Convert NBA Salary column to numeric
    nba_df['2024 Salary'] = nba_df['2024 Salary'].replace(r'[\$,]', '', regex=True).astype(float)

    # Remove duplicates and keep the highest salary
    cleaned_nba_df = nba_df.sort_values('2024 Salary', ascending=False).drop_duplicates(subset=['Player'], keep='first')

    # Keep top 150 highest-paid NBA players
    top_150_nba_df = cleaned_nba_df.head(150)

    # Drop unnecessary columns to remove old salary formatting
    top_150_nba_df = top_150_nba_df[['Player', '2024 Salary']]

    # Save cleaned NBA salaries to a new CSV
    top_150_nba_df.to_csv(output_nba_file, index=False)
    print(f"Cleaned NBA salaries saved to '{output_nba_file}'.")

    # Load WNBA Player Salaries CSV
    wnba_df = pd.read_csv(wnba_file)

    # Convert WNBA Salary column to numeric
    wnba_df = wnba_df[wnba_df['2024 Salary'].str.startswith('$', na=False)]
    wnba_df['2024 Salary'] = wnba_df['2024 Salary'].replace(r'[\$,]', '', regex=True).astype(float)

    # Remove duplicates and keep the highest salary
    cleaned_wnba_df = wnba_df.sort_values('2024 Salary', ascending=False).drop_duplicates(subset=['Player'], keep='first')

    # Keep top 150 highest-paid WNBA players
    top_150_wnba_df = cleaned_wnba_df.head(150)

    # Drop unnecessary columns to ensure consistent formatting
    top_150_wnba_df = top_150_wnba_df[['Player', '2024 Salary']]

    # Save cleaned WNBA salaries to a new CSV
    top_150_wnba_df.to_csv(output_wnba_file, index=False)
    print(f"Cleaned WNBA salaries saved to '{output_wnba_file}'.")

def clean_and_extract_top_team_salaries(nba_team_file, wnba_team_file, output_nba_team_file, output_wnba_team_file):
    # Load NBA Team Salaries CSV
    nba_team_df = pd.read_csv(nba_team_file)

    # If there are multiple salary columns, select one, assuming '2024 Salary'
    if '2023/24(*)' in nba_team_df.columns:
        nba_team_df = nba_team_df.rename(columns={'2023/24(*)': '2024 Total Salaries'})
    elif '2023/24' in nba_team_df.columns:
        nba_team_df = nba_team_df.rename(columns={'2023/24': '2024 Total Salaries'})

    # Convert NBA Team Salary column to numeric
    nba_team_df['2024 Total Salaries'] = nba_team_df['2024 Total Salaries'].replace(r'[\$,]', '', regex=True).astype(float)

    # Keep top 12 highest-paid NBA teams
    top_12_nba_team_df = nba_team_df.sort_values('2024 Total Salaries', ascending=False).head(12)

    # Drop unnecessary columns to remove old salary formatting
    top_12_nba_team_df = top_12_nba_team_df[['Team', '2024 Total Salaries']]

    # Save cleaned NBA team salaries to a new CSV
    top_12_nba_team_df.to_csv(output_nba_team_file, index=False)
    print(f"Cleaned NBA team salaries saved to '{output_nba_team_file}'.")

    # Load WNBA Team Salaries CSV
    wnba_team_df = pd.read_csv(wnba_team_file)

    # Convert WNBA Team Salary column to numeric
    wnba_team_df['Total Salaries'] = wnba_team_df['Total Salaries'].replace(r'[\$,]', '', regex=True).astype(float)

    # Keep top 12 highest-paid WNBA teams
    top_12_wnba_team_df = wnba_team_df.sort_values('Total Salaries', ascending=False).head(12)

    # Drop unnecessary columns to ensure consistent formatting
    top_12_wnba_team_df = top_12_wnba_team_df[['Team', 'Total Salaries']]

    # Save cleaned WNBA team salaries to a new CSV
    top_12_wnba_team_df.to_csv(output_wnba_team_file, index=False)
    print(f"Cleaned WNBA team salaries saved to '{output_wnba_team_file}'.")

if __name__ == "__main__":
    # Paths to the input and output files for player salaries
    nba_player_file = 'nba_player_salaries_2024.csv'
    wnba_player_file = 'wnba_player_salaries_2024.csv'
    output_nba_player_file = 'cleaned_data/top_150_nba_player_salaries_2024.csv'
    output_wnba_player_file = 'cleaned_data/top_150_wnba_player_salaries_2024.csv'

    # Paths to the input and output files for team salaries
    nba_team_file = 'nba_team_salaries_2024.csv'
    wnba_team_file = 'wnba_team_salaries_2024.csv'
    output_nba_team_file = 'cleaned_data/top_12_nba_team_salaries_2024.csv'
    output_wnba_team_file = 'cleaned_data/top_12_wnba_team_salaries_2024.csv'

    # Execute the cleaning and processing function for player salaries
    clean_and_extract_top_salaries(nba_player_file, wnba_player_file, output_nba_player_file, output_wnba_player_file)

    # Execute the cleaning and processing function for team salaries
    clean_and_extract_top_team_salaries(nba_team_file, wnba_team_file, output_nba_team_file, output_wnba_team_file)