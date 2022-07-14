# # # ga= list(map(int, input().rstrip().split()))

# # w = int(input())
# # p = int(input())
# # tw = int(input())
# # tp= int(input())
# # counttw=0
# # counttp=0

# # if tw%w == 0:
# #     counttw = tw//w
# # else:
# #     counttw = (tw//w)+1
# # if tp%p == 0:
# #     counttp = tp//p

# # else:
# #     counttp= (tp//p)+1

# # print(counttw+counttp)


# def Pattern(N):
#   #Enter your code here
#   counth=0
#   countv=0
#   j=0
#   l=[]
#   c=0
#   for i in range(N*N+1):
#     j=i
#     # print(counth)
#     l.append(counth)
#     # print(l)
#     counth+=4
#     if i%N==0 and i!=0:
#         c+=1
#         if l[0]==0:
#             l.pop()
#         print(" ".join(map(str, l)))#for changing list to digit [1,2]=>1 2

#         j=0
#         l=[]
#         counth=0

#         counth+=6*c
# Pattern(5)
def distributingMoney(x, y, z, k):

    l = []
    l.append(x)
    l.append(y)
    l.append(z)
    maxx = max(l)
    print(maxx, 'maxxx')
    for j in l:
        if j==maxx:
            l.remove(j)
    # c=l.index(maxx)
    print(l)
    # del l[c]
    print(l)
    for i in l:
        print(i,'i')

        xwala = maxx-i
        print(xwala,'xawa')
        # print()
        k = k-xwala
        print(k,'k')
    if k == 0:
        return 1
    else:
        return 0

       # Enter your code here
print(distributingMoney(1, 2, 3, 3))
