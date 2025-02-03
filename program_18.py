def area(a,b):
    x=a*b
    print("The area of the rectangle is:", x)
def perameter(a, b):
    x=2*(a+b)
    print("The perameter of the rectangle is:", x)
a=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the width of the rectangle:"))
area(a , b)
perameter(a , b)