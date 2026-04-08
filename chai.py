# total = 0

# while True:

#     print("\n----- Tea Menu -----")
#     print("1. Small Tea - ₹15 ")
#     print("2. Medium Tea - ₹30")
#     print("3. Larg Tea - ₹45")


# # Enter the choice of cup

#     choice = input("Enter cup size (small/medium/larg): ").lower()
#     # Enter the quanity of cup
#     qty = int(input("Enter quantity: "))

# #  if else statement

#     if choice == "small":
#         price = 15

#     elif choice == "medium":
#         price = 30

#     elif choice == "larg":
#         price = 45

#     else:
#         print("Invalid choice! Try again")
#         continue

#     amount = price * qty
#     total += amount

#     print("Added ₹", amount, "to total bill.")
#     more = input("Do you want to order more? (yes/no): ").lower()
#     if more != "yes":
#         break
# print("\n-------Final Bill-------")
# print("Total Amount to Pay: ₹", total)
# print("Thank you! visit again")



total = 0

while True:

    print("\n----- Tea Menu -----")
    print("1. Small Tea - ₹15 ")
    print("2. Medium Tea - ₹30")
    print("3. Larg Tea - ₹45")


# Enter the choice of cup

    choice = input("Enter cup size (small/medium/larg): ").lower()
    # Enter the quanity of cup
    qty = int(input("Enter quantity: "))

#  if else statement

    if choice == "small":
        price = 15

    elif choice == "medium":
        price = 30

    elif choice == "larg":
        price = 45

    else:
        print("Invalid choice! Try again")
        continue

    amount = price * qty
    total += amount

    print("Added ₹", amount, "to total bill.")
    more = input("Do you want to order more? (yes/no): ").lower()
    if more != "yes":
        break
print("\n-------Final Bill-------")
print("Total Amount to Pay: ₹", total)

if total > 1000:
    x = str(input("Enter your cupan code: ")).lower()
    if x == "ayush":
        print(total-total/100*25)

    else:
        print("Coupen code is invalide")



print("Thank you! visit again")