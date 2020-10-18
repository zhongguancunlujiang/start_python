###本文主要讲python单例模式的两种实现
#第一种是常规的实现
#第二种是具有python风格的实现，采用装饰器方法
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

#第二种 待完善

a1 = Single()
a2 = Single()
print(id(a1))
print(id(a2))
