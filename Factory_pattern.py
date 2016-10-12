# coding:utf-8
'''
我们考虑一个情况。
一个工厂生成玩具车跟洋娃娃，这个工厂现在正在生成玩具车。
CEO决定，现在改成生成洋娃娃。
在这种情况下，CEO就是我们所说的client，玩具车或洋娃娃就是objects。
CEO决定生产，他只需要跟工厂说（调用工厂的方法），然后可以改变工程的行为。

工厂模式分为
简单工厂模式 Simple Factory pattern:
工厂方法模式 Factory method pattern:
抽象工厂模式 Abstract Factory pattern:

'''

'''
简单工厂模式

'''

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


# if __name__ == '__main__':
#     ff = ForestFactory()
#     animal = input("Which animal should make_sound Dog or Cat?\n")
#     ff.make_sound(animal)

'''
工厂方法模式
'''


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


# if __name__ == '__main__':
#     profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]\n")
#     profile = eval(profile_type.lower())()
#
#     print("Creating Profile..", type(profile).__name__)
#     print("Profile has sections --", profile.getSections())


'''
抽象工厂模式
'''


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()

# 素食披萨
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass

# 非素食披萨
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            # NonVegPizza 依赖于 VegPizza
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()

'''
Prepare  DeluxVeggiePizza
ChickenPizza  is served with Chicken on  DeluxVeggiePizza
Prepare  MexicanVegPizza
HamPizza  is served with Ham on  MexicanVegPizza
'''