x = float(input("Bill Amount?: "))

y = input("Was the service bad, okay, good or great?: ")

if(y == "bad"):
    print("Tip Amount = 0%")

if(y == "okay"):
    print("Tip Amount = 15%")

if(y == "good"):
    print("Tip Amount = 20%")

if(y == "great"):
    print("Tip Amount = 25%")