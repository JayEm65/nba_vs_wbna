# 🏀 NBA vs WNBA: Salaries and Player Efficiency Ratings 🏀

## 📖 Introduction
This project compares the salaries and Player Efficiency Ratings (PER) of players in the NBA and WNBA. By scraping data from various sports websites and performing thorough data cleaning and analysis, we aim to identify patterns, variances, and insights between the two leagues. We also came up with our own player efficiency rating (PER) for further analysis.

## 🌐 Data Sources
Data was collected exclusively through web scraping from the following sources:

- **NBA Player Salaries**: [HoopsHype NBA Player Salaries](https://hoopshype.com/salaries/players/2023-2024/)
- **WNBA Player Salaries**: [Her Hoop Stats WNBA Player Salaries](https://herhoopstats.com/salary-cap-sheet/wnba/players/salary_2024/stats_2024/)
- **NBA Team Salaries**: [HoopsHype NBA Team Salaries](https://hoopshype.com/salaries/2023-2024/)
- **WNBA Team Salaries**: [Her Hoop Stats WNBA Team Salaries](https://herhoopstats.com/salary-cap-sheet/wnba/summary/2024/)
- **WNBA Offensive PER**: [Her Hoop Stats WNBA Offensive PER](https://herhoopstats.com/salary-cap-sheet/wnba/players/salary_2024/stats_2024/)
- **WNBA Defensive PER**: [Her Hoop Stats WNBA Defensive PER](https://herhoopstats.com/salary-cap-sheet/wnba/players/salary_2024/stats_2024/)

### ⚡ Main Challenges
- **Data Availability**: Unlike APIs and structured datasets, the data from web scraping can be less structured, requiring initial exploration and validation.
- **Web Scraping Complexity**: Handling dynamic content, avoiding scraping limitations, and ensuring ethical scraping practices.
- **Data Cleaning**: Dealing with missing values, duplicated entries, and inconsistent data formats across different sources.

## 🎯 Project Hypotheses
1. **Salary Disparity**: NBA player salaries are significantly higher than WNBA player salaries.
2. **PER Correlation**: Higher-paid players in both leagues (NBA and WNBA) exhibit better performance efficiency ratings.

## 🛠️ Methodology

### Data Collection
Data was scraped using custom Python scripts contained in the `/data_extraction` directory.

1. **NBA Player and Team Salaries**
   - Extracted using functions: `extract_nba_player_salaries` and `extract_nba_team_salaries`
2. **WNBA Player and Team Salaries**
   - Extracted using functions: `extract_wnba_player_salaries` and `extract_wnba_team_salaries`
3. **WNBA Offensive and Defensive PER**
   - Extracted and calculated using functions: `calculate_and_save_offensive_per` and `calculate_and_save_defensive_per`

### PER Calculation
We devised our own methodology to calculate Player Efficiency Ratings (PER) for further analysis:

- **NBA Offensive PER (O-PER)**:
  - Formula: `(PTS + AST + ORB) / 3`
  - Data Collected in: `nba_top_50_offensive_per.csv`

- **NBA Defensive PER (D-PER)**:
  - Formula: `(DRB + BLK + STL) / 3`
  - Data Collected in: `nba_top_50_defensive_per.csv`

- **WNBA Offensive PER (O-PER)**:
  - Formula: `(PTS + AST + ORB) / 3`
  - Data Collected in: `wnba_top_50_offensive_per.csv`

- **WNBA Defensive PER (D-PER)**:
  - Formula: `(DRB + BLK + STL) / 3`
  - Data Collected in: `wnba_top_50_defensive_per.csv`

### Data Cleaning
Initial raw data was scraped into CSV files located within the `extracted_data` directory. Cleaning steps included:
- Handling null values
- Removing duplicates
- String manipulation
- Formatting data fields

Cleaned data is stored in the `cleaned_data` directory.

Main cleaning functions:
- `cleaning.py`
- `clean_salaries.py`
- `clean_per.py`

### Data Analysis & Exploratory Data Analysis (EDA)
Post-cleaning involved EDA to:
- Validate hypotheses
- Apply aggregation and filtering techniques
- Create visualizations

## 📊 Results and Insights
Through data analysis, the following conclusions were drawn:
- **Salary Disparity Confirmed**: NBA player salaries are significantly higher than WNBA player salaries.
- **PER Analysis**: Players with higher salaries generally have higher PER in both leagues.

## ❓ Potential Further Questions [PENDING]
- How do external factors (like media coverage, sponsorship deals) influence player salaries in the NBA vs WNBA?
- What are the trends in rookie salaries and how do they progress compared to veteran players in both leagues?

## 📁 Project Structure & Code Organization

### Data Extraction
- `data_extraction/nba.py`: Functions for extracting NBA data.
- `data_extraction/wnba.py`: Functions for extracting WNBA data.
- `data_extraction/_offensive_per_wnba.py`: Functions for scraping and calculating WNBA Offensive PER.
- `data_extraction/_defensive_per_wnba.py`: Functions for scraping and calculating WNBA Defensive PER.
- `data_extraction/_nba_per.py`: Functions for scraping and calculating NBA PER.

### Data Cleaning
- `data_processing/clean_salaries.py`: Functions for cleaning and processing player and team salaries.
- `data_processing/clean_per.py`: Functions for cleaning and processing PER data.

## 📊 Exploratory Data Analysis (EDA)
The exploratory data analysis methods used include:
- **Aggregation**: Grouping data by specific attributes to find overall trends.
- **Filtering**: Narrowing down data sets based on specific criteria to find relevant insights.
- **Visualizations**: Plots and graphs to visually represent data patterns. [PENDING]

## 📜 Results and Insights
Through data analysis, the following conclusions were drawn:
- **Salary Disparity Confirmed**: NBA player salaries are significantly higher than WNBA player salaries.
- **PER Analysis**: Players with higher salaries generally have higher PER in both leagues.

## 🌐 Project Links
- **GitHub Repository**: [nba_vs_wbna](https://github.com/JayEm65/nba_vs_wbna)
- **Kanban Board (Trello)**: [nba_vs_wbna](https://trello.com/invite/b/66f17e6d34052ca7fb8f2717/ATTIf20786f2f20fdaefd4b69f6c1c1345a043BEF9CA/nbavswbna)

## 🎨 Presentation
The findings of this project are presented in an online slide format:
- **Presentation Slides**: [PLACEHOLDER](PLACEHOLDER)

## 👥 Team
- **Emmanuel Aron**
- **Marc Jahnert**

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🛠️ Setup
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/JayEm65/nba_vs_wbna.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd nba_vs_wbna
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the data extraction and cleaning scripts**:
    ```sh
    python main.py
    ```

---