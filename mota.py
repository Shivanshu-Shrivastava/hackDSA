def show(n,m,p):
    countO=0
    countE=0
    if m==p:
        return 0
    for i in range(m):
        if not i%2==0:
            countO+=1
        else:
            countE+=1
            
        
        

x=int(input('no'))
for i in range(x):
    l= list(map(int, input().rstrip().split()))
    show(l[0],l[1],l[2])

