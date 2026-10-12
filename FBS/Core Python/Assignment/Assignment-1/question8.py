D = int(input('Enter days :'))

years = D // 365
remaining_days = D % 365

weeks = remaining_days // 7
remaining_days = remaining_days % 7

print("Years =", years)
print("Weeks =", weeks)
print("Days =", remaining_days)