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

# Fill missing country values
netflix_df['country'] = netflix_df['country'].fillna('No Country')

# 1. Countries producing the most content
countries = netflix_df[netflix_df['country'] != 'No Country']['country']
all_countries = [country for sublist in countries.str.split(', ') for country in sublist]
country_counts = Counter(all_countries).most_common(15)

plt.figure(figsize=(14, 6))
sns.barplot(x=[count[1] for count in country_counts], 
            y=[count[0] for count in country_counts], 
            palette='plasma')
plt.title('Top 15 Countries Producing Netflix Content', fontsize=16)
plt.xlabel('Number of Titles', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.show()

# 2. Duration analysis for movies
movies = netflix_df[netflix_df['type'] == 'Movie'].copy()
movies['duration'] = movies['duration'].str.extract('(\d+)').astype(float)

plt.figure(figsize=(14, 6))
sns.histplot(data=movies, x='duration', bins=30, kde=True)
plt.title('Distribution of Movie Durations (in minutes)', fontsize=16)
plt.xlabel('Duration (minutes)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()

# 3. Seasons analysis for TV shows
tv_shows = netflix_df[netflix_df['type'] == 'TV Show'].copy()
tv_shows['seasons'] = tv_shows['duration'].str.extract('(\d+)').astype(int)

plt.figure(figsize=(14, 6))
sns.countplot(data=tv_shows, x='seasons', palette='coolwarm')
plt.title('Distribution of TV Show Seasons', fontsize=16)
plt.xlabel('Number of Seasons', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()