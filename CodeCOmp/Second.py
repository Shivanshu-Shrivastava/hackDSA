from itertools import permutations
ga= list(map(int, input().rstrip().split()))
def arr(ga):
    so =sorted(ga,reverse=True)
    if ga == so:
        return ga
    else:
        i=0
        j=1
        while j<len(ga):
            if ga[i]<ga[j]:
                ga[i],ga[j]=ga[j],ga[i]
                return ga
            i+=1
            j+=1
print(arr(ga))
            

