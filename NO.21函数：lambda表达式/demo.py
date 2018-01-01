def ds(x):
    return 2*x+1
print(ds(5))

g=lambda x:2*x+1
print(g(5))

def add(x,y):
    return x+y
print(add(3,4))

f=lambda x,y:x+y
print(f(3,4))

# 1.省下函数定义过程
# 2.不需要考虑函数命名问题
# 3.简化代码的可读性


# 两个牛逼的BIF（内置函数）

# 1.filter（）过滤器 filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
print(filter(None,[1,0,False,True]))
# list(print(filter(None,[1,0,False,True])))
def odd(x):
    return x%2
temp=range(10)
show=filter(odd,temp)
print(list(show))

print(list(filter(lambda x:x%2,range(10))))

# 2.map() map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
print(list(map(lambda x:x*2,range(10))))


