# 创建字典
# 使用dict()函数来创建字典
# dict()创建的键值对，参数名就是键，参数名就是值（这种方式创建的字典，key都是字符串）
d = dict(name='孙悟空',age='18',gender='男')
print(d)

# 也可以将一个包含双值序列的序列转为字典
# 双值序列，序列中只有两个值，[1,2]('a',3)'ab'
# 子序列，如果序列中的袁术也是序列，那么我们就称这个元素为子序列
# [(1,2),(3,5)]
d = dict([('name','孙悟空'),('age','18')])
print(d,type(d))

# len()获取字典中键值对的个数
print(len(d))

# in and not in 
# in 检查字典中是否包含指定的键
# not in 检查字典中是否不包含指定的键
print('hello' in d)

# 获取字典中的值，根据键来获取值
# 语法：d[key]
print(d['name'])

# 通过[]来获取值时，如果键不存在，会抛出异常KeyError
# get(key[,default]),该方法用来根据键来获取字典中的值
print(d.get('name'))
print(d.get('hello'))
# 如果key不存在，则返回none
# 也可以指定一个默认值，来作为第二个参数，这样获取不到值时将会返回默认值
print(d.get('hello','默认值'))

# 修改字典
# d[key]=value
d['name']='刘德华'#修改字典的key-value
d['hello']='香港'#添加字典的key-value

# setdefault(key[,default])可以用来向字典中添加key-value
#   如果key已经存在于字典中，则返回key的值，不会对字典做任何操作
#   如果key不存在，则向字典中添加这个key，并设置value
result = d.setdefault('name','猪八戒')
result = d.setdefault('node','猪八戒')
print('result = ',result)
print(d)

# update([other])
# 将其它字典中的key-value添加到当前字典中
# 如果有重复的key，后面会替换前面的key的value
d2 = dict(addr = '日本',news = '酷狗')
d.update(d2)
print(d)

# 删除
# del删除字典中的key-value
print(d)
del d['name']

# popitem()
# 随机删除字典中的键值对，一般会删除最后一个键值对
# 删除之后，它会将删除的key-value返回
# 返回值返回的是一个tuple=('key','value')
# 删除空字典会抛出异常
d.popitem()

# pop(key[,default])
# 根据key删除字典中的key-value
# result = d.pop('age')
# 将会返回删除的value
# 如果删除不存在的key，会抛出异常
#   如果指定了默认值，再删除不存在的key时，不会报错，而是直接返回默认值
result = d.pop('addr')
result = d.pop('aa','这是一个默认值')
print(d)


# clear用来清空字典


# copy()
# 该方法用于对字典进行浅复制\
# 复制以后对象，和原对象是独立的，修改一个不会影响另一个
# 浅复制只会简单复制对象内部的值，如果值也是一个可变对象，这个可变对象不会被复制

# a = dict(a='c',b='d',c='c')
a = {'a':{'name':'猪八戒','age':'18'},'b':2,'c':3}
# d = a
a2 = a.copy()
a2['a']['name'] = '周星驰'


print(d,id(d))
print(a,id(a))
print(a2,id(a2))


