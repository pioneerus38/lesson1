a = 2
b = 0.5
print(a + b)


name = "Владимир"
c = f'Привет, {name}!'
print(c)


#нет проверки на ввод строки или числа вне диапазона
v = input("Введите число от 1 до 10: ")
print(10 + int(v))


another_name = input("Введите ваше имя: ")
print(f'Привет, {another_name}! Как дела?')


print(float('1'))
# print(int('2.5')) генерируется исключение ValueError
print(int(2.5))
print(bool(1))
print(bool(''))
print(bool(0))