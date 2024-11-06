s1 = {1,2,3,4,5}
s2 = {6,2,8,9,10}

for element in s1.union(s2):
    print(element)

s3 = {1,2,3,4,5}
s3.add(6)



if 3 in s3:
    s3.remove(3)
else:
    print("7 is not in s3")
print(s3)

s3.discard(1)
s3.update([9,8,"a","b"])

print(s3.pop())
print(s3.pop())
print(s3.pop())