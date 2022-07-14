l= list(map(int, input().rstrip().split()))
# l.index()
# dictt = {k: v for v, k in enumerate(l)}
# print('div',dictt)
# if l==sorted(l,reverse=True):
#     print(0)
# l=sorted(l)
# print('sor',l)
# left=0
# right=len(l)-1
# while left<right:
#     if l[left]<l[right]:
#         if dictt[l[left]]<dictt[l[right]]:
#             print('left',dictt[l[left]])
#             print('right',dictt[l[right]])
#             print(l[right]-l[left])
#             break
#         else:
#             right-=1
#     if left==right:
#         right=len(l)-1
#         left+=1
def ch(l):
    x= min(l)
    ind = l.index(x)
    newl= l[ind:]
    print(newl)
    print(len(newl))
    if len(newl)==1:
        return 0
    y=max(newl)
    pr=y-x
    return pr
print(ch(l))





