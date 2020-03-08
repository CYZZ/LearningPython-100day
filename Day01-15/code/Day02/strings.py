"""

字符串string的常用操作符
2019-06-17
"""
str1 = 'hello,world!'
print('字符串的长度是：',len(str1))
print('单词首字母大写：',str1.title())
print('字符串转大写：',str1.upper())
print('字符串是不是大写：',str1.isupper())
print('字符串是不是以hello开头：',str1.startswith('hello'))
print('字符串是不是以hello结尾：',str1.endswith('hello'))
print('字符串是不是以感叹号!开头：',str1.startswith('!'))
print('字符串是不是以感叹号!结尾:',str1.endswith('!'))
str2 = '- \u9a86\u660c'

str3 = str1.title() + ' ' + str2.lower()
print('str3 = ',str3)



