def first_dupicate(numbers):
    seen={}
    for num in numbers:
        if num in seen:
            return num
        else:
            seen[num]=True
    return -1
numbers=[1,4,1,5,5]
print(first_dupicate(numbers))