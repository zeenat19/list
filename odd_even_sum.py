list1=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum_even=0
sum_odd=0
for i in list1:
    if i%2==0:
        print(i,"even num")
        sum_even=sum_even+i
    else:
        print(i,"odd num")
        sum_odd=sum_odd+i
    i=i+1
print("even ka sum",sum_even,"odd ka sum",sum_odd)