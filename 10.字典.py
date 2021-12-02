# 字典
# 字典用{}创建
d = {}#创建一个空字典

# 创建一个包含有数据的字典
# 语法：
#   {key:value,key:value,key:value}
#   字典的值可以是任意对象
#   字典的key可以是任意的不可变对象（int,str,bool,tuple.....），一般都是使用str
#       字典的key是不能重复的，如果出现重复的，后面会替换掉前面的
d = {'name':'孙悟空','age':'18','gender':'男'}
print(d,type(d))

# 需要根据键来获取值
print(d['name'],d['age'],d['gender'])


# 如果使用了字典中不存在的键，会报错：
# print(d['hello']) KeyError:'hello'