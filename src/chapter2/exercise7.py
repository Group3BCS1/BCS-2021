dolla = float(input("Enter amount to take charge for: "))

twenties = dolla //20
ten = (dolla % 20) // 10
fives = ((dolla % 20) % 10)//5
ones = ((dolla % 20) % 10) // 1
quarter = (((dolla % 20) % 10) % 1) // 0.25
dime = ((((dolla % 20) % 10) % 1) % 0.25) // 0.1
nickel = (((((dolla % 20) % 10) % 1) % 0.25) % 0.1) // 0.05
penny = ((((((dolla % 20) % 10) % 1) % 0.25) % 0.1)% 0.05)//0.01

print(f'{twenties} twenties')
print(f'{ten} ten')
print(f'{fives} five')
print(f'{ones} ones')
print(f'{quarter} quarters')
print(f'{dime} dimes')
print(f'{nickel} nickel')
print(f'{penny} penny')
