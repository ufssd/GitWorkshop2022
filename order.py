class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    def add_chicken_sandwich(self):
        self.total_cost+=5
        self.items.append("checken sandwich")
        print("Chicken burger added to order! :)))")
    # implement methods for menu items
