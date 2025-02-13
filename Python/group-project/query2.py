import csv
import pickle

names_genres_dict = dict()
genre_stats = dict()
result_dict = dict()


with open("genres_table.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)
   
    for row in reader:
        genre = row['genres']
        id = row['id']
       
        if id not in names_genres_dict:
            names_genres_dict[id] = {"genre/s":[genre], "keyword/s":0}
        else:
            names_genres_dict[id]["genre/s"].append(genre)
    
        
with open("keywords_table.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        id = row['id']
        keyword = row['keywords']
        
        if id not in names_genres_dict:
            names_genres_dict[id] = {"genre/s": [], "keyword/s": 1}
        else:
            names_genres_dict[id]["keyword/s"] += 1



for movie_data in names_genres_dict.values():
    genres = movie_data["genre/s"]
    keywords = movie_data["keyword/s"]
    
    for genre in genres:
        if genre not in genre_stats:
            genre_stats[genre] = {"movie_count": 0, "total_keywords": 0}
        
        # Update stats for the genre
        genre_stats[genre]["movie_count"] += 1
        genre_stats[genre]["total_keywords"] += keywords

# Compute average keywords per movie for each genre


   

with open("query2.pkl", "wb") as f:
    for genre, stats in genre_stats.items():
        result_dict[genre] = round(stats["total_keywords"] / stats["movie_count"], 1)
    pickle.dump(result_dict, f)

    
print("Names_genres_dict:")
print(names_genres_dict)
print("genre_stats:")
print(genre_stats)
print("result_dict:")
print(result_dict)