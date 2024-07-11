import sys

names = ["Bill", "Carter", "Jhon", "Doe", "Maria", "Jennifer"]

search = input("Name: ").lower()

#The linear search algorithm 
for n in names:
    if search == n.lower():
        print(f"{n} Founded")
        sys.exit(0)

print("Not Found")
sys.exit(1)