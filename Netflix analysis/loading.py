
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

# Set seaborn style for better visuals
sns.set_style("whitegrid")

# Load the dataset
netflix_df = pd.read_csv(r"C:\Users\GABANI\Desktop\data set to work on\Python Project\Netflix\netflix_titles.csv")  


# Handle missing values
netflix_df['director'] = netflix_df['director'].fillna('No Director')
netflix_df['cast'] = netflix_df['cast'].fillna('No Cast')
netflix_df['country'] = netflix_df['country'].fillna('No Country')
netflix_df['rating'] = netflix_df['rating'].fillna(netflix_df['rating'].mode()[0])

# Convert date_added to datetime
netflix_df['date_added'] = pd.to_datetime(
    netflix_df['date_added'],
    format='%B %d, %Y',
    errors='coerce'
)
# Extract year from date_added and release_year
netflix_df['year_added'] = netflix_df['date_added'].dt.year
netflix_df['release_year'] = netflix_df['release_year'].astype(int)

# Create a simplified content type column
netflix_df['type'] = netflix_df['type'].apply(lambda x: 'Movie' if x == 'Movie' else 'TV Show')