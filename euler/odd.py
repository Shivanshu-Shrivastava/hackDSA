# count =0

# for i in range(1,500):
#     t=(i*(i+1))/2
#     p=(i*(3*1 - 1))/2
#     h=i*(2*i - 1)
#     if t==p and p==h and t==h :
#         count+=1
#     if count ==2 :
#         print(t)
#         break  
    
# http://radiusofcircle.blogspot.com

# time module
import time

# time at the star of program execution
start = time.time()


def is_pentagonal(p):
    """function to check if the
    given number is pentagonal"""
    if (1+(24*p+1)**0.5) % 6 == 0:
        return True
    return False


def is_hexagonal(h):
    """function to check if the
    given number is hexagonal"""
    if (1+(8*h+1)**0.5) % 4 == 0:
        return True
    return False

# iterator start after 285
i = 286

# while loop for iterating
while True:
    triangle = i*(i+1)/2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print (triangle)
        break
    i += 1

# time at the end of program execution
end = time.time()

# total time taken for execution
print (end - start)
