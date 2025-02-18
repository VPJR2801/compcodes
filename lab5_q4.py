import random
a,b,c=[],[],[]
for i in range(30):
    a.append(random.randint(-50,50))
print(a)

for i in range(30):
    if a[i]>=0:
       b.append(a[i])
    else:
        c.append(a[i])

print("Positive numbers:",b)
print("Negative numbers:",c)
    
