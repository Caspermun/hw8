# class work
# def divide(x, y=4):
#     return x / y
#
# def multiply(x, y=2):
#     return x * y
#
# def subtraction (x, y):
#     return x - y

# 1
# def arithmetic(x, y, z):
#     if z == "+":
#         return (x + y)
#     elif z == "-":
#         return (x - y)
#     elif z == "*":
#         return (x * y)
#     elif z == "/":
#         return (x / y)
#     else:
#         return ("Invalid operation")

# 2
# def is_year_leap(year):
#     return year % 4 == 0 and (year % 100 != 0)  # != = не равен

# 3
# def square(x):
#     p = 4 * x  # Периметр
#     s = x ** 2  # Площадь
#     d = (x ** 2) * 2  # d = 512
#     d = d ** 0.5  # Диагональ
#     k = (p, s, d)
#     return k

# 4
# def season(x):
#     if x in (1, 2, 12):
#         return 'Winter'
#     elif x in (3, 4, 5):
#         return 'Spring'
#     elif x in (6, 7, 8):
#         return 'Summer'
#     elif x in (9, 10, 11):
#         return 'Autumn'

# 5
# def bank(a, years):
#     for year in range(years):
#         a *= 1.1  # a = a * 1.1
#     print('В итоге ты получишь', a, 'сом')

# 6
# def is_prime(x):
#     if x < 2:
#         return False
#     for z in range(2, x):
#         if x % z == False:
#             return False
#     return True

if __name__ == '__main__':

# class work
    # print(subtraction(multiply(divide(1234564678)), 617282337))

# 1
    # print(arithmetic(5, 8, '+'))
    # print(arithmetic(5, 5, '*'))
    # print(arithmetic(125, 75, '-'))
    # print(arithmetic(10000, 25, '/'))
    # print(arithmetic(50, 25, 0))

# 2
    # print(is_year_leap(2024))

# 3
    # print(square(16))

# 4
    # print(season(int(input('Enter the month number:'))))

# 5
    # bank(int(input('Введи в меня деньги:')),int(input('Сколько лет будешь хранить?:')))

# 6
    # print(is_prime(6))