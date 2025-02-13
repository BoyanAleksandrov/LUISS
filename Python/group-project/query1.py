import csv # Импортваш си библиотеката
import pickle

name_rating_dict = dict() # Първи речник = Id, Жанрове, Рейтинг на филма
result_dict = dict() # Втори речник = жанр, колко от каква оценка има

with open("movies_table.csv", mode="r") as csvfile: # отваряш movies_table.csv
    reader = csv.DictReader(csvfile) # четеш файла като всяка линия е Dictionary, това ти помага да разделяш колоните по имена: Id, title и други
   
    for row in reader: # четеш ред по ред файла
        rating = float(row['vote_average']) # взимаш рейтинга на филма на тази линия
        id = row['id'] # взимаш id на филма на тази линия
       
        if id not in name_rating_dict: # Ако id не съществува в речника, го добавяш
            name_rating_dict[id] = {"genre/s":[], "rating": [rating]} # структура на речника - "Id": {Жанр,рейтинг}, тук добавяш само рейтинг без жанр
        else: # Ако Id вече съществува
            name_rating_dict[id]["rating"].append(rating) # добавяш рейтинга към съответното Id

with open("genres_table.csv", mode="r") as csvfile: # Отваряш genres_table.csv
    reader = csv.DictReader(csvfile) # четеш файла като всяка линия е Dictionary, това ти помага да разделяш колоните по имена: Id, title и други
   
    for row in reader: # четеш ред по ред от файла
        genre = row['genres'] # взимаш жанра на определения ред
        id = row['id'] # взимаш Id на определения ред
       
        if id not in name_rating_dict: # ако Id не е в речника
            name_rating_dict[id] = {"genre/s":[genre],"rating": []} #инициализираш нова променлива в речника със структура - "Id": {Жанр, рейтинг}, тук добавяш само жанр без рейтинг
        else: # Ако Id вече съшествува
            name_rating_dict[id]["genre/s"].append(genre) # добавяш жанр към съответното Id
        
        if genre not in result_dict: # ако нямаш жанр в result_dict
            result_dict[genre] = {(1, 2):0,(2, 3):0,(3, 4):0,(4, 5):0,(5, 6):0,(6, 7):0,(7, 8):0,(8, 9):0,(9, 10):0} # добавяш жанр в result_dict със структура - {Жанр: 1-2:0,2-3:0,3-4:0...} тук броиш кой жанр колко пъти е получавал съответен рейтинг




for movie_id, details in name_rating_dict.items(): # взимаш movie_id и dictionary от жанрове и рейтинг
    for rating in details['rating']: # взимаш рейтинг
        for genre in details['genre/s']: # взимаш жанр
            for (start, end), count in result_dict[genre].items(): # минаваш през всяка една граница, пример (от 1 до 2, от 2 до 3...)
                if start <= rating < end: # ако рейтинга влиза в границата
                    result_dict[genre][(start, end)] += 1 # бройката на оценката на жанра става +1
         
with open("query1.pkl", "wb") as f:
    pickle.dump(result_dict, f)