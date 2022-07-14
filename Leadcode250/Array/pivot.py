nums= list(map(int, input().rstrip().split()))

left=0
right=len(nums)-1
while left<right:
    mid=len(nums[left:right+1])//2
    print('mid',mid)
    x=sum(nums[left:mid])
    print('x',x)

    y=sum(nums[mid+1:right+1])
    print('y',y)

    if x==y:
        # i = nums.index(mid)
        print('i',mid+1)
        break
    else:
        left+=1
        right-=1
print(0)