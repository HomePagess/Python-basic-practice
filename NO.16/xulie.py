# 序列
# 1.list()把对象转换为列表
a=list()
print(a)
b='i love you'
b=list(b)
print(b)
c=(1,3,4,6,9)
c=list(c)
print(c)
# 2.tuple()把对象转为元组 和list()一样

# len() 返回长度  min() max() 返回最小值和最大值

# sum() 返回总和
print(sum(c))
print(sum(c,8))

# sorted() 排序
print(sorted(c))

# reversed()
print(list(reversed(c)))

# enumerate() 加上索引值组成元组
print(list(enumerate(c)))

# zip()
d=[1,2,3,4]
e=[2,3,4,5,6,7,8]
print(list(zip(d,e)))
