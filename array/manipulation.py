from datetime import datetime
x= []
ga= list(map(int, input().rstrip().split()))

p= ga[0]
t= ga[1]
for i in range(p):
    x.append(0)
start = datetime.now()

for j in range(t):
    findar= list(map(int, input().rstrip().split()))

    a= findar[0]
    a-=1
    b= findar[1]
    b-=1
    k= findar[2]
    for l in range(a,b+1):
        qw= x[l]
        qw+=k
        x[l]= qw
        # print('x--',x)
end = datetime.now()

time_taken = end - start
print(max(x))
print('Time: ',time_taken) 




    
