list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
a=[]
while i<len(list1):
    if list2[i] in list1:
        print(list2[i],"presnt in list1")
        a.append(list2[i])
    i=i+1
print(a)
