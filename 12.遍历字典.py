# 遍历字典
# keys()该方法会返回所有的key
# 该方法会返回一个序列，序列中报错有字典的所有的键
a = {'a':{'name':'猪八戒','age':'18'},'b':2,'c':3}
for i in a.keys():
    print(i, a[i])

print(a.keys)
# values()
# 返回一个序列，序列中保存有字典的左右的值
for v in a.values():
    print(v)
# items()
# 该方法会返回字典中所有的项
# 它会返回一个序列，序列中包含双值子序列
# 双值分别是，字典中的key和value

for k,v in a.items():
    print(k,'=',v)