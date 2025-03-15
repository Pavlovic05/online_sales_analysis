from cart import Cart
from products import Product
from product_manager import ProductManager

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoda
product1 = Product("Jabuka", 20, 100)
product2 = Product("Kruska", 50, 280)
manager.add_product(product1)
manager.add_product(product2)

# Prikazivanje svih proizvoda
manager.display_all_products()

# Prikazivanje ukupne vrednosti inventara
print(f"Total inventory value: {manager.total_inventory_value()}")

# Kreiranje instance Cart
cart = Cart()

# Dodavanje proizvoda u korpu
cart.add_to_cart(product1)
cart.add_to_cart(product2)

# Ispis ukupne vrednosti korpe
print(f"Total cart value: {cart.total_cart_value()}")
cart.display_cart()