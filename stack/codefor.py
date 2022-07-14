
import math
# print(math.gcd(15,6))
x=int(input())
y=list(map(int, input().rstrip().split()))
def che(l):
    count=0
    i=0
    j=len(l)-1
    tem =list(l)
    if l!=[]:
        if 1 not in tem:
            count+=1
            tem+=[1]



    while i!=len(l)-1:
        # print(l,'l')
        # print(tem,'tem')
        gcd = math.gcd(l[i],l[j])
        # print(l[i],l[j])

        if gcd not in tem:
            tem+=[gcd]
            count+=1
        j-=1
        if i==j:
            
            j=len(l)-1
            i+=1
        
            
    return count
che(y)