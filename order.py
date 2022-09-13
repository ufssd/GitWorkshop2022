class Order:
    def __init__(self):
        self.total_cost = 0
        self.items  = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')


    def add_lemonade(self):
        self.total_cost += 7.5
        self.items += ('lemonade')
        print("Added lemonade!")   

    def add_cookie(self):
        self.total_cost += 3.0
        self.items+= ('cookie')
        print("Added cookie")
        
    def add_wrap(self):
        self.total_cost = 6
        self.items.append("wrap")
        print("Added wrap")

    # implement methods for menu items
    def add_chicken_strips(self):
        self.total_cost += 15
        self.items += ['chicken strips']
        print('added chicken strips')