while True:
    total_purchase = int(input("Enter the total purchase amount: "))
    initial_purchase = float(total_purchase)
    print (f"Initial Purchase Amount: {initial_purchase:.2f}")


    if total_purchase >= 5000:
        discount = total_purchase * 0.10
    else:
        discount = total_purchase * 0.05

    print(f"Discount: {discount:.3f}")
    final_price = total_purchase - discount
    print(f"Final Price: {final_price:.2f}")

    choice = input("Do you want to try again? (yes/no): ").lower()

    if choice != 'yes':
        break
print("Thank You!")
