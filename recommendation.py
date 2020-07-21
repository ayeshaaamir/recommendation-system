#recommendations
def same_movies(movie_name,user_rating):
  same_score=item_similarity_df[movie_name]*user_rating
  same_score=same_score.sort_values(ascending=False)
  return same_score
print(same_movies("rating",5))
