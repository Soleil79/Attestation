
from data_view import *
from logger import * 



read_data()


def choice():
    print("Выберите действие:\n\
    1 - Показать все заметки;\n\
    2 - Найти заметку по параметрам;\n\
    3 - Добавить новую заметку; \n\
    4 - Изменить заметку; \n\
    5 - Удалить заметку; \n")
    ch = input("Введите цифру: ")

    if ch == '1':
        show_data()
        access_logger('Show all') 

    elif ch == '2':
        print('Выберите параметр поиска: \n\
        1 - По названию; \n\
        2 - По содержанию; \n\
        3 - По дате; \n')
        ch = input('Введите цифру: ')
        if ch == '1': search_data(input('Введите название заметки или его часть: \n'))
        elif ch == '2': search_data(input('Введите содержание заметки или его часть: \n'))
        elif ch == '3': search_datetime(input('Введите дату в формате число-месяц-год: \n'))
        else:  ErrorMessage()
        access_logger('Search a note')
            
    elif ch == '3':
        my_dict = {'id':'', 'title':'', 'text':'', 'date':''}
        for i in my_dict:
            if i != 'id' and i != 'date':
                my_dict[i] = input(f'Введите {i}: ')
        new_note(my_dict)
        access_logger('Add a note')

    elif ch == '4':
        show_data()
        choose = int(input('Что хотите поменять: \n\
            1 - заголовок; \n\
            2 - содержание; \n'))
        if choose in range(3):      
            keys = {1:'title', 2: 'text'}
            change_data(input('Введите ID записки: '), keys[int(choose)])
        else: ErrorMessage()
        access_logger('Change data')
    
    elif ch == '5':
        
        show_data()
        delete_data(input('Введите ID записки: ')) 
        access_logger('Delete a note')        
    
    else:
        ErrorMessage()
        
def ErrorMessage():
    print('Вы ввели не корректные данные! Нажмите Enter чтобы вернуться в главное меню или напишите end: ')
    user_ch = input('')
    if user_ch != 'end':
        choice()
    
        