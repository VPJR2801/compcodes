m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
total = m1 + m2 + m3
average = total / 3
print(f"Total: {total}, Average: {average:.2f}")
if m1 <= 39 or m2 <= 39 or m3 <= 39:
    print("Result: Fail")
else:
    print("Result: Pass")
ranges = [0, 39, 44, 49, 54, 59, 69, 79, 100]
grades = ["NA", "F", "P", "C", "B", "B+", "A", "A+", "O"]
for i, mark in enumerate([m1, m2, m3], start=1):
    for j, r in enumerate(ranges):
        if mark <= r:
            grade = grades[j]
            break
    print(f"Subject {i}: Marks = {mark}, Grade = {grade}")