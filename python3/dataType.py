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
    output = ' '.join(inputWords)
    return output
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

# Tuple(元组)
tuple = ("abcd", "786", 2.23, "runoob", 70.2)
tinytuple = (123, "runoob")
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)
#print(tuple[0] = 11)# 修改元组元素的操作是非法的
#虽然tuple的元素不可改变，但它可以包含可变对象，比如list对象
#构造0个或1个元素的元组比较特殊，需要额外的语法规则
tup1 = ()
tup2 = (20, )
# string，list，tuple均属于sequence序列

#Set （集合）
#使用{}或set()创建集合，创建空集合需要使用set()
student = {'Tom','Jim','Mary','Tom','Jack','Rose'}
print(student)#自动去掉重复元素

#成员测试
if 'Rose' in student :
    print('Rose in set')
else:
    print('Rose not in set')

# set 可以进行集合运算
a = set('aabcsabsaaa')
b = set('alasadad')

print(a)
print(a-b) #a和b的差集
print(a | b) #a和b的并集
print(a & b) #a和b的交集
print(a ^ b)
