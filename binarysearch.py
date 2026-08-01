nums = [-1,0,3,5,9,12]
target = 9
left=0
flag=0
right=len(nums)-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=1
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if flag:
    print(mid)
elif flag==0:
    print(-1)