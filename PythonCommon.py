#此文件主要记录一些python相关常考语法特性
#一、python各种数据类型的推导式

#1、字典推导式
#a、常考点：一句话实现字典的kev、value交换
temp_dict = {"cheng": 100, "du":200, "ok":300}
temp_dict = { value:key for key, value in temp_dict.items() }
print(temp_dict)
