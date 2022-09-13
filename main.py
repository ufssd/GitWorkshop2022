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
    if option ==1:
        myOrder.add_lemonade()
     if option ==2:
        myOrder.add_coke()
     if option ==3:
        myOrder.add_cold_brew_coffee()
     if option ==4:
        myOrder.add_fries()
     if option ==5:
        myOrder.add_salad()
     if option ==6:
        myOrder.add_wrap()
     if option ==7:
        myOrder.add_chicken_strips()
     if option ==8:
        myOrder.add_chicken_nuggets()
     if option ==9:
        myOrder.add_kids_meal()
     if option ==10:
        myOrder.add_mac_n_cheese()
     if option ==11:
        myOrder.add_chicken_biscuit()
     if option ==12:
        myOrder.add_fruit_cup()
     if option ==13:
        myOrder.add_shake()
     if option ==14:
        myOrder.add_frosted_lemonade()
     if option ==15:
        myOrder.add_cookie()
     if option ==16:
        myOrder.add_chicken_sandwich()