array1 = []
array2 = []
mergedarray = []
# Entering number of elements of first array
a1 = input()
a2 = input()
temp1 = a1.split(" ")
temp2 = a2.split(" ")

if temp1[0][0] == '-' and temp2[0][0] == '-':
    n1 = (int(temp1[0][1:]))
    n2 = (int(temp2[0][1:]))
    n1 = -n1
    n2 = -n2

elif temp1[0][0] == '-' and temp2[0][0] != '-':
    n1 = (int(temp1[0][1:]))
    n2 = (int(temp2[0]))
    n1 = -n1
    for b in range(1,n2+1):
        array2.append(int(temp2[b]))


elif temp2[0][0] == '-' and temp1[0][0] != '-':
    n1 = (int(temp1[0]))
    n2 = (int(temp2[0][1:]))
    n2 = -n2
    for a in range(1,n1+1):
        array1.append(int(temp1[a]))

else:
    n1 = int(temp1[0])
    n2 = int(temp2[0])
    for a in range(1,n1+1):
        array1.append(int(temp1[a]))
    for b in range(1,n2+1):
        array2.append(int(temp2[b]))

if n1>0 and n2>0 and n1<100001 and n2<100001:

    i = 0
    j = 0
    temp = ""

    while i < n1 and j < n2:

        if array1[i] < array2[j]:
            mergedarray.append(array1[i])
            i += 1
        else:
            mergedarray.append(array2[j])
            j += 1

    while i < n1:
            mergedarray.append(array1[i])
            i += 1

    while j < n2:
            mergedarray.append(array2[j])
            j += 1
    s = str(n1+n2) + " "
    for i in range(0,(n1 + n2-1)):
        s += str(mergedarray[i]) + " "
    s = s + str(mergedarray[n2+n1-1])
    print(s)

elif n2>0 and n1<1 and n2<100001:
    i = 0
    temp = str(n2) + " "
    for i in range(0, (n2 - 1)):
        temp += str(array2[i]) + " "
    temp = temp + str(array2[n2 - 1])
    print(temp)

elif n1>0 and n2<1 and n1<100001:
    i = 0
    temp = str(n1) + " "
    for i in range(0, (n1 - 1)):
        temp += str(array1[i]) + " "
    temp = temp + str(array1[n1 - 1])
    print(temp)


else:
    print("")