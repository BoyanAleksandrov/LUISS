import csv

result_dict = dict()
names_genres_dict = dict()
test_dict = dict()

with open("genres_table.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        id = row['id']
        result_dict[id] = []



with open("genres_table.csv", mode="r") as csvfile:
    reader = csv.DictReader(csvfile)
   
    for row in reader:
        genre = row['genres']
        id = row['id']
       
        if id not in result_dict:
            result_dict[id] = [genre]
        else:
            result_dict[id].append(genre)
    
        
with open("keywords_table.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id = row['id']
        keyword = row['keywords']
        if id not in names_genres_dict:
            names_genres_dict.setdefault(id, 1)
        else:
            names_genres_dict[id] = names_genres_dict[id] + 1


for el in result_dict.values():
    for val in el:
        if val not in test_dict:
            test_dict.setdefault(val, 0)
for tr in names_genres_dict.keys():
    if tr in result_dict:
        for it in result_dict[tr]:
            if it in test_dict:
                test_dict[it] = test_dict[it] + names_genres_dict[tr]



print(test_dict)