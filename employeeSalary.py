gender=input("Enter the sex of the employee:")
salary=float(input("Enter employee\'s salary:"))
if (gender == "m" ):
    bonus = 0.05*salary
    if (salary<10000):
        bonus = 0.07*salary
elif (gender == "f"):
    bonus = 0.10*salary
    if (salary<10000):
        bonus = 0.12*salary
else:print("****gender or salary amount not applicable****")
total_salary = salary+bonus
print("salary: %.2f " %salary)
print("bonus: %.2f " %bonus)
print("total amount paid to the employee: %.2f" %total_salary)
