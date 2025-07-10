number = int(input("Enter a number to see its multiplication table:").strip())

for x in range(1,11):
    print(f"{number} * {x} = {number * x}")
