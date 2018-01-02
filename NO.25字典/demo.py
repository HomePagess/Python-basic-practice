#创建字典
dict1={'小明':1001,'小红':1002,'小强':1003}
print(dict1)

dict2=[('name','小明'),('xuehao',1001)]
print(dict2)

dict3=dict((('小明',1001),('小红',1002),('小强',1003)))
print(dict3)

dict4=dict(小明='1001',小红='1002')
print(dict4)
dict4['小红']='1004'
print(dict4)
dict4['小强']='1003'
print(dict4)


# fromkey()方法
dict5={}
dict5.fromkeys((1,2,3))
print(dict5)
dict5.fromkeys((1,2,3),'number')
print(dict5)


