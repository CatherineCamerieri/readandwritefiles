import csv

customers = open("customers.csv", "r", newline="")
outfile = open("customer_country.csv", "w", newline="")

customer_file = csv.reader(customers, delimiter=",")
writer = csv.writer(outfile, delimiter=",")

fieldnames = next(customer_file)
first_row = [fieldnames[1], fieldnames[2], fieldnames[4]]
# fieldnames = ["First Name, Last Name, Country"]
writer.writerow(first_row)

for row in customer_file:
    cust_id = row[0]
    first_name = row[1]
    last_name = row[2]
    city = row[3]
    country = row[4]
    phone = row[5]

    new_row = [first_name, last_name, country]
    # new_row = new_row.rstrip("\n")
    writer.writerow(new_row)


customers.close()
outfile.close()
