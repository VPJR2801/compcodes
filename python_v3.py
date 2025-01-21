def stringinstring(str1,str2):
    if str1 in str2:
        print("One string is present in the other.")
        elif str2 in str1:
            print("One string is present in another")
            else:
                print("One string is not present in the other.")
                string1=input("Enter the first string:")
                string2=input("Enter the second string:")
                stringinstring(string1,string2)
