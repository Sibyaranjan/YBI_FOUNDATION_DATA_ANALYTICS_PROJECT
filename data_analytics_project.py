# -*- coding: utf-8 -*-
"""Data analytics project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uMaCw0pqHG1QM0lsqFq5yFxPKNn9xeMk

TITLE OF THE PROJECT:-MOVIE RECOMMENDATION SYSTEM

OBJECTIVE:-THE OBJECTIVE IS THAT TO PROVIDE RECOMMENDATION BASED MOVIE ON THE USER PREFERENCE.

DATA SOURCE:-TAKEN THE DATA FROM YBI FOUNDATION GITHUB DATASET AND YBI FOUNDATION YOUTUBE CHANNEL

IMPORT LIBRARY
"""

import pandas as pd

import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv')

df.head()

df.info()

df.shape

df.columns

df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline', 'Movie_Cast', 'Movie_Director']].fillna('')

df_features.shape

df_features

x = df_features['Movie_Genre']+ ' ' + df_features['Movie_Keywords']+ ' ' +df_features['Movie_Tagline']+' ' +df_features['Movie_Cast']+' '+df_features['Movie_Director']

x

x.shape

from sklearn.feature_extraction . text import TfidfVectorizer

tfidf= TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

from sklearn.metrics.pairwise import cosine_similarity

similarity_score = cosine_similarity(x)

similarity_score

similarity_score.shape

Favourite_Movie_Name = input('Enter your favourite movie name :-')

All_Movies_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name,All_Movies_Title_List)
print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]
print(Close_Match)

Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

Recommendation_Score = list(enumerate(similarity_score[Index_of_Close_Match_Movie]))
print(Recommendation_Score)

len(Recommendation_Score)

Sorted_similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
print(Sorted_similar_movies)

print('Top 30 Movies Suggested for You :- \n')

i = 1

for movie in Sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if(i<31):
    print(i, ':-',title_from_index)
    i+=1

Movie_Name = input('Enter your favourite movie name :-')

list_of_all_titles = df['Movie_Title']. tolist()

Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)

Close_Match = Find_Close_Match[0]

Index_of_movie = df[df.Movie_Title==Close_Match]['Movie_ID'].values[0]

Recommendation_Score = list(enumerate(similarity_score[Index_of_Close_Match_Movie]))

Sorted_similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)

print('Top 10 Movies Suggested for You :- \n')

i=1

for movie in Sorted_similar_movies:
  index= movie[0]
  title_from_index= df[df.Movie_ID==index]['Movie_Title'].values
  if(i<11):
    print(i, ':-', title_from_index)
    i+=1