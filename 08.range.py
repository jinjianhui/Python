# range()是一个函数，可以用来生成一个自然数的序列
r = range(8) #生成一个[0,1,2,3,4,5,6,7]
print(list(r))
# 该函数需要三个参数
#  1、起始位置（可以省略，默认是0）
#  2、结束位置
#  3、步长（可以省略，默认是1）

# 通过range()可以创建一个指定次数的for循环
# for循环除了创建方式之外，其余的都和while一样
for i in range(20):
    print(i)


