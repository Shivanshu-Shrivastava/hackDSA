def maxx(arr):
    li=[]
    for i in arr:
        x = arr.count(i)
        if x>=2:
            li.append(i)
    x=list(set(li))
    return ' '.join([str(v) for v in x])
   
        
print(maxx([7,1,5,2,2,2,6,5]))