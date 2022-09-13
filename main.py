from order import Order

print('*** Welcome to Chick-Fil-A ***')
option = 1

myOrder = Order()

while option != 0:
    print('')
    print('1. Lemonade')
    print('2. Coke')
    print('3. Cold Brew Coffee')
    print('4. Fries')
    print('5. Salad')
    print('6. Wrap')
    print('7. Chicken Strips')
    print('8. Chicken Nuggies')
    print('9. Kid\'s Meal')
    print('10. Mac n\' Cheese')
    print('11. Chicken Biscuit')
    print('12. Fruit Cup')
    print('13. Shake')
    print('14. Frosted Lemonade')
    print('15. Cookie')
    print('16. Chicken Sandwich')
    print('0. Done')
    print('Select an option: ')

    option = int(input())

    if option == 0:
        myOrder.print_order()
        break
    if option == 1:
        myOrder.add_lemonade()
    if option == 15:
        myOrder.add_cookie()
        