def togglecase(s):
result=""
for char in s:
    if 'a' <= char <= 'z':
        result += chr(ord(char)-32)
        elif 'A' <= char <='Z':
            result+=chr(ord(char)+32)
            else:
                result+=char
                return result
            def uppercase(s):
                result=""
                for char in s :
                    if'a' <=char <='z':  letter
                    result +=chr(ord(char)-32)
                    else:
                        result+=char
                        return result
                    def lowercase(s):
                        result=""
                        for char in s :
                            if 'A' <= char <= 'Z':
                                result+= char(ord(char)+32)
                                else:
                                    result+=char
                                    return result
                                s=input("Enter a string:")
                                togglecase(s)
                                uppercase(s)
                                lowercase(s)
