# **Netflix Content Analysis**  

## **📌 Introduction**  
This project analyzes Netflix's movie and TV show content to uncover trends in ratings, genres, directors, and content types over time. By leveraging data visualization and statistical techniques, exploring what types of content dominate Netflix and how viewer preferences have evolved.  

This analysis helps answer questions like:  
- How have content ratings changed over the years?  
- Which genres and directors are most popular on Netflix?  
- Is Netflix shifting more toward movies or TV shows?  

---

## **📌 Background**  
Netflix has revolutionized the entertainment industry with its vast library of movies and TV shows. Understanding content trends can provide insights into:  
- **Viewer preferences** (what genres and ratings are most common)  
- **Production trends** (how content types and ratings have evolved)  
- **Strategic decisions** (what content performs best, potential gaps)  

This project uses a **Netflix Movies & TV Shows dataset** from Kaggle, containing information on titles, directors, cast, release years, ratings, and genres.  

---

## **📌 Tools & Libraries Used**  
- **Python** (Primary programming language)  
- **Pandas** (Data manipulation and cleaning)  
- **Matplotlib** (Data visualization)  
- **Collections.Counter** (Counting frequent items)  

---

## **📌 Analysis & Key Findings**  

### **1️⃣ Content Rating vs. Release Year**  
- **TV-MA (Mature Audience)** dominates recent years, indicating a shift toward adult-oriented content.  
- **TV-14** and **TV-PG** remain stable, suggesting consistent family-friendly content.  
- **R-rated movies** peaked in the early 2000s but have declined slightly.  

📊 **Visualization:** line plots showing rating trends over time.  

### **2️⃣ Popular Genres & Directors**  
- **Top Genres:**  
  - *International Movies & TV Shows* (most frequent)  
  - *Dramas & Comedies* (consistently popular)  
  - *Documentaries* (growing trend)  
- **Top Directors:**  
  - *Rajiv Chilaka* (most prolific, known for children's content)  
  - *Raúl Campos, Jan Suter* (frequent collaborators in comedy)  

📊 **Visualization:** Bar plots for genres/directors.  

### **3️⃣ Content Type Trend Over Time**  
- **Movies** dominated early Netflix (pre-2015).  
- **TV Shows** have significantly increased since 2016, likely due to Netflix’s investment in original series.  
- Recent years show a **balance between movies and TV shows**.  

📊 **Visualization:** Line plots comparing Movies vs. TV Shows over time.  

---

## **📌 What I Learned**  
✅ **Data Cleaning:** Handling missing values (directors, ratings) and converting date formats.  
✅ **Exploratory Data Analysis (EDA):** Using pivot tables, grouping, and aggregation.  
✅ **Visualization Techniques:** Heatmaps, bar plots, line charts.  
✅ **Trend Identification:** Recognizing shifts in content types and ratings.  

---

## **📌 Conclusion**  
- Netflix has **shifted toward mature (TV-MA) content** in recent years.  
- **International content and dramas** dominate the platform.  
- **TV Shows are growing faster than movies**, likely due to Netflix’s original series strategy.  

This analysis helps content creators, marketers, and data enthusiasts understand Netflix’s content strategy and audience preferences. Future work could include **sentiment analysis on descriptions** or **predictive modeling for content success**.  
