# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# seq_list = [1,2,3,4,5,6]
# print(list(map(lambda x:x*x,seq_list)))



# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [5,6,7]
# ab = list(map(lambda x,y:x+y,a,b))
# print(ab)


# fibonacci = [0,1,1,3,4,5,8,13,21,34,55]
# even_numbers = list(filter(lambda x: x%2 == 0,fibonacci))
# print(even_numbers)


# from functools import reduce
# f = lambda a,b: a if a>b else b
# print(reduce (f,[11,24,345,656,23,334]))
'''
    create on may 10, 2018
    @author: ****
'''
# hello world
# print("hello world")

# 格式化输出
# print("%o" %10)
# print("%d" %10)
# print("%f" %10)
# print("%.2f" %10.1456)
# print("%.2e" %10.1556)
# print("%.2g" %121.1556)

# print(round(10.1234,2))

# format 格式化字符串
# print("{} {}".format("hello","world"))
# print("{0} {0} {1}".format("hello","world"))
# format 索引输出
import json

import numpy

str = "hello"
list = ["hello","world"]
tuple = ("hello","world")
# print("{0[1]}".format(str))   e
# print("{0[0]},{0[1]}".format(list))
# print("{0[0]},{0[1]}".format(tuple))


# 通过字典的Key
# Tom = {'age':27,'gender':'M'}
# print("{0[age]}".format(Tom))
# print("{p[gender]}".format(p=Tom))


# 通过对象的属性
# class Person:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
#     def __str__(self):
#         return '{self.name} is {self.age} years old'.format(self = self)
#
# print(Person('Tom',18))

# 字符串并且制定对其宽度
# print('默认输出：{}，{}'.format('hello','world'))
# print('左右各取10位对其：{:10s},{:>10s}'.format('hello','world'))  #hello     ,     world
# print('取10位中间对其：{:^10s},{:^10s}'.format('hello','world'))   #  hello   ,  world
# print('取2位小数：{} is {:.2f}'.format(3.141592,3.141592))         # 取2位小数：3.141592 is 3.14
# print('数值的千位分隔符：{} is {:,}'.format(123456789,123456789))   #数值的千位分隔符：123456789 is 123,456,789


# Python 最基本的数据结构是序列
# 序列： 列表、元组、字符串、Unicode字符串、buffer对象、range对象
# 序列操作： 索引、长度、组合（序列相加）、重复（乘法）、分片、检查成员、历遍、最大值、最小值
# 常用序列： 元组tuple 列表list  列表可以修改、元组不可以修改

# 1.列表
list1 = ['Python','AI']
list2 = [1,2,3,4]
list3 = ["p","y","t","h","o","n",['python','AI']]
# 2.方法
# len(list1)
# max(list1)
# min(list1)
# list.append(obj)
# list.count(obj)
# print(list2.count(1))
# list.extend(seq)
# print(list2.extend(list3))
# list.index(obj)
# list.insert(index,obj)
# list.pop([index = -1])
# list.remove(obj)
# list.reverse()
# list.sort(cmp= None,key=None,reverse = False)   排序
# list.clear()
# list.copy()


# 元组
tuple1 = ('python','AI')
tuple2 = (1,2,3,4)
tuple3 = "a","b","c","d"

# 元组中的值是不允许修改和删除的
tup = tuple1 + tuple2

# 元组 和 列表的 转换
# list(tuple)
# tuple(list)
# 元组是更简单的数据结构

# tip
# t = 1,
# print(t)

# 序列操作
# 索引 list2[0]
# 赋值 list2[1] = 'a'
# 序列相加 list1 + list2
# 序列相乘 list1*3
# 序列的循环调用
#     for a in list1:
#         print(a)
# 使用分片访问的是元素基本样式[下限：上限：步长] 默认步长为1



