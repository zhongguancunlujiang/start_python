###本文主要讲python单例模式的两种实现
#第一种是常规的实现
#第二种是具有python风格的实现，采用装饰器方法
##单例注意事项：
# 1、并发情况下的安全问题：加锁解决
# 2、具有python特性的装饰器实现
# 3、懒加载和饿汉式的区别：懒加载方法是使用的时候再初始化，内存更友好；饿汉式程序启动的时候就初始化好，效率更佳。
import threading
#第一种
class Single(object):
    _lock = threading.Lock()
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        if not hasattr(Single, "_instance"):  #_instance为单例类的实例成员，需要先判断是否已经初始化了
            with Single._lock:  #需要考虑并发情况下，避免重复初始化情况（做后端开发写任何代码首先要考虑是否有并发问题）
                if not hasattr(Single, "_instance"):
                    Single._instance = object.__new__(cls)
        return Single._instance

a1 = Single()
a2 = Single()
print(id(a1))
print(id(a2))

#第二种 利用python装饰器特性，面试中常考
def wrapper(cls):
    instance = {} #用来存放实例的字典
    _lock = threading.Lock()
    def inner(*args, **kwargs):
        if cls not in instance:
            with _lock:
                if cls not in instance:
                    instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return inner

@wrapper
class Singe_sec(object):
    def __init__(self):
        pass

a3 = Singe_sec()
a4 = Singe_sec()
print(id(a3))
print(id(a4))

#单例模式的应用场景，待补充