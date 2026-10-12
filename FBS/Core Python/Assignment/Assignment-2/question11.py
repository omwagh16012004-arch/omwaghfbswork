amount = int(input("Enter amount: "))

note500 = amount // 500
amount = amount % 500

note200 = amount // 200
amount = amount % 200

note100 = amount // 100
amount = amount % 100

note50 = amount // 50
amount = amount % 50

note20 = amount // 20
amount = amount % 20

note10 = amount // 10
amount = amount % 10

total_notes = note500 + note200 + note100 + note50 + note20 + note10

print("500 notes =", note500)
print("200 notes =", note200)
print("100 notes =", note100)
print("50 notes =", note50)
print("20 notes =", note20)
print("10 notes =", note10)

print("Total notes =", total_notes)