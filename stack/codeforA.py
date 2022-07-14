# def ch(a):
#     s=set()
#     l=[]
#     for i in a:
#         if i not in s:
#             s.add(i)
#             l.append(i)
#         else:
#             for j in range(i-1,-1,-1):
#                 if j not in s:
#                     l.append(j)
#                     s.add(j)
#                     break 
#     return " ".join(map(str,l))
# x=int(input())
# for i in range(x):
#     y=int(input())
#     l=list(map(int,input().split()))
#     print(ch(l))

# global t
# t=[-1]*(10**18+1)
# def ch(n):
#     if n==0:
#         t[n]= 0
#     if n==1:
#         t[n]= 1
#     if n==2:
#         t[n]= 6
#     if t[n] !=-1:
#         return t[n]
#     else:
#         t[n]= ((ch(n-1)+2)*2-ch(n-2))
#         return t[n]%(10**9+7) 
# x=int(input())
# for i in range(x):
#     y=int(input())
#     print(ch(y))


from math import gcd
def ch(n):
    a=-1
    b=-1
    ma=float('-inf')
    if n==0 or n%2!=0:
        l=[]
        l.append(a)
        l.append(b)
        return " ".join(map(str,l))
    for i in range(2,n+1,2):
        # print(i)
        if n%i==0:
            A=i
            if n%i==0:
                B=n//i
                if B%2!=0:
                    # print(A,B)
                    ga=gcd(A,B)
                    if ga>=ma:
                        # print(ga,A,B)
                        if ga==ma:
                            ma=ga
                            if A>a:
                                l=[]
                                a=A
                                b=B
                                l.append(A)
                                l.append(B)
                        else:
                            l=[]
                            ma=ga
                            a=A
                            b=B
                            l.append(A)
                            l.append(B)
    return " ".join(map(str,l))
x=int(input())
for i in range(x):
    y=int(input())
    print(ch(y))

