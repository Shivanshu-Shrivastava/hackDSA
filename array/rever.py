t = int(input('re'))
x= list(map(int, input().rstrip().split()))
r=[]
for i in range(t):
    r.append(x.pop())
print(" ".join(map(str, r)))
