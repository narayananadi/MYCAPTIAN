num = int(input("enter the length of fibonacci sequence : "))
ar = [0, 1]
ans = 0
x = 0
while num != 0:
    print(ans)
    ans = ar[x] + ar[x + 1]
    ar[x] = ar[x + 1]
    ar[x + 1] = ans
    num -= 1
