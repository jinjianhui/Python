# 创建列表，通过[]来创建列表
from typing import MutableMapping


My_List = []
print(My_List,type(My_List))
# 列表中存储的数据，称之为元素
# 一个列表中可以存储多个元素，也可以在创建列表时，来制定列表中的元素
# 向列表添加多个元素时，多个元素之间使用,隔开
My_List = [10,20,30,40,50]
print(My_List)

# 列表中可以保存任意的对象

My_List = [10,'hello',print]
print(My_List)

# 列表中的对象都会按照插入的顺序存储在列表中
# 获取列表中的数据，通过索引（index）来获取列表中的元素
# 索引是元素列表中的位置，列表中每一个元素都有一个索引
# 索引是从0开始计数的

# 通过索引来获取列表中的元素
# 语法：my_list[索引]
print(My_List[0])

# 获取列表的长度，列表中的个数
# 语法：len()，通过该函数可以获取列表的长度
print(len(My_List))





