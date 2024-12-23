#username="Имя пользователя"                                  #здесь будет храниться имя пользователя
#title="Заголовок заметки"                                    #здесь будет храниться заголовок заметки
#content="Описание заметки"                                   #десь будет храниться описание заметки
#status="Cтатус заметки"                                      #здесь будет храниться статус заметки
#created_date='Дата создания заметки, формат: 21-12-2024'     #дата создания заметки
#issue_date='Дедлайн (срок истечения), Формат: 22-12-2024'    #дедлайн по заметке

username=input("Добрый день.Укажие Ваше имя: ")
print(f"{username}, создаем новую заметку!")
title=input("Укажите заголовок заметки: ")
content=input("Напишите описание заметки: " )
status=input("Введите текщий статус заметки: " )
created_date=input('Укажите дату создания заметки в формате: 21-12-2024 ')
issue_date=input('Укажие требуемый дедлайн этой заметки в формате: 22-12-2024 ')

print("\n", "-"*30,"\n")
print(f"{username}, Вы создали новую заметку!")
#print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
#print("Дата создания заметки:", created_date)
#print("Дедлайн (срок истечения):", issue_date)

# формальная проверка формата даты по длине строки 10 символов
if len(created_date) != 10:
    print("!!! Внимание: дата создания заметки введена некорректно. Требуемый формат: 21-12-2024, введено: ", created_date)
else:
    print("Дата создания заметки:", created_date)

if len(issue_date) != 10:
    print("!!! Внимание: дедлайн заметки введен некорректно. Требуемый формат: 21-12-2024, введено:", issue_date)
else:
    print("Дедлайн (срок истечения):", issue_date)