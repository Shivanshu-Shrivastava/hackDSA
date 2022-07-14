s= input()
for i in s:
    if i == 'P':
        a= int(s[0]+s[1])
        if a==12:
            print(str(a)+s[2:8])
        else:
            a+=12
            print(str(a)+s[2:8])
    if i == 'A':
        a= int(s[0]+s[1])
        if a== 12:
            a-=12
        if a//10 == 0:
            print('0'+str(a)+s[2:8])
        else:

            print(str(a)+s[2:8])

