import csv
from datetime import datetime as dt

csv_bd = []
id_count = 0


def read_data():
    global csv_bd
    global id_count
    with open('Notepad.csv', 'r', encoding='utf-8', ) as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            csv_bd.append(row)
            if int(row['id']) > id_count:
                id_count = int(row['id']) 
    
 

def show_data():
    global csv_bd, id_count       
    print('СПИСОК ЗАМЕТОК:\nid Заголовок Содержание Дата создания:')
    print('-------------------------------------------------------')
    for row in csv_bd:
        print("; ".join(row.values()))   
    print('')
  

def search_data(word):
    global csv_bd
    count = 0
   
    for row in csv_bd:
        for item in row.values(): 
            if word.casefold() in item.casefold():   
                print("; ".join(row.values()))
                count += 1            
    if count <= 0:
        print('Данные не обнаружены')

def search_datetime(date):
    global csv_bd
    count = 0
    # datetime.strptime(line.strip(), '%d.%m.%Y')
#     date_string = '21 September. 1999'
    # date_object = datetime.strptime(date_string, '%d %B. %Y')
    # print(date_object, type(date_object))
    for row in csv_bd:
        for item['date'] in row:
            item_convert =  dt.strptime(item['date'].strip(), "%d-%m-%Y %H:%M:%S")
            if date in item_convert:   
                print("; ".join(row.values()))
                count += 1            
    if count <= 0:
        print('Данные не обнаружены')

def new_note(new_data):
    global id_count    
    new_id_count = id_count + 1
    new_data['id'] = new_id_count
    now = dt.now()
    new_data['date'] = now.strftime("%d-%m-%Y %H:%M:%S") 
    print(new_data)
    with open('Notepad.csv', 'a', encoding='utf-8') as file:
        field_names = ['id', 'title', 'text', 'date']
        writer = csv.DictWriter(file, fieldnames=field_names, delimiter=';')
        writer.writerow(new_data)
    print('Заметка добавлена')
    

def change_data(id_change, key_change):
    global csv_bd   
    for i in csv_bd:
        if id_change == i['id']:
            i[key_change] = input('Введите новые данные: ')
            break
    with open('Notepad.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'text', 'date'], delimiter=';')
        writer.writeheader()
        for j in csv_bd:
            writer.writerow(j)
    print('Данные успешно изменены')
            
    

def delete_data(id_del):
    global csv_bd
    global id_count    
    new_bd = []
    for i in csv_bd:
        if id_del != i['id']:
            new_bd.append(i)
    
            with open('Notepad.csv', 'w', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'title', 'text', 'date'], delimiter=';')
                writer.writeheader()
                id_count = 1
                for j in new_bd:
                    j['id'] = id_count 
                    writer.writerow(j)
                    id_count += 1
        else:
            print(f'Заметка {id_del} успешно удалена из блокнота')
    csv_bd = new_bd
    
