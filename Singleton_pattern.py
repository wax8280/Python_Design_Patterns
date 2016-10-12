# coding:utf-8

# normal
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# s = Singleton()
# print("Object created", s)
# s1 = Singleton()
# print("Object created", s1)


# Lazy instantiation
class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print(" __init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


# s = Singleton.getInstance()
# print("Object created", s)
# s1 = Singleton.getInstance()
# print("Object created", s1)

'''
在Python中所有的模块都是单例的。
Python中导入import步骤如下
1.检查是否已经导入
2.如果已经导入，返回该模块的实例(object for the module)。如果没有，导入并实例化它(imports and instantiates it)
'''

# The Monostate Singleton pattern
'''
单例模式要求每一个类只有一个实例，通常来说，我们更需要的是所有实例都共享同一个状态
Python中使用__dict__去存储对象的所有状态
'''


class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


# 我们也可以在__new__中调整
class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


# b = Borg()
# b1 = Borg()
# b.x = 4
# print("Borg Object 'b': ", b)  ## b and b1 are distinct objects
# print("Borg Object 'b1': ", b1)
# print("Object State 'b':", b.__dict__)  ## b and b1 share same state
# print("Object State 'b1':", b1.__dict__)

# 单例模式与元类
'''
元类是类的类(a class of a class)，这意味着类是元类的实例

Python里面万物皆对象。
a=5,type(a) 返回 <type 'int'> 意味着 a 是int类型
type(int) 返回 <type 'type'>  意味着 int 是type类型

我们可以用type生成一个类
A = type(name, bases, dict)
name：生成的类名
bases：基类
dict：类的字典，各种属性等
'''


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


# logger1 = Logger()
# logger2 = Logger()
# print(logger1, logger2)


# 实战
# 服务器应用就是一个很好的例子
# 大量的连接只需要一个实例，节省内存
# 防止冲突

import sqlite3


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()
print("Database Objects DB1", db1)
print("Database Objects DB2", db2)
