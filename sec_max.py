numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=0
i=0
while i<len(numbers):
    if numbers[i]>max:
        max=numbers[i]
    i=i+1
    second_max=0
    j=0
    while j<len(numbers):
        if max>numbers[j] and second_max<numbers[j]:
            second_max=numbers[j]
        j=j+1
print(second_max)