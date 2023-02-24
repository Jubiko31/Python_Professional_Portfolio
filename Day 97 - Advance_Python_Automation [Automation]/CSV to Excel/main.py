import csv
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active()

csv_file = open('file.csv', 'r')

for row in csv.reader(csv_file):
    sheet.append(row)
    
csv_file.close()

workbook.save("results.xlsx")

