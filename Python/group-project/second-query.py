import csv
genres = {}
keywords = {}
result = {}
genres_names = set()
with open("movies_table.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        genres[row['id']] = set()

with open("genres_table.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)
   
    for row in reader:
        movie_id = row['id']
        genre = row['genres']
        if movie_id in genres:
            genres[movie_id].add(genre)
        else:
            genres[movie_id] = {genre}
        genres_names.add(genre)

with open("keywords_table.csv", mode="r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_id = row['id']
        keyword = row['keywords']
 
        if movie_id in keywords:
            keywords[movie_id].add(keyword) 
        else:
            keywords[movie_id] = {keyword}





print(genres_names)