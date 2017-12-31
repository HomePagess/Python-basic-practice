# 关键字参数
def saysome(name,word):
    print(name+'->'+word)
saysome('潘俊','让变成改变世界')
saysome(word='让变成改变世界',name='潘帅')

# 默认参数
def saysome(name='潘帅',word='让编程改变世界'):
    print(name+'->'+word)
saysome()

# 可变参数（收集参数）
def test(*params):
    print('参数的长度是：',len(params))
    print('第二个参数是：',params[1])
test(1,'panshuai',3,56,4,78,12)