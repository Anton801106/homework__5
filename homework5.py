# "Неизменяемые и изменяемые объекты. Кортежи"
immutable_var = ('map', 'pen', True, 5, 'pool')
print(immutable_var)
print(type(immutable_var)) # корртежи относятся к неизменяемым типам данных:
# 'tuple' object has no attribute 'pop', 'tuple' object has no attribute 'append'
mutable_list = ['boy', 'girl', 'mam', ' dad', 'son', 'doughter']
mutable_list .remove('boy')
print(mutable_list)
mutable_list .append(8)
print(mutable_list)
mutable_list .extend('unt')
print(mutable_list)
mutable_list .extend(['sister', 'brother', 2])
print(mutable_list)
print(mutable_list[0:4])
print(mutable_list)
print('boy' in mutable_list)
print(mutable_list)
print('mam' in mutable_list)
