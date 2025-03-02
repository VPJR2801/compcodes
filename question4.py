names={"Aslesh","Bhairav","Abhinav","Ayush","Bheem"}
prefix1="A"
Names_A={i for i in names if i.startswith(prefix1)}
print("The set containing names starting with A", Names_A)
prefix2="B"
Names_B={i for i in names if i.startswith("B")}
print("The set containing names starting with B", Names_B)