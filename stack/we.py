def ch(l,x):
    c=0
    for i in range(len(l)):
        if i%2!=0:
            if l[i-1]+l[i]>x:
                if x-l[i-1]>0:
                    l[i]=x-l[i-1]
                    f=1
                if x-l[i-1]<=0:
                    f=0
                    l[i-1]=x-l[i]
                    c+=x-l[i]
                else:
                    c+=x-l[i-1]
            print(l)
            print(i)
            if l[i+1]+l[i]>x:
                if x-l[i+1]>0:
                    l[i]=x-l[i+1]
                if x-l[i+1]<=0:
                    l[i+1]=x-l[i]
                    c+=x-l[i]
                else:
                    c+=x-l[i+1]
    return c



        





    
x=int(input())
for i in range(x):
    
    l=list(map(int,input().rstrip().split()))
    k=list(map(int,input().rstrip().split()))
    print(ch(l,k[1]))