import time
def vendingmachine():
    products = [
        {'code': 'D1', 'name': 'Coca-Cola', 'price': 2.50, 'stock': 1},
        {'code': 'D2', 'name': 'Lemon Juice', 'price': 4.00, 'stock': 7},
        {'code': 'D3', 'name': 'Iced Coffee', 'price': 5.00, 'stock': 8},
        {'code': 'D4', 'name': 'Coffee Jelly', 'price': 5.50, 'stock': 5},
        {'code': 'D5', 'name': 'Water', 'price': 1.50, 'stock': 5},
        {'code': 'S1', 'name': 'Siopao', 'price': 3.25, 'stock': 7},
        {'code': 'S2', 'name': 'Doritos', 'price': 2, 'stock': 4},
        {'code': 'S3', 'name': 'Cookies', 'price': 5, 'stock': 10},
        {'code': 'S4', 'name': 'Pillows', 'price': 3, 'stock': 2},
        {'code': 'S5', 'name': 'Bread Ham', 'price': 7.50, 'stock': 9},
    ]
    balance = 0
    quit = False

    while quit == False:
        print("Welcome to Vending Machine")
        time.sleep(1)
        print("------------------------------------------------------------------")
        print("MENU")
        for product in products: #printing everything in the dictionary
            time.sleep(0.1)
            print(f"Product Name: {product['name']} - Price: {product['price']} - Code: {product['code']} - Stock: {product['stock']}")
        print("------------------------------------------------------------------")

        order = (input("Enter the code name of the item that you'd like to get: "))
        for product in products:
            if order == product['code']:
                order = product
                order['stock'] -= 1 #stocks decreases as long as the program runs
                if order['stock'] == 0:
                    products.remove(product)

        else:
            print(f"Great, {order['name']} will cost you {order['price']} AED") # if code in products are the same,else statement will be shown

            cash = float(input(f"Enter {order['price']} AED to buy: "))

            if cash < order['price']: # if order/price is higher than cash then it will ask the user to input the exact cash to get the customer's item
                balance = float(input("Insert exact amount: "))
                balance = balance + cash
                if balance == order['price']:
                    balance -= order['price']
                    print(str(order['name']) + " being dispensed...")
                    time.sleep(2)
                    print("Here's your " + str(order['name']))
                elif balance > order['price']:
                    balance -= order['price']
                    print(str(order['name']) + " being dispensed...")
                    time.sleep(2)
                    print("Here's your " + str(order['name']) + " and a balance of " + str(balance))
                else:
                    print("Current balance:" + str(balance) + "AED")
                    print("Insert exact amount")

            elif cash == order['price']: # if the inputted cash is equal to order/price then this will be executed
                print(str(order['name']) + " being dispensed...")
                time.sleep(2)
                print(f"Thank you for buying here is your {order['name']}")

            elif cash > order['price']: #if cash is higher than order then this will be executed
                balance = cash - order['price']
                print(str(order['name']) + " being dispensed...")
                time.sleep(2)
                print("Here's your " + str(order['name'] + " and remaining " + str(balance) + "AED"))

        print("Note: If you have remaining balance quit the program first, so you can get your change")
        answer = input("To continue buying type C and to quit the program type Q: ")
        if answer == 'c'.upper(): #If the keyword C or any keyword is entered except Q then it will contimue
            quit = False
        elif answer == 'q'.upper(): #If the keyword Q is entered then it will quit the program
            quit = True
            if balance != 0: #If the user have remaining balance in the machine then it will return the balance to it's user
                print("Thank you, come again and here's your change " + str(balance))
            else: #If balance is equal to zero then this will be executed
                print("Thank you, come again!")



vendingmachine()