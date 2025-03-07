print("List your 4 subjects marks:")
math = int(input("Math:"))
science = int(input("Science:"))
english = int(input("English:"))
history = int(input("History:"))
sum = math+science+english+history
print("Sum of all 4 subjects:" , sum)
perc = (sum/400)*100
print(end = "Percentage mark = ")
print(perc)