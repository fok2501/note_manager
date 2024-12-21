#input Имя и возраст

name=input("Как Вас зовут? Введите свое имя:")
# print(name)
print(f"Добрый день, {name}!")
# age = int(input(f"Введите Ваш возраст, {name}: "))
age = int(input("Введите ваш возраст: "))
print(f"{name}, через 5 лет Вам будет: ", age+5)