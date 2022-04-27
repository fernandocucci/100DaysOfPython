print('==========================================')
print('| Day 002 - Project: Tip Calculator      |')
print('==========================================')
bill = float(input("How much is the bill?: $"))
tip = int(input("Tip % (10,15,20)): "))
people = int(input("Split the bill in how many persons?: "))

total = "{:.2f}".format(bill*(1+(tip/100))/people)

print(f"Each person must pay ${total}")
