def isBalanced(s):
    # Write your code here
    l=[]
    for i in s:
        l.append(i)
    if not len(l)%2==0:
        return 'NO'
    else:
        for j in range(len(l)//2):
            x=l.pop(0)
            y=l.pop()
            # print(x,y,'x,y')
            if x == '{' and y != '}' or x=='[' and y!=']' or x=='(' and y!=')'  :
                return 'NO'
        return 'YES'
x=input('bracke')
print(isBalanced(x))