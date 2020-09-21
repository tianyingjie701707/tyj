# l=[1,2,3,5,5,6,5]
# l[0]=5
# print(l)
#
# t=(1,2,2,3,5,6,6)
# print(t)
#
# s={1,1,2,2,3,4,5,6,6,8.5}
#
# print(s)
#
# a=100
# b='5'
# print(a+int(b))
#
#
#
# l=[1,2,3,4,4,5,6]
# print(tuple(l))
# print(set(l))
#
#
# q="asedff"
# w=[1,2,1,2,5,"a"]
# e=(1,2,2,4,1,5,"a")
# r={1,2,1,5,8,8,"a"}
# t={"name":"tt","age":"12"}
# print("a"in q)
# print("a"in w)
# print("a"in r)
# print("name"in t)
#
# #如果我有500万，我就给潘鹏买两只柯基，给他当保镖，如果没钱，还是洗洗睡吧
#
# money=1000
#
# if(money >= 5000000):
#     print("我就给潘鹏买两只柯基")
#     print("给他当保镖")
# else:
#     print("还是洗洗睡吧")

#如果我有50,潘鹏给我煮面条
#如果我有500，潘鹏给我按摩
#如果我有5000，潘鹏包揽家务
#如果我有50000，潘鹏给我叫小祖宗
# money=6
# if(money > 50):
#     print("潘鹏给我煮面条")
# elif(money > 500):
#     print("潘鹏给我按摩")
# elif(money > 5000):
#     print("潘鹏包揽家务")
# else:
#     print("潘鹏给我叫小祖宗")

# for i in [1,2,3,4,5,6,7,8,9]:
#     print(i)
#     print("吃饺子咯")
#
# print(list(range(100)))
# print(list(range(1,10)))
# print(list(range(1,10,2)))
# print(list(range(10,1,-1)))
# print(list(range(10,1,-2)))
# i=9
# while(i<10):
#     i+=1
#     print(i)
# while tuple:
#     print("走你")
# for i in range(1,11):
#     if(i==7):
#         pass
#     else:
# def div(n,m):
#     if m == 0:
#         print('m被除数不能为0')
#     else:
#         print(n/m)
#
# div(40,8)
# div(20,80)
# div(5,6)
# def select_data(s):
#     res='查询结果'
#     return res
#
# result=select_data('')
# print(result)
# def w(n,m):
#     return n+m
# print (w(4,9))
#
# def w(n,m=15):
#     return n+m
# print(w(5,4))
# print(w(4,5))
# print(w(5,m=10))
# print(w(10,m=60))
# print(w(1,))
# def ar(*args, **kwargs):
#   print(args)
#   print(kwargs)
# ar(98, 8, 7, 9, 5.5, 44, a=1.1, b=15, c=4, name="王麻子")

#
# def ar(a,*args,b=1,**kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
# ar(98, 8, 7, 9, 5.5, 44, b=15, c=4, name="王麻子")
# l = open ('a.txt','w')
# l.write('hi')
# l.close()
#
# c=10
#
# def aoo():
#     global c
#     c=20
#
#
# aoo()
# print(c)
# n='9876543210'
# m='987'
# print(n+m)
# print(n*3)
# print(m*5)
# print(n[0])
# print(m[2])
# print(n[2:6])
# print(n[:5])
# print(n[1:])
# print(n[-5])
# print(n[-2:])
# print(n[:-2])
# print(n[::-1])
# print(n[::2])
# print(n[::-2])
# a=' jhfuihfijdfiudh  '
# a=a.strip()
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# line = '你,快,给,我,跪,下'
# line = line.replace (',',',')
# print(line)
# print(line.split(','))
# print(line.find('预期'))
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}'.format(j,i,i*j),end='\t')
#     print()
l=[1,2,3,4,5,6,7,8,9,0]
# for i in l:
#     print(i)#竖列显示
# l[0]=20
# l.append(9)
# l.insert(2,30)
# l.extend((1,2,3,1,5))
# l.pop()
# l.pop(0)
# l.pop(-1)
# l.remove(1)
# print(l.index(6))
# l.sort()
# l.sort(reverse=True)
#
#
# print(l)
# m=[154,56,4,5,87,54,55,1,2,3]
# for i in range(len(m)-1,0,-1):
#     for n in range(0,i):
#         if(m[n])>(m[i]):
#             m[n],m[i]=m[i],m[n]
# print(m)
#
#对变量和方法的打包
#创建一个类
# class str_demo():
#     s = None
#     def replace(self):
#         print("15424")  #字符串替换
#     def split(self):
#         print('164.145') #字符串切割
#
#
# sd =str_demo() #实例化  sd就是一个对象
# sd.s = 'hello'
# sd.replace()
# sd.split()

#编写一个返回随机手机号的方法
#编写一个返回指定长度和内容的随机字符串方法
#编写一个返回随机姓名和方法
# import random
# l = random.choices("0123456789",k=8)
# m = random.choices(('182','185','186','136','137','138','150'),k=1)
# n = (m+l)
# print(n)
# print(''.join(n))

# 题2
# import random
# def shuzi(num,str):
#    l = random.choices(str, k=num)
#    s = "".join(l)
#    print(s)
# shuzi(5,"58465135eeerererww")

#题3
# import random
# def random_str(str, length):
#     res = random.choices(str, k=length)
#     return "".join(res)
#
#
#
# def name():
#     l_list = ['赵','钱','孙','李','周','吴','郑','王','杨李','欧阳']
#     s_list = "新鹏小飞明月月云彩六玖大白花伦柠檬肉"
#     l = random.choice(l_list)
#     s_length = random.randint(1,2)
#     s = random_str(s_list,s_length)
#     return l+s
# print(name())

#SyntaxError  语法错误
print('jhhbhvb')

#print(1/0) # ZeroDivisionError 运行时错误   异常:报错，结束代码运行结束
print("adafdfc")
try:
    # r = open("b.txt","r") # 报错 FileNotFoundError
    print(1 / 0)  # ZeroDivisionError
except (FileNotFoundError,)  as e:  # 捕获指定异常，并获取异常信息
    print(e)
    print("程序执行遇到了问题")
    print("重新打开文件")
except ZeroDivisionError as e:
    print("除数不能为0")
else:
    print("程序运行没报错")
finally:
    print("不管程序有没有报错都会运行")

print("文件已经打开")

def random_name():
    xing_list = ["赵","钱","孙","李","周","武","郑","王","欧阳","诸葛","轩辕","上官","司徒"]
    zi_list = "花赤橙黄绿青蓝紫冬梅建国华世凯"
    xing = random.choice(xing_list)
    zi_length = random.randint(1,2)
    zi = random_str(zi_list,zi_length)
    return xing + zi

print(random_name())