def twosum(a,t):
    # for idx,val in enumerate(a):
    #     if t-val in a:
    #         return val,t-val
    i=0
    j=len(a)-1
    while True:
        if a[i]+a[j]==t:
            return a[i],a[j]
        j-=1
        if i==j:
            i+=1
            j=len(a)-1


print(twosum([1,2,5,4 ,8,3],7))