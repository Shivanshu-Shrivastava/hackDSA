n= int(input())
lis=[]

for i in range(n):
    j=i
    while j<n:
        if j==n-1:
            lis.append('#')
        else:
            lis.append('')
        j+=1
    if i==n-1:
        print(lis)
        lis=[]



