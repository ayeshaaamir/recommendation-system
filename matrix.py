def sequenced(row):
  new_row=(row-row.mean())/(row.max()-row.min())
  return new_row
ratings_seq=ratings.apply(sequenced)
#create similarity matrix
item_similarity=cosine_similarity(ratings_seq.T)
print(item_similarity)

