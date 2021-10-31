print("Welcome to the Tip-Calculator\n-----------------------------")

total_bill=float(input("What was the total bill?\nRs."))

tip_percent=int(input("What percentage of tip would u like to give?10,12 or 15?\n"))

total_bill=total_bill*(1+tip_percent/100)
#total_bill=tip_percent/100*total_bill+total_bill

no_of_people=int(input("How many people to split the bill?\n"))

total_bill=round(total_bill/no_of_people,2)
#total_bill="{:.2f}".format{total_bill}

print("-----------------------------")
print(f"Each person should pay:\nRs.{total_bill}")
