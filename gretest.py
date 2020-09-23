numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
while i<len(numbers):
    count=numbers[i]
    if count<40 and count>20:
        print(count)
    i=i+1
