
# Question 1: Cashier Check
# def cashier_check(shoppinglist, register):
#     list = []
#     for i in range(len(shoppinglist)):
#         if shoppinglist[i] not in register:
#             list.append(shoppinglist[i])
#     return list

# Question 2: Cashier Receipt
def cashier_receipt(shoppinglist, register):
    total_bill = 0.0

    # Use a set to keep track of processed items
    processed_items = set()

    for item in shoppinglist:
        if item in register and item not in processed_items:
            quantity = shoppinglist.count(item)
            cost = register[item]
            total_item_cost = quantity * cost

            print(f"{quantity} {item}: ${total_item_cost:.2f}")
            total_bill += total_item_cost

            # Add the item to the set of processed items
            processed_items.add(item)

    print(f"Total: ${total_bill:.2f}")

# Example usage:
print(cashier_receipt(['Milk', 'Milk', 'Apple', 'Apple'], {'Milk': 3.3, 'Apple': 0.7}))