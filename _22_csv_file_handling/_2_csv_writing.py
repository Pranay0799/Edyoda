import csv

fieldnames = ["rno","name"]
rows = [[1,"Bharati"],[2,"Shruti"]]

with open(r"C:\Users\prana\OneDrive\Desktop\EdYoda Data Science Course\lectur notes from 24_09_23\DS140823\Python\_22_csv_file_handling\test.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer.writerows(rows)

