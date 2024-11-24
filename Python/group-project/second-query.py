import csv
movies = {}

with open("movies_table.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        movies.update({row['id']: None})

print(movies)
