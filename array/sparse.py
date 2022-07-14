s= int(input())
stli =[]
for i in range(s):
    x= input()
    stli.append(x)


q= int(input())
quli =[]
for i in range(q):
    x= input()
    quli.append(x)

def check(st):
    count=0
    for i in stli:
        if i==st:
            count+=1
    return count
sho =[]
for j in quli:
    x= check(j)
    sho.append(x)
for k in sho:
    print(k)


# print(stli,quli)