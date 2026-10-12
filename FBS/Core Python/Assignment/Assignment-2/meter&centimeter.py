num1 = float(input("Enter feet: "))
num2 = float(input("Enter inches: "))

total_inches = (num1 * 12) + num2

centimeters = total_inches * 2.54
meters = centimeters / 100

print("Distance in meters =", meters)
print("Distance in centimeters =", centimeters)