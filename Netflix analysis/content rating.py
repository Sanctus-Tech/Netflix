
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



# Create a pivot table for ratings over years
rating_year = netflix_df.pivot_table(index='release_year', columns='rating', values='show_id', aggfunc='count', fill_value=0)

# Plot the trend
plt.figure(figsize=(14, 8))
sns.heatmap(rating_year, cmap='YlOrRd', linewidths=0.5)
plt.title('Content Rating Trends Over Years', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Release Year', fontsize=12)
plt.show()

