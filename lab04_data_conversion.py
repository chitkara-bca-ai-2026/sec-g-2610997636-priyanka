print("==================================================")
print("             DATA CONVERSION UTILITY")
print("==================================================")

product_name = input("Enter Product Name : ")
price = float(input("Enter Price       : "))
quantity = int(input("Enter Quantity    : "))

total_price = price * quantity
amount_str = str(total_price)

print("--------------------------------------------------")
print("               TYPE CASTING SUMMARY")
print("--------------------------------------------------")

print(f"{'Variable':<16} {'Value':<15} {'Python Type'}")
print("-" * 50)


print(f"{'product_name':<16} {str(product_name):<15} {str(type(product_name))}")
print(f"{'price':<16} {str(price):<15} {str(type(price))}")
print(f"{'quantity':<16} {str(quantity):<15} {str(type(quantity))}")
print(f"{'total_price':<16} {str(total_price):<15} {str(type(total_price))}")
print(f"{'amount_str':<16} {str(amount_str):<15} {str(type(amount_str))}")

print()
print("--------------------------------------------------")
print("                 TAX INVOICE")
print("--------------------------------------------------")

print("Product Name  : ", product_name)
print("Price per Unit: Rs.", price)
print("Quantity      : ", quantity)

print("--------------------------------------------------")

print("Invoice Total : Rs.", amount_str)

print("==================================================")