import csv

date = open("task1.csv")
reader = csv.reader(date)

for row in reader:
	print(" ".join(row))