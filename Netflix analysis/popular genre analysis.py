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




# First, we need to split the listed_in column which contains multiple genres
netflix_df['listed_in'] = netflix_df['listed_in'].apply(lambda x: x.split(', '))

# Create a list of all genres
all_genres = [genre for sublist in netflix_df['listed_in'] for genre in sublist]

# Count genre occurrences
genre_counts = Counter(all_genres).most_common(15)

# Plot the top genres
plt.figure(figsize=(14, 6))
sns.barplot(x=[count[1] for count in genre_counts], 
            y=[count[0] for count in genre_counts], 
            palette='viridis')
plt.title('Top 15 Most Popular Genres on Netflix', fontsize=16)
plt.xlabel('Number of Titles', fontsize=12)
plt.ylabel('Genre', fontsize=12)
plt.show()

