import pickle

with open("query2.pkl", "rb") as f:

    loaded_dict = pickle.load(f)

print(loaded_dict)