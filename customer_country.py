import csv

customers = open("customers.csv", "r", newline="")
outfile = open("customer_country.csv", "w", newline="")

customer_file = csv.reader(customers, delimiter=",")
writer = csv.writer(outfile, delimiter=",")

fieldnames = next(customer_file)
first_row = [fieldnames[1], fieldnames[2], fieldnames[4]]
writer.writerow(first_row)

i = 0
for row in customer_file:
    cust_id = row[0]
    first_name = row[1]
    last_name = row[2]
    city = row[3]
    country = row[4]
    phone = row[5]
    i += 1

    new_row = [first_name, last_name, country]
    writer.writerow(new_row)

print("Total number of customers read:", i)


customers.close()
outfile.close()
