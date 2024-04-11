immutable_var = 1, 2, 'redis', True
print(immutable_var)

# immutable_var[0] = 2
# print(immutable_var)
# при запуске кода выдаёт ошибку, т.к элементы внутри кортежа не могут изменяться
# по причине того, что кортеж относится к неизменяемым коллекциям, а список - к изменяемым

mutable_list = [1, 2, [1, 2], 'leaf', False]
mutable_list[2] = 'Canada'
print(mutable_list)




