"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600

"""
seconds = int(input("Введите секунды "))

hours = int(seconds / 3600)
seconds -= int(hours * 3600)
minutes = int(seconds / 60)
seconds -= int(minutes * 60)

print(f"{hours} : {minutes} : {seconds}")