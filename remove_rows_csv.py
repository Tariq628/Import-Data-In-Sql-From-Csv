import csv


with open('sample4.csv', 'rb') as inp, open('sample4_edit.csv', 'wb') as out:
    writer = csv.writer(out)
    for i, row in enumerate(csv.reader(inp)):
        writer.writerow(row)
