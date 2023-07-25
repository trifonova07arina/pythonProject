
# import time
# import sys
#
# my_iter1 = [x for x in range(1,99999999)]
# my_iter2 = (x for x in range(1,99999999))
# # for elem in my_iter:
# #     print(elem)
# print(sys.getsizeof(my_iter1))
# print(sys.getsizeof(my_iter2))
# print(type(range(1,11)))

# def my_lazy_func():
#
#     for i in range(1,11):
#         print(f'До {i}')
#         yield i
#         print(f'После {i}')
#
# for i in my_lazy_func():
#     print(i)
#
# # my_list = list(my_lazy_func())
# # print(my_list)

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
#with open('file.txt', 'w') as f:
  #   f.write('Hello, world!')
 #    print(f.closed)

# print(f.closed)
class cat:
    def __init__(self, *args,**kwargs,s):
        self.s=s
    