# 字典   键是唯一的
# 格式： dict = {key1:value1 , key2:value2 , key3:value3}
# 字典基本操作
# len(dict)
# str(dict)
# dict[key]
# dict.get(key)
# dict[key] = newvalue
# dict.values()
# dict.keys()
# dict.pop(key [,default]) 删除字典给定键所对应的值
# dict.items()
# key in dict
# key not in dict

# 条件语句 与 循环语句
# if condition1:
#         statement1
# else:
#     statement2
#

# num = 3
# if num >0 :
#     print("正数")
# elif num == 0 :
#     print("零")
# else :
#     print("负数")


# 三元运算符
# [on_true] if [expression] else [on_false]

# a =1
# b =2
# c = a - b if a > b else a+b
# print(c)


# 循环语句
# while expression:
#     statements
#
# for iterating_var in sequence:
#     statements(s)

# break continue pass

# for i in range(5):
#     print("i=%d"%i)

# for i in range(5):
#     if i == 3:
#         break
#     print("i=%d"%i)


# for j in range(5):
#     if j == 3 :
#         continue
#     print("j=%d"%j)
#
# def smaple():
#     pass

# lambda函数案例
# sum = lambda x,y:x+y
# print(sum(3,4))


# map
# seq_list = [1,2,3,4,5,6]
# print(list(map(lambda x:x*x,seq_list)))

# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [5,6,7]
# ab = list(map(lambda x,y:x+y,a,b))


# filter
# filter(function,iterable)
# fibonacci = [0,1,1,3,4,5,8,13,21,34,55]
# even_numbers = list(filter(lambda x: x%2 ==0 ,fibonacci))
# print(even_numbers)


#reduce
# from functools import reduce
# f = lambda a,b: a if a>b else b
# print(reduce (f,[11,24,345,656,23,334]))
#

#
# import numpy
# print(numpy.__version__)


#NumPy 轴axes  轴的数量：秩 rank
# T 转置
# size 数组中的元素个数，等于shape 元素的乘积
# itemsize
# dtype
# shape n*m (n,m)
# data
# ndim
# Flat
# imag
# real
# nbytes



# import  numpy as np
# a = np.random.random(4)
# print(type(a))
# print(a.shape)
# print(a)

# list=[1,23,4]
# print(np.array(list).astype(float))
# print(np.array(list ,dtype=float))
#
# print(float(list))
# print(set(np.typeDict.values()))


# NumPy 创建数组
# list=[1,2,3]
# tuple=(1,2,3)
# dict={'a':1,'b':2}

# numpy.array(object,dtype=None,copy=True,order=None,subok=False,ndmin=0)

# import numpy as np
#
# a = np.array([[1,2],[4,5,7]])
# print(a)
# print(np.array(list))



# range 函数创建数组
# import numpy as np
# a = range(0,4)
# b = range(4)
# a1 = [i for i in a]
# b1 = [i for i in b]
# c1 = np.array(a)
# print(type(a))
# print(b1)
# print(a1)
# print([i for i in c1])
# print(c1)
# print(type(a1))
# print(type(c1))

# arange函数 矩阵
# import numpy as np
# a = np.arange(12)
# print(a)
# a2 = np.arange(1,2,0.1)
# print(a2)

# linspace 生成等差数列
# numpy.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)
# start:起始值
# stop：序列结束值
# num：生成的样本数 默认为50
# endpoint：布尔值 TRUE ：则最后一个样本包含在序列内
# retstep:布尔值 TRUE :返回间距
# dtype:数组的类型
# import numpy as np
# a = np.linspace(1,5,10)
# a = np.linspace(1,5,10,endpoint= False)
# print(a)
# print(a.shape)



#logspace 生成等比数列
# numpy.logspace(start,stop,num=50,endpoint=True,base=10.0,dtype=None)
# start: float,基底base的start次幂作为左边界
# stop: float,基底base的stop次幂作为右边界
# num:生成的样本数，默认为50
# endpoint:布尔值，如果为True,则最后一个样本包含在序列内
# base: 基底，取对数的时候log的下标
# dtype:数组的类型

