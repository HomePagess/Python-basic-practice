list1=[123]
list2=[234]
print(list1>list2)

list1=[123,456]
list2=[234,123]
print(list1>list2)

list3=[123,456]
a=(list1<list2)and(list1==list3)
print(a)

list4=list1+list2
print(list4)

print(list3*3)

print(123 in list3)

list5=[123,['mudan','pan'],456]
print('pan' in list5)
print('pan' in list5[1])
print(list5[1][1])

print(dir(list))

print(list3.index(456))

list6=[1,3,5,2,8,4]
list6.reverse()
print(list6)

list6.sort()
print(list6)