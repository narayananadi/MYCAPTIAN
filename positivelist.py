num = int(input("enter capacity of list : "))
print("insert numbers into the list : ")
list1 = []
for x in range(num):
    list1.append(int(input()))

for x in list1:
    if x >= 0:
        print(x, end=" ")