# KAIM-WEEK1-Stock-market-sentiment-analysis
# News Analysis Project

## Overview
This project focuses on analyzing financial news data to extract insights for traders and automated trading systems. It involves exploratory data analysis (EDA), text processing (sentiment analysis and topic modeling), time series analysis, and quantitative financial analysis using TA-Lib.

---

## Folder Structure
├── .vscode/ │ └── settings.json # VSCode settings for the project ├── .github/ │ └── workflows │ └── unittests.yml # CI/CD workflow for running unit tests ├── .gitignore # Files and directories to ignore in Git ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── src/ │ ├── init.py # Source code files ├── notebooks/ │ ├── init.py # Jupyter notebook initialization │ └── README.md # Notebooks documentation ├── tests/ │ ├── init.py # Unit tests for the project └── scripts/ ├── init.py # Scripts for executing the project tasks └── README.md # Scripts documentation

---

## Installation

1. Clone the repository:
   ```bash
        git clone https://github.com/Elish-Ab/KAIM-WEEK1-Stock-market-sentiment-analysis.git
   ```
2. Navigate to the project directory:
    ```bash
         cd KAIM-WEEK1-Stock-market-sentiment-analysis 

    ```
3. Create a virtual environment:
        
    ```bash
        python -m venv venv
        source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

4. Install dependencies:
    ```bash
        pip install -r requirements.txt
    ```

##Features

    1.Exploratory Data Analysis (EDA):
        Descriptive statistics on textual data.
        Publisher analysis and publication trends.
    2.Sentiment Analysis:
        Analyzing the sentiment (positive, neutral, negative) of headlines.
    3.Topic Modeling:
        Identifying topics using Latent Dirichlet Allocation (LDA).
    4.Time Series Analysis:
        Publication frequency over time and its correlation with market events.
    5.Quantitative Financial Analysis:
        Calculating technical indicators using TA-Lib


## How to Run

    Run EDA and Text Analysis:
    ```bash
        python scripts/main.py
    ```

Ensure the dataset is available in the correct path as specified in the script.

Run Jupyter Notebook for Detailed Analysis:

    jupyter notebook

    Test CI/CD Workflow:
        Push code to GitHub and verify that the unit tests pass successfully.

## Technologies Used

    Python: Data processing and analysis.
    Git and GitHub: Version control and collaboration.
    GitHub Actions: CI/CD automation.
    Pandas: Data manipulation.
    TA-Lib: Technical indicator analysis.
    NLTK & scikit-learn: Sentiment and topic analysis.
    Matplotlib & Seaborn: Data visualization.

Contributing

    Fork the repository.
    Create a new branch for your feature:

git checkout -b feature-branch-name

Commit your changes:
    ```bash
     git commit -m "Describe your changes"
    ```
Push to the branch:
    ```bash
        git push origin feature-branch-name

        Create a pull request.
    ```
License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For questions or feedback, contact:

    Name: Elisha Abriham
    Email: elishabu28@gmail.com
    GitHub: github/Elish-Ab
