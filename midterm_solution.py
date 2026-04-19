name = input("Enter your name: ")
weekly_budget = int(input("Enter your Weekly Budget: "))

print(f"Student Name: {name}")
print(f"Weekly Budget: {weekly_budget}")
print("=================================")
print("  WEEKLY EXPENSE -- CATEGORIES  ")
print("=================================")

expense_category = [
    ["1. Food & Drinks",       "[e.g. Lunch, snacks, coffee]"],
    ["2. Transportation",      "[e.g. Bus, jeepney, ride-share]"],
    ["3. Mobile / Internet",   "[e.g. Load, data plan, WiFi top-up]"],
    ["4. School Supplies",     "[e.g. Notebook, pen, bond paper]"],
    ["5. Entertainment",       "[e.g. Games, movies, hangout]"]
]

for item in expense_category:
    print(item[0], item[1])

print("=================================")

expenses = []

total = 0
for i in range(4):
    total += 1
    print(f"--- EXPENSE {total} ---")

    choice = int(input("Category (1 - 5 or 0 to skip): "))

    if choice >=1 and choice <= 5:
        print(expense_category[choice-1][0])
    elif choice == 0:
        continue
    else:
        while choice > 5:
            print("Invalid Input. Try again")
            choice = int(input("Category (1 - 5 or 0 to skip): "))
        
    
    description = input("Description: ")
    amount = int(input("Amount: "))
    tag = ""
    if amount > 0.25 * weekly_budget:
        tag = "! High Expense Alert!"
        print(tag)
    
    
    expenses.append({"choice":choice-1, "description":description, "amount":amount, "tag":tag})


print("=================================")
print(f"  {name.upper()} -- WEEKLY EXPENSE LOG  ")
print("=================================")

print(f"Weekly Budget: P{weekly_budget:.2f}")


for exp in range(len(expenses)):


    print(f"[{exp + 1}] {expense_category[expenses[exp]["choice"]][0]}")
    
    print(expenses[exp]["description"])
    print(expenses[exp]["amount"])



print("----------------------------------")

spent = 0
for expense in expenses:
    spent += expense["amount"]
print(f"Total Expense: P{spent:.2f}")
remained = weekly_budget - spent
print(f"Remaining: P{remained:.2f}")

if remained >= 0:
    print("Status: Budget OK! Keep it up.")
elif remained < 0:
    print("Status: Budget OK! Keep it up.")
print("=================================")