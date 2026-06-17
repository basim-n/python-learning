def selection_sort(numbers):
    for i in range(0,len(numbers)):
        smallest=numbers[i]
        position=i
        for j in range(i,len(numbers)):
            
            if numbers[j]<smallest:
                smallest=numbers[j]
                position=j

        numbers[i],numbers[position]=numbers[position],numbers[i]
    return numbers
numbers = [2,7,5,9,3]
print(selection_sort(numbers))