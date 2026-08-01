nums=[1,2,2,3,3,3,4]
ds={}
for i in nums:
    if i in ds:
        ds[i]+=1
    else:
        ds[i]=1
ls=[]
for i in ds:
    ls.append((i,ds[i]))
ls.sort(key=lambda x:x[1],reverse=True)
ans=[]
for i in ls[:2]:
    ans.append(i[0])
print(ans)