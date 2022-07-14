x=int(input())
li=[]
for i in range(x):
     a = input()
     li.append(a)

def chekc(l):
    templ = list(l)
    
    s=''
    rem=''
    apptemp=''
    for i in l:
        # print(templ,'tem')
        # print(l,'l')
        # print(i,'i\n')
        if i[0]=='1':
            # print(i[2:])
            apptemp=i[2:]
            s=s+i[2:]
            # print(s,'s1')
        if i[0]=='2':
            flen = len(s)-int(i[2])
            rem= s[flen:]
            s=s[0:flen]
            # print(s,'s2')

        if i[0]=='3':
            # print(s,'s3')
            
            plen = int(i[2])-1
            
            print(s[plen],'result s3')
        if i[0]=='4':
            ind = l.index(i)-1
            # print(ind,'ind4')
            
            while ind >0:
                
                if templ[ind][0]=='2':
                    # flennn = len(s)-int(i[2])
                    
                    s=s+rem
                    # print(s,'s4')
                    templ.pop(ind)
                    # print(templ,'templ')
                    break
                   
                    # templ.pop(ind)
                    # del(templ[ind])

                    # print(l,'dek')


                    
                if templ[ind][0]=='1':
                    s=s.replace(templ[ind][2:],'')
                    # print(s,'s5')
                    templ.pop(ind)
                    # print(templ)
                    # del(templ[ind])
                    # print(l,'dek')

                    break
                    
             




                ind-=1
chekc(li)