# import numpy as np
# a = np.logspace(0,2,5)
# print(a)  //[  1.           3.16227766  10.          31.6227766  100.        ]


# ones 与 zero 系列函数 empty
# ones_like zero_like empty_like
# ones(shape,dtype=None,order='C')
# sharp: (2,3) 2
# dtype: 数据类型 可选。 numpy.int8 默认为numpy.float64
# order:{'c','F'},规定返回数组元素在内存的存储顺序，C-row_major F-column-major

# import numpy as np
# a = np.ones(4)
# b = np.ones((4,),dtype=np.int8)
# c = np.ones((2,1))
# s = (2,2)
# d = np.ones(s)
# v = np.array([[1,2,3],[4,5,6]])
# e = np.ones_like(a)
# print("a={} \n b ={} \n c ={} \n d ={} \n v ={} \n e={}".format(a,b,c,d,v,e))

# import numpy as np
# a = np.ones(5)
# b = np.zeros((5,1),dtype=np.int)
# c = np.zeros((2,1))
# s = (2,2)
# d = np.zeros(s)
# e = np.zeros((2,),dtype=[('x','i4'),('y','i4')])
# # x = np.arrange(6)
# # x = x.reshape((2,3))
# # f = np.zeros_like(x)
# y = np.arange(3,dtype=np.float)
# g = np.zeros_like(y)
# print("a ={} \n b ={} \n c ={} \n d ={} \n e ={} \n y={} \n g={}".format(a,b,c,d,e,y,g))




# import numpy as np
# e = np.zeros((2,),dtype=[('i4','i2'),('f16','i4')])
# x = np.arange(6)
# x = x.reshape((2,3))
# f = np.zeros_like(x)
# print("e ={} \n x ={} \n f ={}".format(e,x,f))
#

# empty(shape,dtype=None,order='C')
# import numpy  as np
# a = np.empty([2,2])
# b = np.empty([2,2],dtype=int)
# temp = np.array([[1,2,3],[4,5,6]])
# c = np.empty_like(temp)
# print("a={} \n b={} \n c={}".format(a,b,c))

# eye(N,M=None,k=0,dtype=float)
# import numpy as  np
# a = np.eye(2,dtype=int)
# b = np.eye(3,k=1)
# print("a={} \n b={}".format(a,b))

# identity(n,dtype=None) 方正
# import numpy as np
# a = np.identity(3)
# print(a)

# 索引和切片
import numpy as np
# a = np.arange(1,6)
# print(a[3])
# print(a)

# a = np.arange(16)
# a = a.reshape(4,4)
# print(a)
# print(a[0][2])
# print(a[0,2])
# print(a[1:3,2:3])
# print(a[1][2])


# a = (np.arange(16).reshape(4,4))
# x = np.array([0,1,2,1])
# x == 1
# print(x)
# print(a)
# print(x==1)
# print(a[x!=2])
# print(a[~(x==1)])
# print(a[np.logical_not(x==1)])
#
# print(a[(x==1)|(x==2)])


# import matplotlib.pyplot as plt
# a = np.linspace(0,2*np.pi,200)
# b = np.sin(a)
# plt.plot(a,b)
# # mask = b >=0
# # plt.plot(a[mask],b[mask],'bo')
# mask = (b>=0)&(a<= np.pi/2)
# plt.plot(a[mask],b[mask],'go')
# plt.show()

# 矩阵的合并
# a = np.floor(10*np.random.random((2,2)))
# b = np.floor(10*np.random.random((2,2)))
# #hstack() 在行上合并
# c = np.vstack((a,b))
#
# #vstack() 在列上合并
# d = np.hstack((a,b))
#
# print(c)
# print(d)

