'''Product inventory feature'''

product = {
    "ID-1" : {
        "name" : "Adidas",
        "price" : 1380,
        "quantity" : 2,
        "category" : "shoes",
        "stock"  : 30

    }
}
product["ID-2"] = {
    "name" : "Royal Oud",
    "price" : 999,
    "quantity" : 2,
    "category" : "perfume",
    "stock" : 1
}
product["ID-2"]["quantity"] = 4
                 
total_stock = 0
total_price = 0

for pid, info in product.items():
    total_stock += info["stock"] 
    total_price += info["price"] * info["quantity"]
    # product_quantity[pid] = info["quantity"]

total_product = len(product)
average_price = total_price / total_price
search_category = input("Enter your category: ")
            
found = False

for pid , info in product.items():

    if info["category"].lower() == search_category.lower():
        found = True
        print("\nSearched category")
        print("=" * 30)
        print("ProductID:",pid)
        print("Name    : ", info["name"])
        print("Price   : ", info["price"])
        print("Quantity: ",  info["quantity"])
        print("Category: ",  info["category"])
        print("Stock   : ", info["stock"])
        print("=" * 36)
        print("Total stock of all categories is:",total_stock)
        print("=" * 36)
        print("Average price is: ",average_price)
        print("=" * 36)
        
        if info["stock"] <= 2:
            print("Stock Alert! " "\n" "Your stock almost finished.")        
        else:
            print("You have good amount of stock.")  
    
if not found:
    print("Your search category is not found")

