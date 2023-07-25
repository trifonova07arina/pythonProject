

# f = open('file.txt', 'w')
# try:
#     f.write([1,2,3])
# except Exception:
#     print('Ошибочка вышла!')
# f.close()

# with open('file.txt', 'w') as f:
#     f.write('Hello, world!')
#     print(f.closed)
#
# print(f.closed)

import  contextlib

# @contextlib.contextmanager
# def str_reverse(my_str):
#     print('Входим в контекстный менеждер:')
#     yield my_str[::-1]
#     print('Выхоим из контекстного менеджера!')
#
# with str_reverse('Hello, world!') as reversed_str:
#     print(f'Выполняется код в конструкции with: {reversed_str}')

# @contextlib.contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print('Произошла ошибка!')
#
# with exc_handler(IndexError):
#     my_l = [7,2,99]
#     print(my_l[9])

# def args_kwargs_func(*args, **kwargs):
#     print(f'{type(args)}: {args}')
#     print(f'{type(kwargs)}: {kwargs}')
#
# args_kwargs_func(4, True, [], 'stroka', d=4)

class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    def get_days(self):
        return self.__days
    def get_season(self):
        return self.__season

    def set_days(self, days):
        if days in [365,366]:
            year.__days = days
        else:
            raise Exception ('Введено неправильное количество дней')

    def set_season(self, season):
        if season.lower() in ['зима','весна','лето','осень']:
            year.__season = season.lower()
        else:
            raise Exception ('Введено неправильное название сезона')

year = Year(365, 'зима')

print(year.get_days())
print(year.get_season())

year.set_days(366)
year.set_season('Весна')

print(year.get_days())
print(year.get_season())


