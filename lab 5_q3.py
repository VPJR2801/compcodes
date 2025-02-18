import random
a=[]
for i in range(50):
    a.append(random.randrange(1,30))
print(a)

b=[]
for i in a:
    if i not in b:
        b.append(i)

print(b)        
