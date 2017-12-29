tuple1=(1,2,3,4,5,6,7,8)
print(tuple1[1])
# 元组逗号是关键，括号不是关键
temp=1,2,3
print(type(temp))
print(temp)
# 元组索引，截取
print(tuple1[1:3])
print(tuple1[2])
# 修改元组
temp1=('我','是','帅','哥')
temp1=temp1[:2]+('大',)+temp1[2:]
print(temp1)