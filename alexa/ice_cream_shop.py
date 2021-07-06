
print("1.chocolate 100")
print("2.vanilla 80")
print("3.mango 180")
print("4.kesar pista 50")
print("5.straberry 150")

flavour = int(input("enter your choice for ice cream:"))
quantity = int(input("enter quantity:"))
if flavour==1:
    bill=100*quantity
    print("your bill is: ",bill)
if flavour==2:
    bill=80*quantity
    print("your bill is: ",bill)
if flavour==3:
    bill=150*quantity
    print("your bill is: ",bill)
if flavour==4:
     bill=50*quantity
     print("your bill is: ",bill)
if flavour == 5:
        bill = 150 * quantity
        print("your bill is: ", bill)