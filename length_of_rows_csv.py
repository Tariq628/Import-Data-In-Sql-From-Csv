import csv


with open('sample4.csv', "r",encoding='utf-8') as file_obj:
    reader_obj = csv.reader(file_obj)
    row_count = sum(1 for row in reader_obj)  # fileObject is your csv.reader
    print(row_count)