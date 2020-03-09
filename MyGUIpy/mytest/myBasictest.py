import mytest.cal.calculator
from mytest.cal import calculator
from mytest.cal.calculator import car

dic = {'Name': 'chiyuze', 'Age': 18, 'class': 'First', 'num': [1, 2, 3]}
# 浅拷贝：应用对象 赋值
dict2 = dic
# 拷贝
dict3 = dic.copy()

# 修改data数据
dic['user'] = 'root'
dic['num'].remove(1)

print(dic)
print(dict2)
print(dict3)
print(dic.items())

# dic.fromkeys(seq=)
