class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    def add_lemonade(self):
        self.total_cost+=7.5
        self.items+=["lemonade"]

    def add_chicken_strips(self):
        self.total_cost+=15
        self.items+=["chicken strips"]

    # implement methods for menu items
