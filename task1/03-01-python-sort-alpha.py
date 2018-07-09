import csv

date = open("task1.csv")
reader = csv.reader(date)

datelist = []

for row in reader:
	datelist.append(row)

datelist.sort()
datelist.insert(0,datelist[-1])
del datelist[-1]

for lists in datelist:
	print(" ".join(lists))