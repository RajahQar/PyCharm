break_loop = False
class CoffeeMachine:
    def __init__(self):
        self.money_level = 550
        self.water_level = 400
        self.milk_level = 540
        self.bean_level = 120
        self.cup_level = 9
        self.state = "choosing an action"

    def print_status(self):
        print("The coffee machine has:")
        print(self.water_level, "of water")
        print(self.milk_level, "of milk")
        print(self.bean_level, "of coffee beans")
        print(self.cup_level, "of disposable cups")
        print(self.money_level, "of money")

    def make_drink(self, water, milk, beans, cost):
        if self.water_level >= water and self.milk_level >= milk and self.bean_level >= beans and self.cup_level >= 1:
            self.water_level -= water
            self.milk_level -= milk
            self.bean_level -= beans
            self.cup_level -= 1
            self.money_level += cost
            print("I have enough resources, making you a coffee!\n")
        else:
            # check for missing ingredient
            if self.water_level < water:
                fail_cause = "water"
            elif self.milk_level < milk:
                fail_cause = "milk"
            elif self.bean_level < beans:
                fail_cause = "beans"
            elif self.cup_level < 1:
                fail_cause = "cups"
            fail_msg = "Sorry, not enough " + fail_cause
            print(fail_msg)

    # The following 3 methods need to change in order to work with the get_action method and the state variable
    def buy(self, order):
        # print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino")
        # order = input("> ")
        if order == "1":
            # espresso: 250ml water, 16g beans, cost $4
            self.make_drink(250, 0, 16, 4)
        elif order == "2":
            # latte: 350ml water, 75ml milk, 20g beans, cost $7
            self.make_drink(350, 75, 20, 7)
        elif order == "3":
            # cappuccino: 200ml water, 100ml milk, 12g beans, cost $6
            self.make_drink(200, 100, 12, 6)
        elif order == "back":
            pass

    # def fill(self):
    #     # Ask how much to fill of each ingredient in order.  water milk bean cup
    #     print("Write how many ml of water do you want to add:")
    #     self.water_level += int(input("> "))
    #     print("Write how many ml of milk do you want to add:")
    #     self.milk_level += int(input("> "))
    #     print("Write how many grams of coffee beans do you want to add:")
    #     self.bean_level += int(input("> "))
    #     print("Write how many disposable cups of coffee do you want to add:")
    #     self.cup_level += int(input("> "))

    def get_action(self, action):
        if action == "back":
            self.state = "choosing an action"
        elif action == "exit":
            global break_loop
            break_loop = True
        elif self.state == "choosing a type of coffee":
            if action == "1":
                # espresso: 250ml water, 16g beans, cost $4
                self.make_drink(250, 0, 16, 4)
            elif action == "2":
                # latte: 350ml water, 75ml milk, 20g beans, cost $7
                self.make_drink(350, 75, 20, 7)
            elif action == "3":
                # cappuccino: 200ml water, 100ml milk, 12g beans, cost $6
                self.make_drink(200, 100, 12, 6)
            self.state = "choosing an action"
        elif self.state == "fill_water":
            self.water_level += int(action)
            self.state = "fill_milk"
            print("Write how many ml of milk do you want to add:")
        elif self.state == "fill_milk":
            self.milk_level += int(action)
            self.state = "fill_beans"
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "fill_beans":
            self.bean_level += int(action)
            self.state = "fill_cups"
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.state == "fill_cups":
            self.cup_level += int(action)
            self.state = "choosing an action"
        elif action == "buy":
            self.state = "choosing a type of coffee"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino")
        elif action == "fill":
            self.state = "fill_water"
            print("Write how many ml of water do you want to add:")
        elif action == "take":
            self.state = "none"
            print("I gave you $" + str(self.money_level))
            self.money_level = 0
        elif action == "remaining":
            self.state = "choosing an action"
            self.print_status()
        if self.state == "choosing an action":
            print("Write action (buy, fill, take, remaining, exit):")


coffee_machine = CoffeeMachine()
print("Write action (buy, fill, take, remaining, exit):")
while not break_loop:
    coffee_machine.get_action(input("> "))

