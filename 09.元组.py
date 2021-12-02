# 元组 tuple
# 不可变的序列
# 操作方式基本上和列表时一直的
# 使用元组时，把元组当做一个不可变的列表
# 当我们希望数据不改变时，就使用元组

# 创建元组
# 使用()来创建元组
my_tuple = ()
print(type(my_tuple))

my_tuple = (1,2,3,4,5)
print(my_tuple[3])

# 当元组不是空元组是，括号可以省略
# 如果元组不是空元组，它里面至少有一个,
my_tuple = 1,
my_tuple = 1,2,3,4
print(my_tuple)

# 元组的解包（解构）
# 把每一个元素赋值给一个变量
a,b,c,d = my_tuple
# print('a =',a)
# print('b =',b)


a = 100
b = 200

print(a,b)
# 交换a和b的值，可以使用元组的解包
a , b = b , a
print(a , b)

# 对一个元组进行解包时，变量的数量必须对元组中的元素数量一致
# 也可以再变量前添加一个*，这样变量将会获取元组中所有的剩余数量
# 不能出现两个或者以上的*，否则会报错
a, b, *c = my_tuple
print(a,b)
print('c = ',c)