def binary_search(numbers, target):
    left=0
    right=len(numbers)-1
    while left<=right:
        mid=(left+right)//2
        if numbers[mid]==target:
            return mid
        elif numbers[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1
numbers = [1, 3, 5,7,  9, 11, 13]
target = 7
print(binary_search(numbers,target))