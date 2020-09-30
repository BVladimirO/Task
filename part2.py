   #Просим пользователя ввести номер пользователя
user_number=input('Введите номер пользователя, которого нужно переместить в конец:')
print('Список до изменения')
#Список пользователей
user_list=['name:Иван age:20 account:login : Ivan password : q1', 
'name:Петр age:21 account:login : Peter password : q2', 
'name:Ольга age:22 account:login : Olga  password : q3', 
'name:Анна age:23 account:login : Anna password : q4',
''
]
#Проверка ввода 
if user_number == '1':
    print(user_list)
    user_list.sort(key='name:Иван age:20 account:login : Ivan password : q1'.__eq__)
    print('Список после изменения')
    print(user_list)
    print('Пользователь с именем Иван перемещен в конец')
if user_number == '2':
    print(user_list)
    user_list.sort(key='name:Петр age:21 account:login : Peter password : q2'.__eq__)
    print('Список после изменения')
    print(user_list)
    print('Пользователь с именем Петр перемещен в конец')
if user_number == '3': 
    print(user_list)
    user_list.append(user_list.pop(user_list.index('name:Ольга age:22 account:login : Olga  password : q3',)))
      #user_list.sort(key='name:Ольга age:22 account:login : Olga password : q3'.__eq__)
    print('Список после изменения')
    print(user_list)
    print('Пользователь с именем Ольга перемещен в конец')
if user_number == '4':
    print(user_list)
    user_list.sort(key='name: Анна age:23 account:login : Anna password : q4'.__eq__) 
    print('Список после изменения')
    print(user_list)
    print('Пользователь с именем Анна перемещен в конец')