#矩阵的分割
# from numpy import newaxis
# # np.column_stack((a,b))
# a = np.array([1,2])
# b = np.array([3,4])
# # c = np.column_stack((a,b))
# # d = np.hstack((a,b))
# # print("a=\n{} \nb=\n{} \nc=\n{} \nd=\n{}".format(a,b,c,d))
#
# # newaxis 插入新的维度，由一维变成二维度
# e = np.column_stack((a[:,newaxis],b[:,newaxis]))
# f = np.hstack((a[:,newaxis],b[:,newaxis]))
# # print(a)
# # print(a[:,newaxis,newaxis])
# print("e=\n{} \nf=\n{}".format(e,f))


# 矩阵运算与线性代数
# 线性函数基础
# np.linalg.norm  范数
# np.linalg.inv   逆矩阵
# np.linalg.solve 求解线性方程组
# np.linalg.det   求矩阵的行列式
# numpy.linalg.lstsq  lstsq表示LeaST Square 最小二乘求解线性函数

# 特征值与特征分解
# numpy.linalg.eig        特征值和特征向量
# numpy.linalg.eigvals    特征值
# numpy.linalg.SVD        奇异值分解
# numpy.linalg.qr         矩阵的QR分解

# 范数计算
# np.linalg.norm(x,ord=None,axis=None,keepdims=False)

# import numpy as np
# x = np.array([
#     [0,3,4],
#     [1,6,4]]
# )
#默认参数 ord=None ,axis=None, keepdims=False
# print("默认参数(矩阵二范数，不保留矩阵二维特性)：",np.linalg.norm(x))
# print("矩阵二范数，保留矩阵二维特性：",np.linalg.norm(x,keepdims=True))
# print("矩阵每个行向量，求向量的二范数：",np.linalg.norm(x,axis=1,keepdims=True))
# print("矩阵每个列向量，求向量的二范数：",np.linalg.norm(x,axis=0,keepdims=True))
# print("矩阵一范数:",np.linalg.norm(x,ord=1,keepdims=True))
# print("矩阵二范数：",np.linalg.norm(x,ord=2,keepdims=True))
# print("矩阵无穷范数:",np.linalg.norm(x,ord=np.inf,keepdims=True))
# print("矩阵每个行向量，求向量的一范数",np.linalg.norm(x,ord=1,axis=1,keepdims=True))


# 矩阵的逆
# import numpy as np
# a = np.mat("0 1 2;1 0 3;4 -3 8")
# a_inv= np.linalg.inv(a)
# print(a)
# print(a_inv)
# print(a*a_inv)

# mat 函数可以用来构造一个矩阵，传进去一个专用字符串，矩阵的行与行之间 用分号隔开，行内的元素用空格隔开

# 求解方程组的解
# import numpy as np
# a = np.array([[3,1],[1,2]])
# b = np.array([9,8])
# x = np.linalg.solve(a,b)
# print(x)
# # 使用dot 函数检查求得的解是否正确
# print(np.dot(a,x))

# 计算矩阵行列式
# import numpy as np
# a = np.array([[1,2],[3,4]])
# print(np.linalg.det(a))
#
# a = np.array([[[1,2],[3,4]],[[1,2],[2,1]],[[1,3],[3,1]]])
# print(a.shape)
# print(np.linalg.det(a))


# 最小二乘法求解线性函数
# np.linalg.lstsq(array_A,array_B)[0]
import numpy as np
# x = np.array([0,1,2,3])
# y = np.array([-1,0.2,0.9,2.1])
# A = np.vstack([x,np.ones(len(x))]).T
# print(A)
# m,c = np.linalg.lstsq(A,y)[0]
# print(m,c)
#
# import matplotlib.pyplot as plt
# plt.plot(x,y,'o',label='Original data',markersize=10)
# plt.plot(x,m*x+c,'r',label='Fitted line')
# plt.legend()
# plt.show()

# x_d = [18,23,25,35,65,54,34,56,72,19,23,42,18,39,37]
# y_d = [202,186,187,180,156,169,174,172,153,199,193,174,198,183,178]
# n = len(y_d)
# import numpy.linalg
# B = numpy.array(y_d)
# A = numpy.array([[x_d[j],1] for j in range(n)])
# # print(A)
# X = numpy.linalg.lstsq(A,B)[0]
# a = X[0];
# b = X[1]
# print("Line is :y=",a,"x+",b)
#
# # 绘图
# import matplotlib.pyplot as plt
# plt.plot(np.array(x_d),B,'ro',label = 'Original data',markersize = 10)
# plt.plot(np.array(x_d),a*np.array(x_d)+b,label='Fitted line')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()


