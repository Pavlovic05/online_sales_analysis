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
