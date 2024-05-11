
# book_phones = {
#   'Квам-Дамн': '-79899899889',
#   'Лук Скамворкер': '112',
#   'Петард Вейпер': '1',
#   'Лия Моргала': '+09998765432',
#   'Эдуард Скамворкер': '0'
# }
# action = input('Выбери действие: 1 - показать, 2 - добавить, 3 - изменить, 4 - удалить контакт,  5 — Показать все имена в книге, 6 — Показать все номера в книге ')
# if action == '1':
#     name = input('Имя: ')
#     if name in book_phones:
#         print(book_phones[name])
#     else:
#         print('Нет в телефонной книге')
# elif action == '2' or action == '3':
#     name = input('Имя: ')
#     phone = input('Телефон: ')
#     book_phones[name] = phone
#
#     for key in book_phones:
#         print(f'{key}: {book_phones[key]}')
#
# elif action == '4':
#     name = input('Имя: ')
#     if name in book_phones:
#         del book_phones[name]
#     else:
#         print('Нет в телефонной книге')
#     for key in book_phones:
#         print(f'{key}: p{book_phones[key]}')
#
# elif action =="5":
#     # name = input('Имя: ')
#     # if name in book_phones:
#         for name in book_phones:
#             print(name)
#
#
#
# elif action =="6":
#     for name in book_phones.values():
#             print(name)


# # Этот код - подсказка. Если он тебе мешает - удали.
# white_list = set()  # Множество, в котором будет храниться "белый список"
# answers = set()     # Множество будущих разрешенных ответов
#
# white_request = ' '   # Объявление переменной, через которую будут заноситься пункты белого списка
# request = ' '         # Объявление переменной, через которую будут заноситься пункты запросов учеников
#
# # Допиши решение везде, где стоит "..."
#
# # Работает, пока в white_request не ввели пустую строку
#
# # Работает, пока в request не ввели пустую строку
# while True:
#     white_request = input('введи:')
#     if white_request == "":
#         break
#     white_list.add(white_request)
#
# while True:
#     answer = input('введи:')
#     if answer == "":
#         break
#     answers.add(answer)
#
# # Перебирает множество разрешенных ответов
# for answer in answers:
#   if answer in white_list:
#       print(answer)

# Продолжи писать решение

# import  turtle
#
# def turtles(colors, x, y, dot):
#     turtle.goto(x,y)
#     turtle.dot(34, colors)
#
# turtles("red",23,45,56)
# turtle.mainloop()


# print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление')
# choice = input('Введите номер действия: ')
# if choice == 1 or 2 or 3 or 4:
#     a = int(input('Введи первое число: '))
#     b = int(input('Введи второе число: '))
# else:
#     print("Такого действия нет.")
#
# def sum_nums(a, b):
#     return a + b
#
# if choice == 1:
#     sum_nums(

# data = ['55.435656', '23.678546', '76.542465', '10.43433345', '84.323454524', '43.546784132']
# new_data=map(float, data)
# for i in new_data:
#     print(i)
# new_data=list(new_data)
# print(new_data)


# num1 = int(input("Введи число 1: "))
# num2 = int(input("Введи число 2: "))
# list = []
# if num1>num2:
#     num1, num2 = num2, num1
#
# for i in range(num1,num2):
#     if i%3==0:
#         list.append(i)
#
#
#
# print(list)
import tkinter as tk
import file_connection
from tkinter import messagebox

# Содержимое статей (названия и текст статей)
articles = file_connection.get_articles()

current_article = None

# Функция для отображения выбранной статьи
def show_article():
    global current_article
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        current_article = title

        # Очистка окна и добавление текста статьи
        text.delete(1.0, tk.END)
        text.insert(tk.END, articles[title])

        # Очистка окна и добавление названия и текста статьи
        title_label.config(text=title)
        title_label.pack()
        text.pack()
        back_button.pack()
        listbox.pack_forget()
        delete_button.pack_forget()
        read_button.pack_forget()
        add_button.pack_forget()


# Функция для возврата к списку статей
def go_back():
    global current_article
    current_article = None

    # Очистка текста статьи и названия, отображение списка статей
    text.delete(1.0, tk.END)
    title_label.config(text="")
    listbox.pack(fill=tk.BOTH)
    text.pack_forget()
    title_label.pack_forget()
    back_button.pack_forget()
    read_button.pack()
    add_button.pack()
    delete_button.pack()


# Функция для удаления статьи
def delete_article():
    global current_article, articles, listbox
    selected_index = listbox.curselection()
    if selected_index:
        title = listbox.get(selected_index)
        current_article = title
        answer = messagebox.askyesno("Удаление", "Вы действительно хотите удалить эту статью?")
        if answer:
            go_back()
            del articles[title]
            listbox.delete(selected_index)
            file_connection.delete_article(title)


# Функция для добавления новой статьи
def add_article():
    global articles

    def save_new_article():
        new_title = entry_title.get()
        new_text = text.get("1.0", tk.END)
        if new_title and new_text:
            articles[new_title] = new_text
            listbox.insert(0, new_title)
            file_connection.save_article(new_title, new_text)
            add_window.destroy()
            show_article()

    add_window = tk.Toplevel(root)
    add_window.title("Добавить статью")

    label_title = tk.Label(add_window, text="Введите название статьи:")
    label_title.pack()
    entry_title = tk.Entry(add_window)
    entry_title.pack()

    label_text = tk.Label(add_window, text="Введите текст статьи:")
    label_text.pack()
    text = tk.Text(add_window, wrap=tk.WORD)
    text.pack()

    save_button = tk.Button(add_window, text="Сохранить", command=save_new_article)
    save_button.pack()


# Создание окна
root = tk.Tk()
root.title("Кошко-вики")
root.geometry("600x500")  # Фиксированный размер окна

# Создание списка статей
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH)

# Заполнение списка статьями
for article in articles:
    listbox.insert(tk.END, article)

# Создание текстового виджета для отображения текста статьи (изначально скрыт)
text = tk.Text(root, wrap=tk.WORD)
text.pack()
text.pack_forget()

# Создание виджета Label для отображения названия статьи (изначально скрыт)
title_label = tk.Label(root, text="", font=("Helvetica", 14))
title_label.pack()
title_label.pack_forget()

# Создание кнопки "Назад" (изначально скрытой)
back_button = tk.Button(root, text="Назад", command=go_back)
back_button.pack()
back_button.pack_forget()

# Создание кнопки "Прочитать"
read_button = tk.Button(root, text="Прочитать", command=show_article)
read_button.pack()

# Создание кнопки "Добавить статью"
add_button = tk.Button(root, text="Добавить статью", command=add_article)
add_button.pack()

delete_button = tk.Button(root, text="Удалить статью", command=delete_article)
delete_button.pack()

# Запуск приложения
root.mainloop()