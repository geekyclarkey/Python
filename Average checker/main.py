
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Easy way
# total = sum(student_heights) #This adds up the value of each integer in the list
# amount = len(student_heights) #This gets the amount of items in the list
# average = round(total/amount) #This gets the average by deviding the total amount with the amount of items then rounds the total

# Or the hard way. Using For loop
total = 0
amount = 0

for height in student_heights:
  total = total + height

for student in student_heights:
  amount = amount + 1

average = round(total/amount)

print(average)
