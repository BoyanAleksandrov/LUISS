data = {"student1":{"math":75, "science": 82},"student2":{"math":88, "science": 90}}

def update_score(data, student, subject, new_score):
    if student in data.keys():
            data[student][subject] = new_score
    else:
        new_dict = {student:{subject:new_score}}
        data.update(new_dict)
        print(data)

update_score(data, "student4", "maths", 90)