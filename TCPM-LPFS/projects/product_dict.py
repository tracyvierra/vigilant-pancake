# Author: Tracy Vierra
# Date Created: 2/28/2022
# Date Modified: 2/28/2022

# Description:

# Usage:

products = {"product 1": {"price": 10, "stock": 5}, "product 2": {"price": 20, "stock": 10}, "product 3": {"price": 30, "stock": 15}, "product 4": {"price": 60, "stock": 15}, "product 5": {"price": 70, "stock": 15}}

print("Product List: ")
print(" ")

for key in products.keys():
  print(key)

print(" ")

prod = input("Please enter a product to see the price and number of stock available: ")

print(products.get(prod, "Product not found"))


'''
products = {"Chair":40, "Sofa": 500, "Table": 90, "Monitor": 100 , "Carpet": 200}
newproduct = input('Enter product name')
if(newproduct in products):
    print(products.get(newproduct))
else:
    print('Product Not Found')
'''