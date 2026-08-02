matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
target=8
bottom=0
flag = False
top=len(matrix)-1
while bottom<=top:
    mid=(top+bottom)//2
    if  matrix[mid][0]<=target<=matrix[mid][-1]:
        left=0
        right=len(matrix[mid])-1
        while left<=right:
            mid1=(left+right)//2
            if matrix[mid][mid1]==target:
                flag=True
                break
            elif matrix[mid][mid1]<target:
                left=mid1+1
            else:
                right=mid1-1
        break
    elif target>matrix[mid][-1]:
        bottom=mid+1
    elif target<matrix[mid][0]:
        top=mid-1
        
if flag:
    print(flag)
else:
    print(flag)