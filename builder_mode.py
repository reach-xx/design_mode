"""
##            建造者模式
##  举例1： KFC点餐系统（分为汉堡、小吃、饮料）
##  汉堡（芝士汉堡、 鸡肉汉堡）
##  小吃（薯条、鸡腿、 蛋挞）
##  饮料（可乐、奶）
##
##  点餐清单： 汉堡、小吃、饮料
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


class Order():
    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print('Burger: ({name}) price: {price} '.format(name=self.burger.get_name(),
                                                                price=self.burger.get_price()))
        print('Snack: ({name}) price: {price} '.format(name=self.snack.get_name(),
                                                                price=self.snack.get_price()))

        print('Beverage: ({name}) price: {price} '.format(name=self.beverage.get_name(),
                                                                price=self.beverage.get_price()))

        print('Total Price: %d dollars'  %(self.burger.get_price()+
                                    self.snack.get_price()+
                                            self.beverage.get_price()))


class orderBuilder():
    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return Order(self)


class orderDirector():
    def __init__(self, order_builder):
        self.order_builder = order_builder

    def createOrder(self, burger, snack, deverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(deverage)
        return self.order_builder.build()


if __name__ == '__main__':
    # order_builder = orderBuilder()
    # order_builder.addBurger(CheeseBurger())
    # order_builder.addBeverage(Milk())
    # order_builder.addSnack(Eggtart())
    # order_new = order_builder.build()
    # order_new.show()
    order_directer = orderDirector(orderBuilder())
    order_1 = order_directer.createOrder(CheeseBurger(), Milk(), Eggtart())
    order_1.show()




