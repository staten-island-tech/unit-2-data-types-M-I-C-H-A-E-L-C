# Tip Calculator Challenge
# Generate a list of 1 random integer between 1 and 100 as well as a name before the integer (Bill, Tip, Total)
import random

rand_tip_percentage = random.randint(3, 5)

rand_tip_percentage_2 = random.randint(6, 13)

rand_tip_percentage_3 = random.randint(17, 30)

rand_int=(float) = random.randint(20, 200)
print(f"Bill: {rand_int} $")

rand_service = random.randint(1, 10)
print(f"Service Quality:  {rand_service}")

if (rand_service > 0 and rand_service < 5):
  print(f"Tip Percentage: {rand_tip_percentage} %")

if (rand_service > 4 and rand_service < 8):
  print(f"Tip Percentage: {rand_tip_percentage_2} %")

if (rand_service > 7 and rand_service < 11):
  print(f"Tip Percentage: {rand_tip_percentage_3} %")

x=str(rand_int * (rand_tip_percentage / 100))
y=str(rand_int * (rand_tip_percentage_2 / 100))
z=str(rand_int * (rand_tip_percentage_3 / 100))

if (rand_service > 0 and rand_service < 5):
   print (f"Tip Amount:" + x + "$")

if (rand_service > 4 and rand_service < 8):
   print (f"Tip Amount:" + y + "$")

if (rand_service > 7 and rand_service < 11):
   print (f"Tip Amount:" + z + "$")

x=(rand_int * (rand_tip_percentage / 100))
y=(rand_int * (rand_tip_percentage_2 / 100))
z=(rand_int * (rand_tip_percentage_3 / 100))
rand_int=(rand_int)

u=str(rand_int + x)
v=str(rand_int + y)
w=str(rand_int + z)

if (rand_service > 0 and rand_service < 5):
   print (f"Total:" + u + "$")

if (rand_service > 4 and rand_service < 8):
   print (f"Total:" + v + "$")

if (rand_service > 7 and rand_service < 11):
   print (f"Total:" + w + "$")