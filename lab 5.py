#lab 5 question 1
import random
a=[]
b=[]
for i in range(5):
    a.append(random.randrange(5,20,2))

print(a)
a.pop(2)

for i in range(4):
    b.append(random.randrange(4,10,2))
print(b)

b.insert(2,a)
print(b)
