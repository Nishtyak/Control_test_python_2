from os.path import exists
from csv import DictReader, DictWriter
import os
import datetime

def create_file():
    with open("notes.csv", "w", encoding='utf-8') as data:
        f_n_writer = DictWriter(data, fieldnames =[ 'id', 'Заголовок', 'Заметка' , 'Дата создания', 'Дата изменения'])
        f_n_writer.writeheader()

def record_note():
    lst = get_note()
    write_file(lst)

def get_note():
    info = []
    with open('notes.csv', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        notes = list(f_n_reader)
        if len(notes) == 0:
            id = 1
        else:
            id = int(notes[len(notes) - 1]['id']) + 1
    info.append(id)
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    info.append(title)
    info.append(body)
    time = str(datetime.datetime.today().strftime("%Y-%m-%d %H.%M"))
    info.append(time)
    info.append(time)
    return info

def write_file(lst):
    # with open('notes.csv', 'r+', encoding='utf-8') as f_n:
    #     f_n_reader = DictReader(f_n)
    #     res = list(f_n_reader)
    #     obj = {'id': lst[0], 'Заголовок': lst[1], 'Заметка': lst[2] } #, 'create_time': lst[3], 'edit_time': lst[4]
    #     res.append(obj)
    #     f_n_writer = DictWriter(f_n, fieldnames=[ 'id', 'Заголовок', 'Заметка']) # , 'create_time', 'edit_time'
    #     for el in res:
    #         f_n_writer.writerow(el)
    with open("notes.csv", "a", encoding='utf-8') as data:
      data.write(f'{lst[0]},{lst[1]},{lst[2]},{lst[3]},{lst[4]}\n')

def main():
    print("Создать заметку: create")
    print("Список заметок: read")
    print("Редактировать заметку: edit")
    print("Найти заметку по названию: name")
    print("Выборка по дате: time")
    print("Удалить заметку: delete")
    print("Для выхода: exit")

    while True:
        command = input("Введите команду: ")
        if command == 'exit':
            break
        elif command == 'create':
            if not exists('notes.csv'):
                create_file()
                record_note()
            else:
                record_note()

main()