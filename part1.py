key = input ('Введите ключ (name или account):' )

name= """ значение ключа name для юзера 1 = Иван
 значение ключа name для юзера 2 = Петр
 значение ключа name для юзера 3 = Ольга
 значение ключа name для юзера 4 = Анна
"""


if key == 'name':
   print(name)
if key == 'account':
   print(name)
if key== 'NaMe':
   print(name)      
elif key != 'name' and key != 'account' and key != 'NaMe':
   print('Введенный ключ не найден')    
number= input ('Введите порядковый номер:') 
user_list = [' ','Данные по юзеру №1:' +'\n'+ 'имя: Иван' + '\n' + 'возраст: 18' + '\n' + 'логин: Ivan' + '\n' + 'пароль: q1',
               'Данные по юзеру №2:' +'\n'+ 'имя: Петр' + '\n' + 'возраст: 19' + '\n' + 'логин: Peter' + '\n' + 'пароль: q2',
               'Данные по юзеру №3:' +'\n'+ 'имя: Ольга' + '\n' + 'возраст: 20' + '\n' + 'логин: Olga' + '\n' + 'пароль: q3',
               'Данные по юзеру №4:' +'\n'+ 'имя: Анна' + '\n' + 'возраст: 21' + '\n' + 'логин: Anna' + '\n' + 'пароль: q4'
              ]
              
if number == '1' :
    print(user_list[1])
    print('Средний возраст пользователей: 19.5')
elif number == '2' :
    print(user_list[2])
    print('Средний возраст пользователей: 19.5')
elif number == '3' :
    print(user_list[3])
    print('Средний возраст пользователей: 19.5')
elif number == '4' :
    print(user_list[4])
    print('Средний возраст пользователей: 19.5')
else:
    print('Пользователь с указанным номером не найден')




