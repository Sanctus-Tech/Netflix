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
# Create a pivot table of content types by year
content_year = netflix_df.pivot_table(index='release_year', columns='type', values='show_id', aggfunc='count', fill_value=0)

# Calculate percentages
content_year['Total'] = content_year['Movie'] + content_year['TV Show']
content_year['Movie %'] = (content_year['Movie'] / content_year['Total']) * 100
content_year['TV Show %'] = (content_year['TV Show'] / content_year['Total']) * 100

# Plot the trend
plt.figure(figsize=(14, 6))
sns.lineplot(data=content_year, x=content_year.index, y='Movie', label='Movies')
sns.lineplot(data=content_year, x=content_year.index, y='TV Show', label='TV Shows')
plt.title('Content Type Growth Over Time', fontsize=16)
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.legend()
plt.show()

