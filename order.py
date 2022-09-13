class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')
    
    def add_shake(self):
        self.total_cost += 4
        self.items += ['shake']
        print('Added shake')

    # implement methods for menu items
