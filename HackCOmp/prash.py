x=int(input())
y=int(input())
count=0
while x != y or x<0 or y<0:
    print('x',x)
    print('y',y)
    if x>y:
        x=x-y
        count+=x
    else:
        y=y-x
        count+=y
    
print(count)


