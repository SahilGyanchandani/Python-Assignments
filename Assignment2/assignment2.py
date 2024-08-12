class Product:
    def __init__(self, name, price, quantity, product_type):
        self.name = name
        self.price = float(price.replace("RS", "").strip())
        self.quantity = int(quantity)
        self.product_type = product_type

    def __str__(self):
        return f"{self.name}, {self.price} RS, {self.quantity}, {self.product_type}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name.lower() != product_name.lower()]

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def list_products(self):
        for product in self.products:
            print(product)

    def count_products(self):
        return len(self.products)

    def list_products_by_type(self, product_type):
        return [product for product in self.products if product.product_type == product_type]

    def purchase(self, items):
        total_cost = 0
        for item, quantity in items.items():
            product = self.find_product(item)
            if product:
                total_cost += product.price * quantity
        return round(total_cost)

# Initialize Inventory
inventory = Inventory()

# Add initial products
initial_products = [
    ("lettuce", "10.5 RS", 50, "Leafy green"),
    ("cabbage", "20 RS", 100, "Cruciferous"),
    ("pumpkin", "30 RS", 30, "Marrow"),
    ("cauliflower", "10 RS", 25, "Cruciferous"),
    ("zucchini", "20.5 RS", 50, "Marrow"),
    ("yam", "30 RS", 50, "Root"),
    ("spinach", "10 RS", 100, "Leafy green"),
    ("broccoli", "20.2 RS", 75, "Cruciferous"),
    ("garlic", "30 RS", 20, "Leafy green"),
    ("silverbeet", "10 RS", 50, "Marrow")
]

for product in initial_products:
    inventory.add_product(Product(*product))

# 1. Print the total number of products in the list
print("Total number of products:", inventory.count_products())

# 2. Add a new product (Potato, 10 RS, 50, Root)
inventory.add_product(Product("Potato", "10 RS", 50, "Root"))

# Print all products and the total number
print("\nAll products after adding Potato:")
inventory.list_products()
print("Total number of products after adding Potato:", inventory.count_products())

# 3. Print all the products of which have the type Leafy green
leafy_green_products = inventory.list_products_by_type("Leafy green")
print("\nLeafy green products:")
for product in leafy_green_products:
    print(product)

# 4. Remove Garlic from the list and print the total number of products left
inventory.remove_product("Garlic")
print("\nAll products after removing Garlic:")
inventory.list_products()
print("Total number of products after removing Garlic:", inventory.count_products())

# 5. Add 50 cabbages to the inventory
cabbage = inventory.find_product("cabbage")
if cabbage:
    cabbage.quantity += 50
print("\nFinal quantity of Cabbage in inventory:", cabbage.quantity)

# 6. Purchase 1kg lettuce, 2kg zucchini, 1kg broccoli
items_to_purchase = {"lettuce": 1, "zucchini": 2, "broccoli": 1}
total_cost = inventory.purchase(items_to_purchase)
print("\nTotal cost for purchasing 1kg lettuce, 2kg zucchini, 1kg broccoli:", total_cost, "RS")