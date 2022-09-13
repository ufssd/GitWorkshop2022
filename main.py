from order import Order

print('*** Welcome to Chick-Fil-A ***')
option = 1

myOrder = Order()

while option != 0:
    print('')
    print('1. Drink')
    print('2. Fries')
    print('3. Salad')
    print('4. Shake')
    print('5. Chicken Nuggies')
    print('6. Chicken Sandwich')
    print('0. Done')
    print('Select an option: ')

    option = int(input())

    if option == 0:
        myOrder.print_order()
        break
    # implement more cases here