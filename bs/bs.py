# n = 0
# print('n =', n)

# n = 'abc'
# print(n)

# n, m, z = 0, 'abc', False

# n = n + 1
# n = + 1

# print(n, m, z)

# n = 4
# n = None
# print("n =", n)

# n = 1
# if n > 2:
#     n -= 1
#     print(n)
# elif n == 2:
#     n *= 2
#     print(n)
# else:
#     n += 2
#     print(n)

# n, m = 1, 2
# if((n > 2 and n != m) or n == m):
#     n += 1

# n = 0
# while n < 5:
#     n += 1
#     print(n)

# for i in range(5):
#     print(i)

# for i in range(2, 5):
#     print(i)

# for i in range(5, 2, -1):
#     print(i)

# print(5 // 2)

# print(float()))

# arr = [1, 2, 3]

# arr.append(4)

# arr.pop()
# print(arr)

# arr.insert(0, 9)
# print(arr)

# arr[0] = 0
# arr[3] = 0
# print(arr)

# n = 5
# arr = [1] * n
# print(arr)
# print(len(arr))

# arr = [1, 2, 3]
# # print(arr[-1])

# print(arr[-2])


# arr = [1, 2, 3, 4]
# print(arr[1:3])

# print(arr[0:4])

# a, b, c = [1, 2, 3]
# print(a, b, c)

# nums = [1, 2, 3, 4, 5]

# for i in range(len(nums)):
#     print(nums[i])

# for n in nums:
#     print(n)

# for i, n in enumerate(nums):
#     print(i, n)

# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]
# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)

# num = [1, 2, 3]
# num.reverse()
# print(num)

# arr = [5, 4, 7, 8]
# arr.sort()
# print(arr)

# arr.sort(reverse=True)
# print(arr)

# arr = ["bob", "alice", "jane", "doe"]
# arr.sort()
# print(arr)

# arr.sort(key=lambda x: len(x))
# print(arr)

# arr = [i for i in range(5)]
# print(arr)

# arr = [i+i for i in range(5)]
# print(arr)

# arr = [[0] * 4 for i in range(4)]
# print(arr)

# arr = [[0] * 4] * 4
# print(arr)

# s = "abc"
# print(s[0:2])

# s += "def"
# print(s)

# print(int("123") + int("123"))

# print(str(123) + str(123))

# print(ord("a"))

# string = ["ab", "cd", "ef"]
# print("".join(string))

# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# print(queue)

# queue.popleft()
# print(queue)

# queue.appendleft(1)
# print(queue)

# queue.pop()
# print(queue)

# mySet = set()

# mySet.add(1)
# mySet.add(2)
# print(mySet)
# print(len(mySet))

# print(1 in mySet)
# print(2 in mySet)
# print(3 in mySet)

# mySet.remove(2)
# print(2 in mySet)

# print(set([1, 2, 3]))

# mySet = {i for i in range(5)}
# print(mySet)

# myMap = {}
# myMap["alice"] = 88
# myMap["bob"] = 77
# print(myMap)
# print(len(myMap))

# myMap["alice"] = 80
# print(myMap["alice"])

# print("alice" in myMap)
# myMap.pop('alice')
# print("alice" in myMap)

# myMap = {"alice": 90, "bob": 70}
# print(myMap)

# myMap = {i: 2*i for i in range(3)}
# print(myMap)


# myMap = {"alice": 90, "bob": 70}
# for key in myMap:
#     print(key, myMap[key])

# for val in myMap.values():
#     print(val)

# for key, val in myMap.items():
#     print(key, val)

# tup = (1, 2, 3)
# print(tup)
# print(tup[0])
# print(tup[-1])

# myMap = {(1, 2): (2, 5)}
# print(myMap[(1, 2)])

# mySet = set()
# mySet.add((1, 2))
# print((1, 2) in mySet)


import heapq

# minHeap = []
# heapq.heappush(minHeap, 3)
# heapq.heappush(minHeap, 2)
# heapq.heappush(minHeap, 4)

# print(minHeap[0])

# while len(minHeap):
#     print(heapq.heappop(minHeap))

# maxHeap = []
# heapq.heappush(maxHeap, -3)
# heapq.heappush(maxHeap, -2)
# heapq.heappush(maxHeap, -4)

# print(-1 * maxHeap[0])

# while len(maxHeap):
#     print(-1 * heapq.heappop(maxHeap))

# arr = [1, 3, 4, 5]
# heapq.heapify(arr)
# while arr:
#     print(heapq.heappop(arr))


# def myFun(n, m):
#     return n * m


# print(myFun(3, 4))

# def outer(a, b):
#     c = "c"

#     def inner():
#         return a + b + c
#     return inner()


# print(outer("a", "b"))

# def double(arr, val):
#     def helper():
#         for i, n in enumerate(arr):
#             arr[i] *= 2

#         nonlocal val
#         val *= 2
#     helper()
#     print(arr, val)


# nums = [1, 2]
# val = 3
# double(nums, val)

# class MyClass:
#     def __init__(self, nums):
#         self.nums = nums
#         self.size = len(nums)

#     def getLength(self):
#         return self.size

#     def getDoubleLength(self):
#         return 2 * self.getLength()
