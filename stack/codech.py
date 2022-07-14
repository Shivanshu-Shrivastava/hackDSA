def rem( arr):
        # code here 
        for i in arr:
            count = arr.count(i)

            ind = arr.index(i)
            print(count,ind,'coun,inde')
            if count>2:
                arr.pop(ind)
                print(arr,'ar')
        return arr
print(rem([1,2,3,2,5,7,2,6]))