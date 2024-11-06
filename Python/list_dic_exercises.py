data = {"student1":{"math":75, "science": 82},"student2":{"math":88, "science": 90}}

def update_score(data, student, subject, new_score):
    if student in data.keys():
            data[student][subject] = new_score
    else:
        new_dict = {student:{subject:new_score}}
        data.update(new_dict)
        print(data)

update_score(data, "student4", "maths", 90)

data2 = {"apple":10, "iphone": 20, "kettle": 5}
def filter_above_threshold(d, threshold):
    result = dict()
    for k,v in d.items():
          if v > threshold:
               result.update({k:v})
    
    print(result)

filter_above_threshold(data2,5)

data3 = [{1,2,3}, {2,3,4}, {4,5}]

def extract_unique_elements(data4):
    result = set()
    for element in data4:
          for el in element:
               result.add(el)
    return result

print(extract_unique_elements(data3))

dict1 = {"key1": 2, "key2":3,"key3":4,"key4":5}
dict2 = {"key1": 2, "key2":3,"key5":4,"key6":5}

def dict_difference(dict1, dict2):
    result = dict()
    for k, v in dict1.items(): 
        if k not in dict2:
            result.update({k: v})
    for k, v in dict2.items(): 
        if k not in dict1:
            result.update({k: v})
    return result




print(dict_difference(dict1,dict2))