class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    def addChickenSandwich(self):
        self.total_cost += 5
        self.items += ["Chicken sandwich"]
        print("Added chicken sandwich")
    # implement methods for menu items
