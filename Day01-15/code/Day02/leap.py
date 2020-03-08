"""
输入年份，如果是闰年就输出true，否则输出false
2019年06月17日
"""


year = int(input('请输入年份：'))
isleap = (year%4==0 and year %100 !=0 or
          year%400 ==0)

print(isleap)



