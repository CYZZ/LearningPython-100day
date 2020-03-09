"""
操作符的使用

"""

a=5
b=10
c=3
d=4
e = 5
a += b # 15
a -= c # 12
a *= d # 48
a /= e  # 9
print("a = ",a )

flag1 = 3 > 2 # True
flag2 = 2 < 1 # False
flag3 = flag1 and flag2 #False
flag4 = flag1 or flag2 #True
flag5 = not flag1 #False
print("flag1 = ",flag1)
print("flag2 = ",flag2)
print("flag3 = ",flag3)
print("flag4 = ",flag4)
print("flag5 = ",flag5)

print(flag1 is True) #True
print(flag2 is False) #True
