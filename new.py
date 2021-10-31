print("Welcome to the Roller Coaster!")

print("----------------------------------")

height=int(input("What is your height in cm?\n"))
bill=0

if height>120:
  print("You can ride the Roller Coaster!")
  print("--------------------------")

  age=int(input("What's your age?\n"))

  if age<=15:
    bill=5
    print("Child ticket is $5")
    print("--------------------------")
  elif age<=25:
    bill=7
    print("Youth ticket is $7")
    print("--------------------------")
  else:
    bill=12
    print("Adults ticket is $12")
    print("--------------------------")

  wants_photo=input("Do u want a photo?(y or n)\n")
  if wants_photo=="y":
    bill+=3
    print(f"Amout to be paid is ${bill}")
  else:
    print("Ok,then enjoy your ride")
    # print("Get the hell out of here!")

else:
  print("--------------------------")
  print("Sorry, you have to grow taller before you ride the Roller Coaster!")



  