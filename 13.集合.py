# 集合
# 使用{}来创建
from typing import TYPE_CHECKING


s = {1,2,3,4,5,5,3,1,7,89,5,46}
print(s,type(s))

# 使用set()函数来创建集合
s = set()
print(s,type(s))
# set()可以将序列和字典转换为集合
s = set([1,2,3,4,54,5])
s = set('hello')
s = set({'name':'hello','age':'178'})
print(s,type(s))
# 使用in和not in 来检查集合中的元素
print('c' in s)

# 使用len() 来获取集合的长度
print(len(s))

# 使用add()向集合中添加元素
s.add('mm','sss')
print(s)

# 使用update()将一个集合中的元素添加到当前集合中
# update()可以传递序列或字典作为参数，字典只会使用键
s2 = set('world')
s.update(s2)
s.update('dhasidhasjklhd')
print(s)

# pop()随机删除集合中的一个元素
result = s.pop()

# remove()删除集合中指定的元素
s.remove('sss')
s.remove('1')

# clear()清空集合
s.clear()

# copy()对集合进行浅复制
