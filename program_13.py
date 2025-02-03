def bitintomb(a):
    x=a/1024
    y=x/1024
    z=y/1024
    print("kb:", x)
    print("mb:", y)
    print("gb:", z)

a=int(input("Enter bits:"))
bitintomb(a)