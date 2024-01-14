
# NO 1
# def cashier_check(shoppinglist, register):
#     list = []
#     for i in range(len(shoppinglist)):
#         if shoppinglist[i] not in register:
#             list.append(shoppinglist[i])
#     return list

# NO 2
def cashier_receipt(shoppinglist, register):
  total_bill = 0.0

  for item in shoppinglist:
      if item in register:
          cost = register[item]
          quantity = shoppinglist.count(item)
          total_item_cost = cost * quantity

          print(f"{quantity} {item}: ${total_item_cost:.2f}\n")
          total_bill += total_item_cost

  return(f"Total: ${total_bill:.2f}")

# Example usage:
print(cashier_receipt(['Milk', 'Watermelon', 'Orange', 'Apple', 'Toy'], {'Milk': 3.3, 'Orange': 0.5, 'Watermelon': 5}))