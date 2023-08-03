#!/usr/bin/python3
from typing import *

# '''
# 第三注释
# 第四注释
# '''

# """
# 第五注释
# 第六注释
# """

# print("Hello, world!")

# if True:
#     print('true')
# else:
#     print('false')

# str = '123456789'

# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第五个的字符
# print(str[2:])             # 输出从第三个开始后的所有字符
# print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str * 2)             # 输出字符串两次
# print(str + '你好')         # 连接字符串

# print('------------------------------')

# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# input("\n\n按下 enter 键后退出。")


# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )

# print('---------')
# # 不换行输出
# print( x, end="" )
# print( y, end="" )
# print()

# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))

# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']

# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表

# test = "123"
# print(test)
# test = "456"
# print(test)

# def reverseWords(input):

#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")

#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords = inputWords[-1::-1]

#     # 重新组合字符串
#     output = ' '.join(inputWords)

#     return output


# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWords(input)
#     # print(rw)


# num_int = 123
# num_str = "456"

# print("Data type of num_int:", type(num_int))
# print("Data type of num_str:", type(num_str))

# print(str(num_int) + num_str)

# a, b = 0, 1
# while b < 10:
#     a, b = b, a + b
#     print(b, end=",")

# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print("对应人类年龄: ", human)

# # 退出提示
# input("点击 enter 键退出")

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# def hello():
#     print("hello")


# hello()

# list = [1, 2, 3]


# list = [1, 2, 3]
# list.append(4)
# print(list)

# file = open('E:/Workspaces/vscode/python-test/test.txt',
#             mode='r+', encoding='utf-8')
# for line in file.readlines():
#     print(line, end='')

# file.write("new")


# import math
# print(math.pi)

# import mysql.connector

# db = mysql.connector.connect(
#   host="172.20.20.1",
#   port="3307",
#   user="mysql",
#   passwd="mysql",
#   database="ispatial"
# )
# mycursor = db.cursor()

# mycursor.execute("SELECT id, name as names FROM users")

# myresult = mycursor.fetchall()     # fetchall() 获取所有记录

# for x in myresult:
#   print(x)


# try:
#     print(1/0)
# except Exception as err:
#     print(err)
# else:
#     print('no error')
# finally:
#     print('over')

# val = '123.3'
# print('word : %s, %d' % (val, float(val)))

# print(isinstance(False, int))
# print(type(False) == bool)
# print(type(False) == int)

# leetcode 560
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         note = {0: 1}
#         s = 0
#         r = 0
#         for n in nums:
#             s += n
#             if s - k in note:
#                 r += note[s - k]
#             note[s] = note.get(s, 0) + 1
#         return r

# leetcode 289
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         a = "".join((lambda x: (x.sort(), x)[1])(list(s)))
#         b = "".join((lambda x: (x.sort(), x)[1])(list(t)))
#         return set(b) - set(a)

# leetcode lcp44
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def numColor(self, root: TreeNode) -> int:
#         note = set()
#         self.f(root, note)
#         return len(note)

#     def f(self, node: TreeNode, note: set):
#         if node != None:
#             note.add(node.val)
#         self.f(node.left, note)
#         self.f(node.right, note)


nums = [3, 1, 2, 5, 4]
print([j for i, j in enumerate(sorted(nums))])

# nums.sort()
# print(nums)
# print(abs(nums[1] - nums[0]))
# print(max(nums[1], nums[0]))
