import pandas as pd

def clean_and_extract_top_per(nba_file, wnba_file, output_nba_file, output_wnba_file, nba_per_column, wnba_per_column):
    # Load NBA PER CSV
    nba_df = pd.read_csv(nba_file)
    # Drop unnecessary columns and keep only Player and NBA PER columns
    nba_df = nba_df[['Player', nba_per_column]].dropna()
    # Save cleaned NBA PER data to a new CSV
    nba_df.to_csv(output_nba_file, index=False)
    print(f"Cleaned NBA {nba_per_column} data saved to '{output_nba_file}'.")

    # Load WNBA PER CSV
    wnba_df = pd.read_csv(wnba_file)
    # Drop unnecessary columns and keep only Player and WNBA PER columns
    wnba_df = wnba_df[['Player', wnba_per_column]].dropna()
    # Save cleaned WNBA PER data to a new CSV
    wnba_df.to_csv(output_wnba_file, index=False)
    print(f"Cleaned WNBA {nba_per_column} data saved to '{output_wnba_file}'.")

if __name__ == "__main__":
    # Paths to the input and output files for Offensive PER cleaning
    nba_offensive_file = 'extracted_data/nba_top_50_offensive_per.csv'
    wnba_offensive_file = 'extracted_data/wnba_top_50_offensive_per.csv'
    output_nba_offensive_file = 'cleaned_data/c_nba_top_50_offensive_per.csv'
    output_wnba_offensive_file = 'cleaned_data/c_wnba_top_50_offensive_per.csv'

    # Paths to the input and output files for Defensive PER cleaning
    nba_defensive_file = 'extracted_data/nba_top_50_defensive_per.csv'
    wnba_defensive_file = 'extracted_data/wnba_top_50_defensive_per.csv'
    output_nba_defensive_file = 'cleaned_data/c_nba_top_50_defensive_per.csv'
    output_wnba_defensive_file = 'cleaned_data/c_wnba_top_50_defensive_per.csv'

    # Execute the cleaning and processing function for Offensive PER
    clean_and_extract_top_per(nba_offensive_file, wnba_offensive_file, output_nba_offensive_file, output_wnba_offensive_file, 'O_PER', 'O-PER')

    # Execute the cleaning and processing function for Defensive PER
    clean_and_extract_top_per(nba_defensive_file, wnba_defensive_file, output_nba_defensive_file, output_wnba_defensive_file, 'D_PER', 'D-PER')