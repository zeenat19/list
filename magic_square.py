magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
sum=0
sum1=0
for i in range(3):
    for j in range(3):
        if i==j:
            sum=sum+magic_square[i][j]
        if i+j==3-1:
            sum1=sum1+magic_square[i][j]
        if sum!=sum1:
            f1=1
        else:
            for i in range(3):
                sum2=0
                sum3=0
                for j in range(3):
                    sum2=sum2+magic_square[i][j]
                    sum3=sum3+magic_square[i][j]
                    if sum2!=sum:
                        f=1
                    elif sum3!=sum:
                        f=1
                    else:
                        f=0
if f==0:
    print("magic square")
else:
    print("no")
