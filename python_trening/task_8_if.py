def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')
task_yes_no(str_1 = 'test', str_2 = 'testing')

num_float = - 0
if num_float > 0:
    print('положительное число')
elif  num_float == 0:
    print('Ноль')
else:
    print('отрительное число')

num = 5
permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('печать запрещена')

def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('бакалавр')
    elif year_of_study in range(5, 7):
        print('магистр')
    elif year_of_study in range(7, 10):
        print('аспирант')
    else:
        print('ВВедите корректный год обучения')
student_rank(5)

def num(number):
    if 100 < number > 100:
        print('-')
    else:
        print('+')
num(105)
