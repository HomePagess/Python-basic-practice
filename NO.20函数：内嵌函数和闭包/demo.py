# 内嵌函数（内部函数）
def fun1():
    print('fun1()正在被调用')
    def fun2():
        print('fun2()正在被调用')
    fun2()
fun1()

# 闭包 如果一个内部函数对外部函数的变量进行调用了，那么就说这个内部函数是闭包
def funX(x):
    def funY(y):
        return x * y
    return funY
i=funX(8)
print(i)
print(type(i))
print(i(5))
print(funX(8)(5))

# 会报错
# def fun3():
#     x=5
#     def fun4():
#         x*=x
#         return x
#     return fun4()
# fun3()

def fun5():
    x=[5]
    def fun6():
        x[0]*=x[0]
        return x[0]
    return fun6()
print(fun5())


def fun3():
    x=5
    def fun4():
        nonlocal x           
        x*=x
        return x
    return fun4()
fun3()
