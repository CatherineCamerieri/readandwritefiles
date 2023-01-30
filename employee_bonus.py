import csv

employees = open("EmployeePay.csv", "r", newline="")
reader = csv.reader(employees, delimiter=",")

print(
    format("First Name", "11"),
    format("Last Name", "16"),
    format("Salary", "^7"),
    format("Bonus", "5"),
    format("Total", "^10"),
)
print("-" * 53)

next(reader)

for row in reader:
    emp_ID = row[0]
    first_name = row[1]
    last_name = row[2]
    salary = int(row[3])
    bonus_per = float(row[4])

    bonus = bonus_per * salary
    total = bonus + salary

    print(
        format(first_name, "12"),
        format(last_name, "17"),
        "$",
        format(salary, "<8"),
        format(bonus_per, "<5.0%"),
        "$",
        format(total, "<10,.2f"),
        sep="",
    )

employees.close()
