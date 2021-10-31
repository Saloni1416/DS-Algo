print("Welcome to Life in Weeks\n------------------------------------")
age=input("What is your current age?\n")
#days-weeks-month
newAge=90-int(age)

print(F"You are gonna live for {newAge} years more")

days=365*newAge

weeks=52*newAge

month=12*newAge

print("---------------------------------")
message=f"And You have {month} months, {weeks} weeks and {days} days left "

print(message)