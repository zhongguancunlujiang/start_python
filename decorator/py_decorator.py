#python装饰器相关
#1、何谓装饰器
#2、常见使用场景等
"""
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
Python中的装饰器是通过利用闭包实现的。装饰器语法糖@
闭包函数必须返回一个函数对象；闭包函数返回的哪个函数必须引用外部传进来的变量（不能是全局变量）
经常用于有切面需求的场景，如一些公共性的边缘服务功能，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
有了装饰器，就可以抽离出大量与函数功能本身无关的重复代码并继续重用。
"""

#清理redis缓存的场景，如增删改接口添加一个缓存清理装饰器
from functools import wraps
def clear_cache(key):
    def warpers(fun):
        @wraps(fun)
        def inner(*args, **kwargs):
            print(key)
            print(*args)
            result = fun(*args, **kwargs)
            return result
        return inner
    return warpers

@clear_cache("redis_key")
def query_comdt(snbid, status):
    print("query comdt")

if __name__ == "__main__":
    query_comdt("lujaing", 20000)
