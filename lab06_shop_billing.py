print("==================================================")
print("          CLOTHING STORE BILLING SYSTEM           ")
print("==================================================")

customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

total_amount = price * quantity

print("\n=================================================")
print("                     BILL                          ")
print("=================================================")

print("Customer Name    :", customer_name)
print("Garment Name     :", garment_name)
print("Price Per Unit   : Rs.", price)
print("Quantity         :", quantity)
print("Total Amount     : Rs.", total_amount)

print("=================================================")