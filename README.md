NBA vs WNBA: Salaries and Player Efficiency Ratings
Introduction
This project compares the salaries and Player Efficiency Ratings (PER) of players in the NBA and WNBA. By scraping data from various sports websites and performing thorough data cleaning and analysis, we aim to identify patterns, variances, and insights between the two leagues.

Data Sources
Data was collected exclusively through web scraping from the following sources:

NBA Player Salaries: [HoopsHype NBA Player Salaries](https://hoopshype.com/salaries/players/2023-2024/)
WNBA Player Salaries: [Her Hoop Stats WNBA Player Salaries](https://herhoopstats.com/salary-cap-sheet/wnba/players/)
NBA Team Salaries: [HoopsHype NBA Team Salaries](https://hoopshype.com/salaries/2023-2024/)
WNBA Team Salaries: [Her Hoop Stats WNBA Team Salaries](https://herhoopstats.com/salary-cap-sheet/wnba/summary/2024/)
WNBA Offensive PER: [Her Hoop Stats WNBA Offensive PER](https://herhoopstats.com/salary-cap-sheet/wnba/players/)
WNBA Defensive PER: [Her Hoop Stats WNBA Defensive PER](https://herhoopstats.com/salary-cap-sheet/wnba/players/)
Main Challenges
Data Availability: Unlike APIs and structured datasets, the data from web scraping can be less structured, requiring initial exploration and validation.
Web Scraping Complexity: Handling dynamic content, avoiding scraping limitations, and ensuring ethical scraping practices.
Data Cleaning: Dealing with missing values, duplicated entries, and inconsistent data formats across different sources.
Project Hypotheses
Salary Disparity: NBA player salaries are significantly higher than WNBA player salaries.
PER Correlation: Higher-paid players in both leagues (NBA and WNBA) exhibit better performance efficiency ratings.
Methodology
Data Collection
Data was scraped using custom Python scripts. The scripts are contained in the /data_extraction directory.

NBA Player and Team Salaries
Extracted using functions: extract_nba_player_salaries and extract_nba_team_salaries
WNBA Player and Team Salaries
Extracted using functions: extract_wnba_player_salaries and extract_wnba_team_salaries
WNBA Offensive and Defensive PER
Extracted and calculated using functions: calculate_and_save_offensive_per and calculate_and_save_defensive_per
Data Cleaning
Raw data was scraped into CSV files located within the extracted_data directory. Cleaning steps included:

Handling null values
Removing duplicates
String manipulation
Formatting data fields
Cleaned data is stored in the cleaned_data directory.

Main cleaning functions:

cleaning.py
clean_salaries.py
clean_per.py
Data Analysis & Exploratory Data Analysis (EDA)
Post-cleaning involved EDA to:

Validate hypotheses
Apply aggregation and filtering techniques
Create visualizations
Results and Insights
Through data analysis, the following conclusions were drawn:

Salary Disparity Confirmed: NBA player salaries are significantly higher than WNBA player salaries.
PER Analysis: Players with higher salaries generally have higher PER in both leagues.
Further Questions
How do external factors (like media coverage, sponsorship deals) influence player salaries in the NBA vs WNBA?
What are the trends in rookie salaries and how do they progress compared to veteran players in both leagues?
Project Structure & Code Organization
Data Extraction
data_extraction/nba.py: Functions for extracting NBA data.
data_extraction/wnba.py: Functions for extracting WNBA data.
data_extraction/_offensive_per_wnba.py: Functions for scraping and calculating WNBA Offensive PER.
data_extraction/_defensive_per_wnba.py: Functions for scraping and calculating WNBA Defensive PER.
data_extraction/_nba_per.py: Functions for scraping and calculating NBA PER.
Data Cleaning
data_processing/clean_salaries.py: Functions for cleaning and processing player and team salaries.
data_processing/clean_per.py: Functions for cleaning and processing PER data.