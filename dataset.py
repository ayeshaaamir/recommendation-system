# google colab
from google.colab import files
uploaded=files.upload()
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import io
df2=pd.read_csv(io.BytesIO(uploaded['links.csv']))
df2=pd.read_csv(io.BytesIO(uploaded['movies.csv']))
df2=pd.read_csv(io.BytesIO(uploaded['ratings.csv']))
df2=pd.read_csv(io.BytesIO(uploaded['tags.csv']))
ratings=pd.read_csv("ratings.csv")
ratings

# jupyter
