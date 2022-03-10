
print("Welcome to my tip calculator!")
bill = float(input("how much was the bill? "))
tip = int(input("how much tip do you want to leave? 10,12,15?  "))
people = int(input("How many people are you splitting the bill with? "))

bill_with_tip = bill / 100 * tip + bill
bill_per_person = bill_with_tip/people
final_amount = "{:.2f}".format(bill_per_person)

print(" ")
print(f"The amount each person should pay is {final_amount}€")
