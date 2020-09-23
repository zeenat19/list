element=[23,14,12,56,19,9,15,25,31,42,43]
i=0
sum=0
sum1=0
count=0
count1=0
while i<len(element):
    if element[i]%2!=0:
        sum=sum+element[i]
        average=element[i]//7
        count=count+1
    else:
        sum1=sum1+element[i]
        average1=element[i]//4
        count1=count1+1
    i=i+1
print("odd num",count)
print("even num",count1)
print("odd num",sum)
print("even num",sum1)
num=sum+sum1
print("total sum of odd and even num",num)
num=num//11
print("total of odd and even",num)
num = count+count1
print("totoal count of even and odd",num)








