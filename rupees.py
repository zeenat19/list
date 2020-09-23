rupees=[3000,600000,324990909,90990900,5600000,690909090,3101010]
i=0
cororpati=0
lakhpati=0
dilwale=0
while i<len(rupees):
    if rupees[i]<10000000:
        cororpati=cororpati+1
    if rupees[i]>100000:
        lakhpati=lakhpati+1
    else:
        dilwali=dilwale+1
    i=i+1
print(cororpati)
print(lakhpati)
print(dilwali)