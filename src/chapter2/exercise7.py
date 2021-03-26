dolla = float(input("Enter amount to take charge for: "))

print("Your change is: ")

twenties = dolla // 20
ten = (dolla % 20) // 10
fives = ((dolla % 20) % 10)//5
ones = (((dolla % 20) % 10) % 5) // 1
quarter = ((((dolla % 20) % 10) % 5) % 1) // 0.25
dime = (((((dolla % 20) % 10) % 5) % 1) % 0.25) // 0.1
nickel = ((((((dolla % 20) % 10) % 5) % 1) % 0.25) % 0.1) // 0.05
penny = (((((((dolla % 20) % 10) % 5) % 1) % 0.25) % 0.1) % 0.05)//0.01

print(f'{int(twenties)} twenties')
print(f'{int(ten)} ten')
print(f'{int(fives)} five')
print(f'{int(ones)} ones')
print(f'{int(quarter)} quarters')
print(f'{int(dime)} dimes')
print(f'{int(nickel)} nickels')
print(f'{int(penny)} pennies')
