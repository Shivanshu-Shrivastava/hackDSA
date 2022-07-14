# l= list(map(int, input().rstrip().split()))
# # tar = int(input('t'))
# # i=0
# # j=0
# # while True:
# #     lis= []
# #     if not i==j:
# #         if l[i]+l[j] == tar:
# #             lis.append(i)
# #             lis.append(j)
# #             break
# #         if j == len(l)-1:
# #             j=0
# #             i+=1
# #     j+=1
# # print(lis)    
# nums=[1,2,3,3] 
# # dictt = {k: v for v, k in enumerate(nums)} // {0:1,1:3}
# x=dict(enumerate(nums))
# # x= {enumerate(nums)}
# print(x)

# # print(dictt)
def Pattern(N):
  #Enter your code here
  for i in range(0,N):
      j=i+4
      print(j,end=' ')
Pattern(5)