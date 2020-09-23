marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
sum=0
count=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        a=marks[i][j]
        sum=sum+a
        j=j+1
        count=count+1
    i=i+1
print(sum)
    
