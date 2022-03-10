
age = input("What is your current age? ")
expected_age = input("What age do you think you will live until? ")

days = (int(expected_age) * 365) - (int(age) * 365)
weeks = (int(expected_age) * 52) - (int(age) * 52)
months = (int(expected_age) * 12) - (int(age) * 12)

# days = 32850 - (int(age) * 365)
# weeks = 4680 - (int(age) * 52)
# months = 1080 - (int(age) * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left." )
