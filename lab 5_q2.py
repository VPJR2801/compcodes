import random
c=[]
for i in ranges (20):
    c.append(random.randrange(5,35,1))
print(c)

a=int(input(""))
d=0
for i in range (len(c)):
    if c[i]==a:
        d+=1

print("Frequency of number is",d)
