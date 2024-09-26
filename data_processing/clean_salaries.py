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

if __name__ == "__main__":
    # Paths to the input and output files
    nba_file = 'nba_player_salaries_2024.csv'
    wnba_file = 'wnba_player_salaries_2024.csv'
    output_nba_file = 'cleaned_data/top_150_nba_player_salaries_2024.csv'
    output_wnba_file = 'cleaned_data/top_150_wnba_player_salaries_2024.csv'

    # Execute the cleaning and processing function
    clean_and_extract_top_salaries(nba_file, wnba_file, output_nba_file, output_wnba_file)