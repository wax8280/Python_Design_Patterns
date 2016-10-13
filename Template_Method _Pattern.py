# coding:utf-8
from abc import ABCMeta


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class iOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code")

    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program runing on runtime environment")


# iOS = iOSCompiler()
# iOS.compileAndRun()


from abc import ABCMeta, abstractmethod


class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print("Defining the Algorithm. Operation1 follows Operation2")
        self.operation2()
        self.operation1()


class ConcreteClass(AbstractClass):
    def operation1(self):
        print("My Concrete Operation1")

    def operation2(self):
        print("Operation 2 remains same")


class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()


client = Client()
client.main()
