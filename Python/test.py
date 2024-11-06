dict1 = {"key1": 2, "key2":3,"key3":4,"key4":5}
dict2 = {"key1": 2, "key2":3,"key5":4,"key6":5}

def dict_difference(dict1, dict2):
    result = dict()
    for k,v in dict1:
          if k not in dict2:
               result.update({k:v})

    return result

print(dict_difference(dict1,dict2))