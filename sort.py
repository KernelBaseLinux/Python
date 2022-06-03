List = [4,5,6,777,888,22,33]
for i in range (7):
    for j in range(i + 1, 7):
        if(List[i] > List[j]):
            temp = List[i]
            List[i] = List[j]
            List[j] = temp

print("Sorted List", List)

assert List == [4, 5, 6, 22, 33, 777, 888]
