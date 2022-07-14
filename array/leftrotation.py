# h = int(input('how'))
# r= int(input('ro'))
p =list(map(int, input().rstrip().split()))

r=p[1]
pl= list(map(int, input().rstrip().split()))
li = []
for i in range(r):
    x= pl.pop(0)
    # print('x------',x)
    # print('1----',pl)
    pl.append(x)
    # print('2----------',pl)
    # li.append(pl.pop(-1))
    # print('pl==',pl)
print(" ".join(map(str, pl)))


