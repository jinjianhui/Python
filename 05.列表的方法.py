# 列表的方法
stus = ['孙悟空','猪八戒','沙和尚']
print("原列表：",stus)

# s.append()
stus.append('唐僧')
# 默认添加在序列的最后
print("修改后：",stus)

# s.insert(i,j)
# i写入添加的位置
# j写入添加的元素
stus.insert(2,'刘德华')

# extend()
# 使用新的序列来扩展当前序列
# 需要一个序列在作为参数，它会将该序列的元素添加到到当前列表中
stus.extend(['白骨精','金角大王'])
print(stus)

# clear()清空
# stus.clear()

# pop()
# 根据索引删除并返回指定的元素
stus.pop(2)#删除索引为2的元素
result = stus.pop(2)
print("删除的元素为：",result)
print("修改后：",stus)

# remove()
# 删除指定值的元素
stus.remove('猪八戒')
print(stus)#如果相同值的元素有多个，默认删除第一个元素

# reverse()
# 用来反转列表
stus.reverse()
print(stus)

# sort()
# 用来对元素进行排序
# 默认进行升序排列
# sort(reverse=Ture)降序排列
my_list = ['asdasfasgjkfhas']
my_list.sort()
print(my_list)
