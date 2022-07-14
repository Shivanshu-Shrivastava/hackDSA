nums1= list(map(int, input().rstrip().split()))
nums2= list(map(int, input().rstrip().split()))
m=int(input())
n=int(input())

nums1a= nums1[0:m]
nums2b = nums2[0:n]
new = nums1a+nums2b
nums1 = sorted(new)
print(nums1)