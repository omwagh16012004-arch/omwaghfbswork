num1 = float(input("Enter cost price: "))
num2 = float(input("Enter discount percentage: "))

discount = num1 * num2 / 100

selling_price = num1 - discount

print("Selling price =", selling_price)