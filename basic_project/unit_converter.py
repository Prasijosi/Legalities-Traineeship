#Unit converter
unit = input('Enter unit (mi, km, C, F, lbs, kg): ')
value = float(input("Enter value: "))

# Convert based on the unit entered
if unit.lower() == "mi":
    print(f"{value} miles is equal to {value * 1.60934} kilometers")
elif unit.lower() == "km":
    print(f"{value} kilometers is equal to {value * 0.621371} miles")
elif unit.lower() == "lbs":
    print(f"{value} pounds is equal to {value * 0.453592} kilograms")
elif unit.lower() == "kg":
    print(f"{value} kilograms is equal to {value * 2.20462} pounds")
elif unit.lower() == "c":
    print(f"{value} Celsius is equal to {(value * 9/5) + 32} Fahrenheit")
elif unit.lower() == "f":
    print(f"{value} Fahrenheit is equal to {(value - 32) * 5/9} Celsius")
else:
    print("Invalid unit")
