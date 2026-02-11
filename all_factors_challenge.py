a = int(input("input number: "))
b = int(1)
for i in range(a + 1):
    if (( a % b ) == 0):
        print(b)
    b = (b + 1)