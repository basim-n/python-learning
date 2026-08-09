nums = [5,4,3,2]
left=0
right=len(nums)-1
while left<right:
    mid=(left+right)//2
    
    if nums[mid]>nums[mid+1]:
        right=mid


    else:
        left=mid+1
print(left)
