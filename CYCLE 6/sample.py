import csv
with open('D:\csvfile.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 print("ID Name")
 print("---------------------------------")
 for row in data:
   print(row['ID'], row['NAME'])
 