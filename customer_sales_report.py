import csv

infile = open("sales.csv", "r", newline="")
outfile = open("salesreport.csv", "w", newline="")

reader = csv.reader(infile, delimiter=",")
writer = csv.writer(outfile, delimiter=",")

fieldnames = next(reader)
first_row = [fieldnames[0], "Total"]
writer.writerow(first_row)


prev_id = ""
prev_total = 0

for row in reader:
    cust_id = row[0]
    order_date = row[1]
    ship_date = row[2]
    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])

    if prev_id == "":
        prev_id = cust_id

    if cust_id == prev_id:
        total = prev_total + subtotal + tax + freight
        prev_total = total

    if cust_id != prev_id:
        prev_total = format(prev_total, ".2f")
        newrow = [prev_id, prev_total]
        writer.writerow(newrow)
        prev_total = 0
        total = subtotal + tax + freight

    prev_id = cust_id
    prev_total = total
prev_total = format(prev_total, ".2f")
newrow = [prev_id, prev_total]
writer.writerow(newrow)


infile.close()
outfile.close()
