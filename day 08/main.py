item_name = ['milk','bread','eggs','banana']
quantities = [2,3,4,6]
prices = [100,120,40,20]

# Add items
def add_items(name,quantity,price):
    item_name.append(name)
    quantities.append(quantity)
    prices.append(price)
    print(f"{name} added successfully")
# remove items
def remove_items(name):
    if name in item_name:
        index = item_name.index(name)
        quantities.pop[index]
        prices.pop[index]
        print(f"{name} removed successfully!")
    else:
        print("Item not found")     
# update quantity
def update_quantity(name,new_quantity):
    if name in item_name:
        index = item_name.index(name)
        quantities[index] = new_quantity
        print(f"{name} updated successfully to {new_quantity}.")
    else:
        print(f"{name} not found.")

# calculate total
def calculate_total():
    subtotal = sum(p * q  for p,q in zip(quantities , prices))
    discount = 0
    discount = subtotal * 0.10
    if subtotal>100:
        total = subtotal - discount
    return subtotal,discount,total
print("=" * 38)
print("            ITEMS RECEIPT")
print("=" * 38)

print(f"{'item':<10}{'quanity':<10}{'price':<8}{'subtotal':<10}")   
print("=" * 38)
for i in range(len(item_name)):
    subtotal = quantities[i] * prices[i]
    print(f"{item_name[i]:<10}{quantities[i]:<10}{prices[i]:<10}{subtotal}")
    print("=" * 38)


