list1 = []
list2 = []

for k in range(2, 6) :
    list1= [num for num in range(1,9) if num % k == 0]
    list2.append(list1)
    list1 = []

print(list2)
