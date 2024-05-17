menu = {

        'Tea' : 10,
        'Coffee' : 20,
        'Pizza' : 100,
        'Burger' : 50,
        'Pasta' : 70,
        'Cold Coffee' : 50,
        'Garlic Bread' : 70,

}

print (" \nWelcome To Star Bucks Cafe & Restro ") 
print (" \nMENU: \n Tea : Rs10\n Coffee : Rs20\n Pizza : Rs100\n Burger : Rs50\n Pasta : Rs70\n Cold Coffee : Rs50\n Garlic Bread : Rs70 ")

Total_Amount = 0

Order_1 = input(" \nEnter the name of Dish/Beverage you want to order\n ")
if Order_1 in menu:
    Total_Amount += menu[Order_1]
    print(f" Your Order { Order_1} has been placed ")

else:
    print(f" Order Dish/Beverage { Order_1 } is not available now! ")

another_order = input("Do you want to add another order? (Yes/No)\n ")
if another_order =="Yes" :
        Order_2 = input("Enter your second order = ")
        if Order_2 in menu :
                Total_Amount += menu[Order_2]
                print(f"Item {Order_2} has been added to order")
        else:
                print(f"Ordered item {Order_2} is not available!")
                print(f"The total amount of order to pay is {Total_Amount}")



