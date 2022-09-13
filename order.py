class Order:
    def __init__(self):
        self.total_cost = 0
        self.items  = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    # implement methods for menu items

    def add_lemonade(self):
        self.total_cost += 7.5
        self.items += ["lemonade"]
        print("Added lemonade")

    def add_salad(self):
        self.total_cost += 20
        self.items.append('salad')
        print("Adding salad...")
        
    def add_kidmeal(self):
        self.total_cost += 8
        self.items += ["kid's meal"]
        print("Added kid's meal")

    def add_cookie(self):
        self.total_cost += 3.0
        self.items+= ('cookie')
        print("Added cookie")
        
    def add_wrap(self):
        self.total_cost = 6
        self.items.append("wrap")
        print("Added wrap")
