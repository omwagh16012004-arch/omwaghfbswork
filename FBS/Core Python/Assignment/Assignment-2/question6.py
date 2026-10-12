num1 = float(input("Enter basic salary: "))

da = num1 * 10 / 100
ta = num1 * 12 / 100
hra = num1 * 15 / 100

total_salary = num1 + da + ta + hra

print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total salary =", total_salary)