num_float = -1


# также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('положительное число')
elif num_float == 0:
    print('ноль')
else:
    print('число отрицательное')

#_______________________________________________________________
num = 0
permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

    #______________Задача Дано число если оно больше 100 или меньше -100, то ввывести на экран символ "-",
    # иначе вывести "+"

x = 222
if x > 100 or x < -100:
    print('-')
else:
    print('+')