#   求特征值 eigenval 与 特征向量 eigenvector
# C = np.mat("3 -2 ;1 0")
# # eigvals 求解特征值
# c0 = np.linalg.eigvals(C)
# print(c0)
# # eig 求解特征值 与 特征向量
# c1,c2 = np.linalg.eig(C)
# print(c1)
# print(c2)
# # 使用dot函数 验证求得的解是否正确
# for i in range(len(c1)):
#     print("left:",np.dot(C,c2[:,i]))
#     print("right:",c1[i]*c2[:,i])
#

# 奇异值分解 SVD Singular Value Decomposition
# D = np.mat("4 11 14 ;8 7 -2")
# U,Sigma,V = np.linalg.svd(D,full_matrices=False)
# print("U:{}\n Sigma:{}\n V:{}".format(U,Sigma,V))
#
# # 验证奇异值分解
# print(U*np.diag(Sigma)*V)

# QR分解 三角分解 A=QR A的QR分解
# 矩阵 ---> 正交变换--->Hessenberg矩阵--->QR分解 Q正规正交矩阵、上三角形矩阵R

# numpy 的广播机制
# VauleError :operands could not be broadcast together with shapes(4,)(5,)
# 上面错误的原因就是数据运算过程中违背了广播原则。
# 广播原则,就是一种维度处理原则
# 广播操作会让程序更加简洁高效
# 广播原则：如果两个数组的后缘维度（即从未尾开始算起的维度）的轴长符合
# 或其中一方的长度为1，则认为它们是广播兼容的，广播会在缺失或者长度为1 的轴上进行
# 当我们使用ufunc函数对两个数组进行计算时，ufunc函数会对这两个数组的对应元素进行计算，
# 因此要求这连个数组有相同的大小（及维度相同）。
# 如果这两个数组的维度不同的话,为了避免多重循环，会进行如下的广播处理。
# 1.让所有输入数组都向其中维度最长的数组看齐，维度不足的部分都通过在前面加1补齐
# 2.输出数组的维度是输入数据维度的各个轴上的最大值
# 3.如果输入数组的某个轴和输出数组的对应轴的长度相同,或者其长度为1时，这个数组能够用来计算，否则出错
# 4.当输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值

# x = np.arange(4)
# print(x)
# xx = x.reshape(4,1)
# print(xx)
# y = np.ones(5)
# print(y)
# z = np.ones((3,4))
# # print(z)
# # print(x.shape)
# # print(y.shape)
# print(xx.shape)
# # print(z.shape)
# # q = xx + y
# q = xx+x
# print(q)


# a = np.array([0.0,10.0,20.0,30.0])
# a = a[:,np.newaxis] #加入新的坐标轴
# b = np.array([1.0,2.0,3.0])
# c = b+a
# print(c)

# Tip :注意，执行广播的前提在于，两个ndarray 执行的是 element-wise (按位加，按位减) 运算,
# 而不是矩阵乘法

# Numpy 统计函数

import jieba
# # 全模式 cut_all=True
# text = "野生动物园有很多凶猛的动物"
# str_quan1 = jieba.cut_for_search(text)
# print("|".join(str_quan1))

import jieba.posseg as pseg
text = "野生动物园有很多凶猛的动物"
# word = pseg.cut(text)
# for w in word:
#     if w.flag in ["n","v"]:
#         print("w.word={}, w.flag={}".format(w.word,w.flag))

# # jieba.add_word("有很多")
# str_quanl = jieba.cut(text,cut_all=False)
# print("|".join(str_quanl))

# 关键词提取 是基础
# 文本分类、文本聚类、信息检索















































