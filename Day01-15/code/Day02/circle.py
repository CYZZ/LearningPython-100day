
"""
输入半径计算圆形的周长和面积
2019年6月16日
"""
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
# area = math.pi * radius^2.0


print('周长：%.2f'%perimeter)
print('面积：%.2f'%area)






