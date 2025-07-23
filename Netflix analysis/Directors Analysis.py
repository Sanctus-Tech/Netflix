import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter

# Set seaborn style for better visuals
sns.set_style("whitegrid")

# Load the dataset
netflix_df = pd.read_csv(
    r"C:\Users\GABANI\Desktop\data set to work on\Python Project\Netflix\netflix_titles.csv")

# Handle missing values
# Fill missing values in 'director' with 'No Director'

netflix_df['director'] = netflix_df['director'].fillna('No Director')

# Filter out 'No Director' and split directors (some have multiple)
directors = netflix_df[netflix_df['director'] != 'No Director']['director']
all_directors = [director for sublist in directors.str.split(
    ', ') for director in sublist]

# Count director appearances
director_counts = Counter(all_directors).most_common(15)

# Plot top directors
plt.figure(figsize=(14, 6))
sns.barplot(x=[count[1] for count in director_counts],
            y=[count[0] for count in director_counts],
            palette='magma')
plt.title('Top 15 Most Prolific Directors on Netflix', fontsize=16)
plt.xlabel('Number of Titles', fontsize=12)
plt.ylabel('Director', fontsize=12)
plt.show()
