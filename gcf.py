a = int(input("input number 1: "))
b = int(input("input number 2: "))
y = int(1)
for i in range(max(a , b)):
    if (a % y == 0 and b % y == 0):
        x = y 
    y = (y + 1)
print(x)