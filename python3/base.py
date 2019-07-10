import keyword
print(keyword.kwlist)

# 第一个注释
print("Hello, Python!")# 第二个注释

'''
多行注释
'''

"""
多行注释
"""

print("Hello, Python!")

# 行与缩进
if True:
    print ("True")
else:
    print ("False")

'''
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  print("False") #缩进不一致导致运行错误
'''

#多行语句

total = "item_one" + \
    "item_two" + \
    "item_three"
print(total);

total = ['item_one', 'item_two', 'item_three', 'item_four', 'item_five']
print(total);

#数Number字类型
i1 = 1
b1 = True
f1 = 1.23
c1 = 1 + 2j
print(i1, b1, f1, c1)

#字符串String
s = "abc\ndef"
print(s)

s = r"abc\ndef"
print(s)

print(total[0], total[1], total[-1], total[-2])

s = "abcdefg"
print(s[0:5])

#空行
#等待用户输入
#input("\n\n按下 enter 键后退出。")

#同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

#多个语句构成代码组
x = 5
if x <= 5 :
    print("a")
elif x <= 10 :
    print("b")
else :
    print("c")

#Print 输出
x = "a"
y = "b"
# 换行输出
print(x)
print(y)
print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

#import 与 from...import
'''
import sys #导入整个模块
from sys import argv,path #从模块中导入某个函数
from sys import * #导入模块所有函数
'''
import sys
print('=================Python import mode===============');
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import argv,path # 导入特定的成员\
print('====================python from import===============')
print('path:', path)