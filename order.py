class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    # implement methods for menu items
    def add_lemonade(self):
        self.total_cost += 7.5
        self.items += ["lemonade"]
        print('Added lemonade!')

    def add_nuggies(self):
        print('How many nuggies?')
        print('1. 1 nuggest')
        print('2. 35 nuggests')
        nugCount = int(input())
        if nugCount == 1:
            self.total_cost += 13
        if nugCount == 2:
            self.total_cost += 47
        self.items += ["chicky nuggies yum yum"]
        print('Added your chickie nuggies *spits on your face* uwu')