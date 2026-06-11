def two_sum(numbers,target):
    left=0
    right=len(numbers)-1
    while left<right:
        if numbers[left] + numbers[right]==target:
            return [left,right]
        elif numbers[left]+numbers[right]>target:
            right-=1
        elif numbers[left]+numbers[right]<target:
            left+=1
    return "There is no such numbers"
numbers = [2, 7, 11, 15]
target = 9
indices= two_sum(numbers,target)
print(indices)