# Введение в Python: Встроенные функции, переменные, комментарии.
# Базовые типы данных: строки, целые и дробные числа.

sum_of_ages = 14 + 16 + 18 + 26 + 11 + 14 + 31 + 13 + 19 + 16 + 21 + 20 + 16 + 41 + \
    + 32 + 34 + 18 + 28

print(sum_of_ages)
average = sum_of_ages / 18

rounded_average = round(average, 2)
rounded_average_new = '%.1f' % average

print(type(rounded_average))
print(type(rounded_average_new))



# a = '2'
# b = '3'
# print(int(a) + float(b))
# a = '6'
# print(int(a) + float(b))
# print(type(str(1000)))


# print(2**3)
# print(20 // 3)
# c = round(20 / 3, 1)
# # e = '.2f % 20/3'
# print(c)
# # print(e)
#
# print(20 % 3)

name = 'jack'
surname = input('введите фамилию ')
Age = int(input('введите возраст: '))
weight = 63.5
hobby = "chess, football"
country = 'usa'

read_book = "я прочёл книгу \"Простой Python\""

print(f'Hello, {name.title()} {surname.capitalize()}\n'
      f'ты на земле с {2022 - Age} года')


# print('Hello,', name.title(), surname.capitalize())
# print('Hello, {} {}'.format(name.title(), surname.capitalize()))
# print('Hello,' + ' ' + name.title() + ' ' + surname.capitalize())

# print(type(name))
# print(type(Age))
# print(type(weight))
#
# print(country.upper())

# job_1 = 'teacher'
# secondJob = 'engineer'

# 1wrong = 0
# &wrong! = 0
# False = 0


