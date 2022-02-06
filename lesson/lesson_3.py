#задание №1
one_num = int(input('Введите 1 число:'))
two_num = int(input('Введите 2 число:'))
def result(one_num, two_num):
    return one_num / two_num
if one_num != 0 and two_num != 0:
    print(result(one_num, two_num))
else:
    print('error')

#задание №2
name = str(input('Введите имя:'))
surname = str(input('Введите фамилию:'))
year_of_birth = str(input('Введите год рождения:'))
home_town = str(input('Введите город проживания:'))
email = str(input('Введите email:'))
phone = str(input('Введите номер телефона:'))
def result(**kwargs):
    return kwargs
print(result(Имя=name, Фамилия=surname, Год=year_of_birth,Адрес=home_town, Email=email, телефон=phone))

#задание №3
arg_1 = int(input('Введите целое число:'))
arg_2 = int(input('Введите целое число:'))
arg_3 = int(input('Введите целое число:'))
def my_func(arg_1, arg_2, arg_3):
    if arg_1 >= arg_3 and arg_3 <= arg_2:
        return arg_1 + arg_2
    elif arg_1 >= arg_2 and arg_2 <= arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3
print(my_func(arg_1, arg_2, arg_3))

#задание №4
x = int(input('Введите положительное число:'))
y = int(input('Введите целое отрицательное число:'))
def my_func(x, y):
    if x != 0:
        return x ** y
print(my_func(x, y))

x = int(input('Введите положительное число:'))
y = int(input('Введите целое отрицательное число:'))
i = 1
result = 1
while i <= y:
    result *= x
    i += 1
print(result)

#задание №5
line = str(input('Введите числа:'))
while True:
    for n in map(int, input().split()):
     line += n
     print(map)
    except ValueError
    print('None')


#задание №6,7
int_func = str(input('Введите слова маленькими буквами:'))
func = int_func.split(" ")
def line(int_func):
    return int_func.title()
print(line(int_func))



