# Tip Calculator Challenge
# Generate a list of 1 random integer between 1 and 100 as well as a name before the integer (Bill, Tip, Total)
import random

rand_tip_percentage = random.randint(3, 5)

rand_tip_percentage_2 = random.randint(6, 13)

rand_tip_percentage_3 = random.randint(15, 30)

rand_int = random.randint(20, 200)
print(f"Bill: {rand_int} $")

rand_service = random.randint(1, 10)
print(f"Service Quality:  {rand_service}")

if (rand_service > 0 and rand_service < 5):
  print(f"Tip Percentage: {rand_tip_percentage} %")

if (rand_service > 4 and rand_service < 8):
  print(f"Tip Percentage: {rand_tip_percentage_2} %")

if (rand_service > 7 and rand_service < 11):
  print(f"Tip Percentage: {rand_tip_percentage_3} %")



if (rand_service > 0 and rand_service < 5):
   print (rand_int * (rand_tip_percentage / 100),"$")

if (rand_service > 4 and rand_service < 8):
   print (rand_int * (rand_tip_percentage_2 / 100),"$")

if (rand_service > 7 and rand_service < 11):
   print (rand_int * (rand_tip_percentage_3 / 100),"$")



if (rand_service > 0 and rand_service < 5):
   print (f"Tip Amount:" (rand_int * (rand_tip_percentage / 100)* rand_int))