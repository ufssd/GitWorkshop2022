class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')
    def add_lemonade(self):
        self.items +=[ "Lemonade"]
        self.total_cost += 7.5
        print("Added lemonade!")

    def add_coke(self):
        self.items +=[ "Coke"]
        self.total_cost += 3
        print("Added coke!")

    def add_cold_brew_coffee(self):
        self.items +=[ "Cold Brew Coffee"]
        self.total_cost += 4.0
        print("Added Cold Brew!")

    def add_fries(self):
        self.items +=[ "Fries"]
        self.total_cost += 2.50
        print("Added fries!")

    def add_salad(self):
        self.items +=[ "Salad"]
        self.total_cost += 5.0
        print("Added salad !")

    def add_wrap(self):
        self.items += ["Wrap"]
        self.total_cost += 7.50
        print("Added wrap")

    def add_chicken_strips(self):
        self.items += ["Chicken Strips"]
        self.total_cost += 7.50
        print("Added Chicken Strips")
    
    def add_chicken_nuggets(self):
        self.items += ["Chicken Nuggets"]
        self.total_cost += 7.50
        print("Added Chicken Nuggets")

    def add_kids_meal(self):
        self.items += ["Kids Meal"]
        self.total_cost += 7.50
        print("Added kids meal")

    def add_mac_n_cheese(self):
        self.items += ["Mac n Cheese"]
        self.total_cost += 7.50
        print("Added mac n cheese")

    def add_chicken_biscuit(self):
        self.items += ["Chicken Biscuit"]
        self.total_cost += 7.50
        print("Added Chicken Biscuit")
    
    def add_fruit_cup(self):
        self.items += ["Fruit Cup"]
        self.total_cost += 3.00
        print("Added Fruit cup")

    def add_shake(self):
        self.items += ["Shake"]
        self.total_cost += 7.50
        print("Added shake")
    
    def add_frosted_lemonade(self):
        self.items += ["Frosted Lemonade"]
        self.total_cost += 7.50
        print("Added Frosted Lemonade")

    def add_cookie(self):
        self.items += ["Cookie"]
        self.total_cost += 2.50
        print("Added Cookie")

    def add_chicken_sandwich(self):
        self.items += ["Chicken Sandwich"]
        self.total_cost += 10.50
        print("Added Chicken Sandwich")

    # implement methods for menu items
