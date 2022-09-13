class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    def add_lemonade(self):
        self.total_cost += 7.5
        self.items += ["lemonade"]
        print("Added lemonade!")

    def add_chicken_sandwich(self):
        print("How would you like your chicken? Grilled or fried?")
        option = input()
        self.total_cost += 20.5
        self.items += [option + " chicken sandwich"]
        print(option + " chicken sandwich comin right up!")
            
    # implement methods for menu items
