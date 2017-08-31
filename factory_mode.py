"""
##            工厂模式
##  举例1： KFC点餐系统（分为汉堡、小吃、饮料）
##  汉堡（芝士汉堡、 鸡肉汉堡）
##  小吃（薯条、鸡腿、 蛋挞）
##  饮料（可乐、奶）
##
##
"""


class HamBurger(object):
    # name = ''
    # price =0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class CheeseBurger(HamBurger):
    def __init__(self):
        self.name = 'Cheese'
        self.price = 20.0


class ChickenBurger(HamBurger):
    def __init__(self):
        self.name = 'Chicken'
        self.price = 17.0


class Snack(object):
    # name = ''
    # price = 0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Chips(Snack):
    def __init__(self):
        self.price = 10.0
        self.name = 'Chips'


class Drumstick(Snack):
    def __init__(self):
        self.price = 8.0
        self.name = 'Drumstick'


class Eggtart(Snack):
    def __init__(self):
        self.price = 4.0
        self.name = 'Eggtart'


class Beverages(object):
    # name = ''
    # price = 0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Coke(Beverages):
    def __init__(self):
        self.name = 'Coke'
        self.price = 7.0


class Milk(Beverages):
    def __init__(self):
        self.name = 'Milk'
        self.price = 6.0

"""
##        简单工厂模式直接访问
"""

# class simpleFactory():
#     @staticmethod
#     def createFood(foodClass):
#         food = foodClass()
#         return food

# cheese = simpleFactory.createFood(CheeseBurger)
# print(cheese.get_price(), cheese.get_name())


"""
##              抽象工厂模式
##
"""
class FoodFactory:
    type = ''
    def createFood(self, foodClass):
        try:
            if isinstance(foodClass, object):
                print('Type:', self.type)
                self.food = foodClass()
            else:
                print('False')
                self.food = False
            return self.food

        except TypeError as e:
            print(e)


class BurgerFactory(FoodFactory):
    def __init__(self):
        self.type = 'BURGER'


class SnackFactory(FoodFactory):
    def __init__(self):
        self.type = 'SNACK'


class BeverageFactory(FoodFactory):
    def __init__(self):
        self.type = 'BEVERAGE'


if __name__ == '__main__':
    #汉堡食物工厂
    burger = BurgerFactory()
    cheese = burger.createFood(CheeseBurger)
    print(cheese.get_price(),cheese.get_name())

    chicken = burger.createFood(ChickenBurger)
    print(chicken.get_price(), chicken.get_name())
    chicken.set_price(29.0)
    print(chicken.get_price())

    #小吃食物工厂
    snack = SnackFactory()
    chips = snack.createFood(Chips)
    print(chips.get_price(), chips.get_name())

    egg = snack.createFood(Eggtart)
    print(egg.get_price(), egg.get_name())


    #饮料食物工厂
    beverage = BeverageFactory()
    coke = beverage.createFood(Coke)
    print(coke.get_price(), coke.get_name())

    milk = beverage.createFood(Milk)
    print(milk.get_price(), milk.get_name())

    milk = beverage.createFood(False)
    if milk:
        print(milk.get_price(), milk.get_name())



