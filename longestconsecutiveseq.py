nums=[100,4,200,1,3,2]
st=set(nums)


longest=0
for i in st:
    if i-1 not in st:
        current=i
        length=1
        while current+1 in st:
            current+=1
            length+=1
        longest=max(length,longest)
print(longest)


        

    
