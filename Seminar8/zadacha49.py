'''
Задача №49. Решение в группах Создать телефонный справочник с возможностью 
импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона 
- данные, которые должны находиться в файле. 
1. Программа должна выводить данные 
2. Программа должна сохранять данные в текстовом файле 
3. Пользователь может ввести одну из характеристик для поиска определенной записи
(Например имя или фамилию человека)
'''

import json


def json_load():
    try:
        with open("data_file.json", "r", encoding="utf-8") as read_file:
            phonebook = json.load(read_file)
    except:
        phonebook = {
            "дядя Ваня": {
                'phones': [1234567, 3216457],
                'birthday': '01.09.1960',
                'email': "vanya@mail.ru"
            },
            "дядя Вася": {
                'phones': [6543217]
            }
        }
    return phonebook

def save():
    with open("data_file.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Контакт был успешно сохранен")

def change():
    name_to_change = input("Введите имя контакта: ")
    lower_sized_name = name_to_change.lower()
    for contact_name in phonebook.keys():
        if lower_sized_name == contact_name.lower():
            new_name = input("Введите новое имя: ")
            phonebook[new_name] = phonebook.pop(contact_name)
            save()
            print("Имя контакта успешно изменено.")
            return
    print("Контакт с таким именем не найден.")

def add():
    new_name_to_add = input("Введите имя контакта: ").lower()
    if new_name_to_add in phonebook:
        new_phone = input("Введите номер телефона: ")
        phonebook[new_name_to_add]['phones'].append(new_phone)
        save()
        print("Номер успешно добавлен!")
    else:
        new_contact = input("Контакт с данным именем не найден, создать новый? (y/n) ")
        if new_contact.lower() == 'y':
            new_phone = input("Введите номер телефона: ")
            phonebook[new_name_to_add] = {'phones': [new_phone]}
            save()
            print("Контакт успешно создан!")
        else:
            print("Контакт не добавлен.")

def search():
    contact_name = input("Введите имя контакта для поиска: ").lower()
    found_contacts = []
    for key in phonebook:
        if contact_name in key.lower():
            found_contacts.append(key)
    if found_contacts:
        print("Найденные контакты:")
        for key in found_contacts:
            print(f"{key}: {phonebook[key]}")
    else:
        print("Контакт не найден.")


phonebook = json_load()

while True:
    command = input("Введите команду: ")
    if command == "/help":
        print("Список команд: ... ")
    elif command == "/show":
        print(phonebook)
    elif command=="/add":
        add()
    elif command == "/change":
        change()
    elif command == "/save":
        save()
    elif command == "/delete":
        contact = input("Введите имя контакта, который надо удалить: ").lower()
        for key in phonebook.keys():
            if key.lower() == contact:
                del phonebook[key]
                save()
                print("Контакт успешно удален!")
                break
        else:
            print("Такого контакта нет в книге!")
    elif command == "/search":
        search()
    elif command == "/stop":
        break
    else:
        print("Такой команды нет, изучите команды через запрос /help")