# def recursion():
    # return recursion()
# 错误，执行永远不会停下来

# 求5的阶层

# 普通版本
def factorial(n):
    result=n
    for i in range(1,n):
        result *= i
    return result
# print(factorial(5))

number=int(input('请输入一个正整数: '))
result=factorial(number)
print("%d的阶层是:%d" % (number,result))

# 递归版本
def digui(n):
    if n==1:
        return 1
    else:
        return n*digui(n-1)
number = int(input('请输入一个正整数: '))
result=digui(number)
print('%d的阶乘是:%d'%(number,result))
