def find_first(nums, target):
    left=0
    right=len(nums)-1
    first=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            first=mid
            right=mid-1
        elif nums[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return first
def find_last(nums,target):
    left=0
    right=len(nums)-1
    last=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            last=mid
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return last


    
first=find_first(nums = [1,2,2,2,3],target=2)
last=find_last(nums = [1,2,2,2,3],target=2)
print([first,last])

