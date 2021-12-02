#
stus = ['猪八戒','孙悟空','沙和尚','唐僧','蜘蛛精','白骨精']
# +和*
my_list = [1,2,3]+[4,5,6]
print(my_list)

my_list = [1,2,3]*2
print(my_list)

# in 和 not in
# in用来检查指定的元素是否在列表中，在则返回Ture，否则返回False
print('沙和尚'in stus)
print('牛魔王'not in stus)

# min() 获取列表中的最小值
# max() 获取列表中的最大值

arr = [1,23,4,99,100]
print(max(arr),min(arr))

# 两个方法（method），方法和函数基本上一样，只不过方法必须用过对象，方法（）的形式调用
# xxx.print() 方法实际上就是和对象关系紧密的函数
# s.index()获取指定元素在列表中第一次出现的索引
print(stus.index('沙和尚',3))#第二个参数3表示从第几个元素开始找，第三个位置，表示结束的位置
# 异常抛出：ValueError:'牛魔王'not in list
# s.count()
print(stus.count('沙和尚'))#统计元素出现的次数