print("Divagar Supermarket")
print("No 44 nehru street puducherry")
print("-------------------------")
print("Bill Receipt")
print("-----------------------")
input("Enter the serial Number:")
input("Enter the particutars:")
rate=int(input("Enter the rate:"))
quantity=int(input("Enter the quanlity:"))
total=rate*quantity
print("total amount RS:",total)
gst=total *10/100
print("gst (10per):",gst)

print("amount to be paid :",total)
