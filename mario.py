while True:
    getNum = int(input("Put a valid number: "))
    if getNum > 0:
        break

i = 1  
while i <= getNum:
    for j in range(i):
        print("#", end="")
    print()
    i += 1
