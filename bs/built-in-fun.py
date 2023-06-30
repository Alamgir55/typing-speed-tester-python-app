# class ImplementAbs:
#   def __init__(self, string):
#     self.string = string

#   def __abs__(self):
#     return self.string.lower()

# custom_obj = ImplementAbs("HELLO")

# x = abs(-9)
# y = abs(-100.879)
# z = abs(custom_obj)

# print(x)
# print(y)
# print(custom_obj)

# import asyncio

# class AsyncIterator:
#   def __init__(self, start, stop):
#     self.start = start
#     self.stop = stop

#   def __aiter__(self):
#     self.cur = self.start
#     return self

#   async def __anext__(self):
#     await asyncio.sleep(1)
#     if self.cur >= self.stop:
#       raise StopIteration

#     self.cur += 1
#     return self.cur -1

# async def example():
#   custom_obj = AsyncIterator(1, 10)
#   obj_iter = aiter(custom_obj)
#   print(obj_iter)
#   async for num in obj_iter:
#     print(num)

# asyncio.run(example())

# a = [1,0,1,2,3]
# print(all(a))

# b = [True, True, 1, 2]
# print(all(b))

# c = ["", "a", "b"]
# print(all(c))

# d = [[0,0],[0,0],[0,0],[0,0]]
# print(all(d))

# e = [[], [1], True]
# print(all(e))

# import asyncio

# class AsyncIterator:
#   def __init__(self, start, stop):
#     self.start = start
#     self.stop = stop

#   def __aiter__(self):
#     self.cur = self.start
#     return self

#   async def __anext__(self):
#     await asyncio.sleep(1)
#     if self.cur >= self.stop:
#       raise StopIteration

#     self.cur += 1
#     return self.cur - 1


# async def example():
#   custom_obj = AsyncIterator(1, 10)
#   obj_iter = aiter(custom_obj)
#   print(await anext(obj_iter))
#   print(await anext(obj_iter))
#   print(await anext(obj_iter))

# asyncio.run(example())

# a = [1,0,1,2,3]
# print(any(a))

# b = [True, True, 1, 2]
# print(any(b))

# c = ["", "a", "b"]
# print(any(c))

# d = [[0,0],[0,0],[0,0],[0,0]]
# print(any(d))

# e = [[], [1], True]
# print(any(e))

# base10 = 100
# base2 = bin(base10)

# base10_neg = -100
# base2_neg = bin(base10_neg)

# print(base2)
# print(base2_neg)

# print(bool)
# print(bool(""))
# print(bool(1))
# print(bool(-1))
# print(bool([1, 2]))
# print(bool({}))
# print(bool({"key": "value"}))

# class Class:
#     pass


# def func():
#     print("hi")


# def func2():
#     def inner():
#         pass
#     return inner


# def func3(x): return x + 1


# not_func = "hell"

# print(callable(Class))
# print(callable(func))
# print(callable(func2()))
# print(callable(func3))
# print(callable(not_func))

# A = 65
# a = 97

# print(chr(A))
# print(chr(a))

# class TestClass:
#     def regular_method(self):
#         print(self)

#     @classmethod
#     def class_method(cls):
#         print(cls)

#     def __str__(self):
#         return "TestClass Instance"


# t = TestClass()
# t.regular_method()
# t.class_method()
# TestClass.class_method()


# complex1 = "32+2j"
# print(complex(complex1))

# print(complex(3, 4))

# class MyClass:
#     def __init__(self, x):
#         self.x = x


# c = MyClass(10)
# print(c.x)
# delattr(c, "x")
# print(c.x)


# lst = [("a", 1), ("b", 2)]
# lst_dict = dict(lst)

# print(lst_dict)

# import math

# print(dir(math))

# quotient, remainder = divmod(10, 3)
# print(quotient, remainder)

# values = ["a", "b", "c", "d"]
# for index, valu in enumerate(values):
#     print(f"{index}: {valu}")

# print(list(enumerate(values)))

# x = 2
# code = input("Enter some code: ")
# eval(code)

# code = input("Enter some code: ")
# exec(code)

# def filter_func(value):
#     return value % 2 == 0


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = filter(lambda x: x % 2 == 0, lst)
# evens_2 = filter(filter_func, lst)

# print(evens)
# print(evens_2)

# print(list(evens))
# print(list(evens_2))

# x = 1
# x_float = float(1)

# string = "-9.8"
# string_float = float(string)

# print(x_float)
# print(string_float)

# print(float("inf"))
# print(float("-inf"))
# print(float('1e-003'))


# txt = "For only {price:.2f} dollars!"
# print(txt.format(price=49))

# binary_value = format(100, 'b')
# print(binary_value)

# lst = [1, 2, 3]
# s = set(lst)
# s.add(4)

# print(s)

# fs = frozenset(lst)
# print(fs)

# class MyClass:
#     def __init__(self, x):
#         self.x = x


# c = MyClass(10)
# print(getattr(c, "x"))

# print(globals())

# class MyClass:
#     def __init__(self, x):
#         self.x = x


# c = MyClass(10)
# print(hasattr(c, "x"))
# print(hasattr(c, "y"))

# help(int)

# class CustomHex:
#     def __index__(self):
#         return 10


# print(hex(255))
# print(hex(1))

# c = CustomHex()
# print(hex(c))

# x = [1, 2, 3]
# y = x
# a = 1000000
# b = a + 1 - 1

# print(id(x))
# print(id(y))
# print()
# print(id(a))
# print(id(b))

# print(int("122"))

# a = 1
# b = 2

# print(isinstance(a, int))
# print(isinstance(b, float))
# print(isinstance(a, type))
# print(isinstance(int, type))


# class A:
#     pass


# class B:
#     pass


# class C(A):
#     pass


# class D(C):
#     pass


# class E(A, B):
#     pass


# print(issubclass(C, A))
# print(issubclass(D, C))
# print(issubclass(D, A))
# print(issubclass(E, A))
# print(issubclass(E, B))


# class Iterator:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         self.cur = self.start
#         return self

#     def __next__(self):
#         if self.cur >= self.stop:
#             raise StopIteration

#         self.cur += 1
#         return self.cur - 1


# def example():
#     custom_obj = Iterator(1, 10)
#     obj_iter = iter(custom_obj)
#     print(obj_iter)
#     for num in obj_iter:
#         print(num)


# example()
