num = int(input("Enter a three-digit number: "))

dig1 = num % 10
num = num // 10

dig2 = num % 10
number = num // 10

digit3 = number

sum_digits = dig1 + dig2 + digit3

print("Sum of digits =", sum_digits)