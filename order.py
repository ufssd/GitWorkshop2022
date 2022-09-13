class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    def add_wrap(self):
        self.total_cost = 6
        self.items.append("wrap")
        print("Added wrap")
    # implement methods for menu items
