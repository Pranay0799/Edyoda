# CSV - Comma Seperated Value
# extension - .csv
import csv

with open(r"C:\Users\prana\OneDrive\Desktop\EdYoda Data Science Course\lectur notes from 24_09_23\DS140823\Python\_22_csv_file_handling\demo.csv") as file:
    data = csv.reader(file)

    header = next(data)
    
    
    rows = []
    for i in data:
        print(i)
        rows.append(i)

    count = data.line_num
    print("Count : ",count)

    for i in rows[:1]:
        print(i)
