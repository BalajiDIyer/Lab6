def encode(pw):
    epw = ''
    for val in pw:
        nval = int(val) + 3
        if nval >=10:
            nval = nval-10
        nval = str(nval)
        epw += nval
    return epw
pw = str(input('Enter Number:'))

print(encode(pw))





def decode(encoded):
    password = ""
    for x in range (0, len(encoded)):
        if encoded[x]== "2":
            password += "9"
        elif encoded[x] == "1":
            password += "8"
        elif encoded[x] == "0":
            password += "7"
        else:
            password += str(int(encoded[x]) - 3)
    return password
