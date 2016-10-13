# coding:utf-8
class Printer():
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("[colorful]Printing  --", self.src, " from ", self.rootdir)
            else:
                print("[gray]Printing  --", self.src, " from ", self.rootdir)


# if __name__ == '__main__':  # Client code
#     printer = Printer('python3.5.doc', '/usr/bin/')
#     printer.preferences({'jod1': True})
#     printer.preferences({'jod2': False})
#     printer.execute()

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()


class Receiver:
    def action(self):
        print("Receiver Action")


class Invoker:
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


# if __name__ == '__main__':
#     # 接收者
#     recv = Receiver()
#     # 一个发送给接收者的命令
#     cmd = ConcreteCommand(recv)
#
#     # 接收命令，执行命令
#     invoker = Invoker()
#     invoker.command(cmd)
#     invoker.execute()


# 真实世界的例子
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

# ConcreteCommand
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()

# ConcreteCommand
class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

# Receiver
class StockTrade:
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")

# Invoker
class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == '__main__':
    # Client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # Invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
