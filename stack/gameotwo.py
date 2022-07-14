
def twoStacks(maxSum, a, b):
    # Write your code here
    count=0
    summ=0
    i=0
    j=0
    while summ<=maxSum:
        af=a[i]
        bf=b[j]
        print(af,bf,'af bf')
        print(count,'count')
        print(summ,'summ')
        if af<bf:
            summ+=af
            count+=1
            i+=1
        else:
            summ+=bf
            count+=1
            j+=1
    return count-1
x=int(input('nnn'))
max=int(input('max'))
for i in range(x):
     a= list(map(int, input('a').rstrip().split()))

     b = list(map(int, input('b').rstrip().split()))
     print(twoStacks(max,a,b))

