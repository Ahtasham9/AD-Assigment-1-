import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("mlb_elo_latest.csv")

# 1. Line Plot


def create_elo_ratings_line_plot(data):
    """
    Create a line plot to visualize Elo ratings of the home and away teams over time.

    Args:
        data (DataFrame): Pandas DataFrame containing the dataset.

    Returns:
        None
    """
    data['date'] = pd.to_datetime(data['date'])
    data = data.sort_values(by='date')

    plt.figure(figsize=(12, 6))
    plt.plot(data['date'], data['elo1_pre'],
             label='Home Team Elo Rating', color='blue')
    plt.plot(data['date'], data['elo2_pre'],
             label='Away Team Elo Rating', color='red')
    plt.xlabel('Date')
    plt.ylabel('Elo Rating')
    plt.title('Elo Ratings Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()


create_elo_ratings_line_plot(df)


# 2. Scatter Plot

def create_elo_ratings_scatter_plot(data):
    """
    Create a scatter plot to compare Elo ratings of home and away teams before games.

    Args:
        data (DataFrame): Pandas DataFrame containing the dataset.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(data['elo1_pre'], data['elo2_pre'], alpha=0.5)
    plt.xlabel('Home Team Elo Rating (Pre-game)')
    plt.ylabel('Away Team Elo Rating (Pre-game)')
    plt.title('Elo Ratings Comparison Before Games')
    plt.grid(True)
    plt.show()


create_elo_ratings_scatter_plot(df)


# 3. Histogram

def create_elo_probabilities_histogram(data):
    """
    Create a histogram to visualize the distribution of Elo rating probabilities for the home team.

    Args:
        data (DataFrame): Pandas DataFrame containing the dataset.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    plt.hist(data['elo_prob1'], bins=20, edgecolor='k')
    plt.xlabel('Elo Probability for Home Team')
    plt.ylabel('Frequency')
    plt.title('Distribution of Elo Rating Probabilities for Home Team')
    plt.grid(True)
    plt.show()


create_elo_probabilities_histogram(df)
