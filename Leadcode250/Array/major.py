nums= list(map(int, input().rstrip().split()))
l={}
for i in nums:
    x=nums.count(i)
    l[i]=x
    
print(l)
print(max(l, key=l.get))