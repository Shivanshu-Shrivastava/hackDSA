n = int(input().strip())
# import math
def find(arr):
    left=0
    right=0
    i=0
    j=len(arr)
    while i<len(arr):
        # print('left',arr[i][i])
        # print('right',arr[i][j-1])
        left+=arr[i][i]
        right+=arr[i][j-1]
        i+=1
        j-=1
    
    
    # print(left)
    # print(right)
    to= abs(left-right)
    print(to)

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
# print(arr)

find(arr)
