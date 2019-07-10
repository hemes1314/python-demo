# 变量使用前必须被赋值，
counter = 100 # 整型变量
miles = 1000.0 # 浮点型变量
name = "runoob" # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "runoob"

# 标准数据类型
# 可变：Number，String，Tuple(元组), 不可变： List， Set, Dictionary(字典)
# Number：int, float, bool, complex(复数)
# Number（数字）
# int 没有python2中Long
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# type()不会认为字类是一种父类类型
# isinstance()会认为字类是一种父类类型
a = 111
print(isinstance(a, int))

# 删除对象引用
var1 = 1
var2 = 10
del var1,var2

# 数值运算
print(5 + 4)
print(4.3 - 2)
print(3 * 7)
print(2 / 4) # 返回浮点数
print(2 // 4) # 返回整数
print(17 % 3) # 取余
print(2 ** 5) # 乘方

# String 字符串
str = "Runoob"
print(str)
print(str[0:-1]) # 第一个到倒数第二个
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "TEST")

# 转义
print("Ru\noob")
print(r"Ru\noob")

# 字符串不能改变

# List
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = ['123', 'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1, 2, 3, 4],
    # list[0]=1, list[1]=2, 而 -1 表示最后一个元素，list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 - 1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长， -1表示逆向
    inputWords=inputWords[-1::-1]

    # 重新组合字符串
    output = ''.join(inputWords)

