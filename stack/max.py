def SillyNumber(N):
    i=1
    p=0
    if p>N:
        return p

    p=i*i+SillyNumber(i+1)
  
  #Enter your code here
print(SillyNumber(21))