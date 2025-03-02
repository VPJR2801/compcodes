import random
random_numbers={random.randint(15,45) for i in range (11)}
less_than_30={num for num in random_numbers if num<=30}
random_number={num for num in random_numbers if num<35}

print("original set :", random_numbers)
print("Numbers less than 30:", len(less_than_30))
print("The set after removing numbers greater than 35:", random_number)