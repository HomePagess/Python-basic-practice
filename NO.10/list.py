member=['小甲鱼',1,3,'荷叶','小布丁']
print(member)
# 添加元素
member.append('panshuai')
print(member)
print(len(member))
# 扩展元素
member.extend(['天蚕土豆',520])
print(member)
# 插入元素
member.insert(0,'tongtong')
print(member)
# 获取元素
print(member[1])
# 调换元素
temp=member[1]
member[1]=member[2]
member[2]=temp
print(member)
# 删除元素1
member.remove('荷叶')
print(member)
# 删除元素2  删除整个列表：del member 
del member[1]
print(member)
# 删除元素3 pop() 默认删除最后一个元素 pop(1):移除编号为3的元素 pop(-1)一处倒数第二个元素
member.pop()
print(member)
# 列表分片
print(member[1:3])
print(member[:3])
print(member[:])