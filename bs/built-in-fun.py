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

print(bool)
print(bool(""))
print(bool(1))
print(bool(-1))
print(bool([1,2]))
print(bool({}))
print(bool({"key": "value"}))
