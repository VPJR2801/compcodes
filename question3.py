names=set()
#adding the names
names.add("Messi")
names.add("Ronaldo")
names.add("Neymar")
names.add("Modric")
names.add("Mbappe")
print("The original set:", names)
#modifying one name
names.discard("Mbappe")
names.add("Vishwa")
print("The set after modifying one name", names)
#delete two name
names.add("Messi")
names.add("Ronaldo")
print("The set after deleting two names is :", names)

