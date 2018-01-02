# 斐波那契数列的迭代实现
def fab(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print('输入有误')
        return -1
    while (n-2)>0:
        n3=n1+n2
        n1=n2
        n2=n3
        n-=1
    return n3
result=fab(20)
if result!=-1:
    print('总共有%d对小兔子诞生'%result)


# 斐波那契数列的递归实现  n越大,结果越慢出现
def digui(n):
    if n<1:
        print('输入有误')
        return -1
    if n==1 or n==2:
        return 1
    else:
        return digui(n-1)+digui(n-2)
result=digui(20)
if result!=-1:
    print('总共有%d对小兔子诞生'%result)
# 分治思想