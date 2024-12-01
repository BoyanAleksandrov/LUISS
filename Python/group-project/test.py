import pickle

with open("second_query.pkl", "rb") as f:

    loaded_dict = pickle.load(f)

print(loaded_dict)