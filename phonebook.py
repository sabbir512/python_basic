import csv

file = open("phonebook.csv", "a")

name = input("Name: ")
number = input("Number: ")

write = csv.writer(file)
write.writerow([name, number])

file.close()