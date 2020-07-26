from google.colab import files
uploaded = files.upload()

import pandas as pd
# getting data
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
path = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
df = pd.read_csv(path, sep='\t', names=column_names) 
# checking head of data
df.head()

# checking movies and their ids
movie_titles = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv') 
movie_titles.head() 

# merging data
data = pd.merge(df, movie_titles, on='item_id') 
data.head() 

# calculating ratings of movies
data.groupby('title')['rating'].mean().sort_values(ascending=False).head() 

# calculating count rating
data.groupby('title')['rating'].count().sort_values(ascending=False).head() 

# creating dataframe with counting ratings of movies
ratings = pd.DataFrame(data.groupby('title')['rating'].mean())  
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
ratings.head() 

# visualizinggg
# importing
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set_style('white') 
%matplotlib inline 

# plotting graph for number of ratingzz
plt.figure(figsize =(10, 4)) 
ratings['num of ratings'].hist(bins = 70) 

# plotting graph for ratingzz
plt.figure(figsize =(10, 4)) 
ratings['rating'].hist(bins = 70) 

# sorting a/c to ratings 
moviemat = data.pivot_table(index ='user_id', 
              columns ='title', values ='rating') 
moviemat.head() 
ratings.sort_values('num of ratings', ascending = False).head(10) 

# analyzing correlation with same movies
starwars_user_ratings = moviemat['Star Wars (1977)'] 
liarliar_user_ratings = moviemat['Liar Liar (1997)'] 
starwars_user_ratings.head() 

# analysing correlation with similar movies 
similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings) 
corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation']) 
corr_starwars.dropna(inplace = True) 
corr_starwars.head() 

# Similar movies like starwars 
corr_starwars.sort_values('Correlation', ascending = False).head(10) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 
corr_starwars.head() 
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head() 

# Similar movies like liarliar 
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation']) 
corr_liarliar.dropna(inplace = True) 
corr_liarliar = corr_liarliar.join(ratings['num of ratings']) 
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head() 

import matplotlib.pyplot as plt
import os
import re
import shutil
import string
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import preprocessing
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
