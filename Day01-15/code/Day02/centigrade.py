"""
温度单位转换
将华氏温度转为摄氏度温度
F = 1.8C + 32


"""
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8

print('%.1f 华氏度=%.1f摄氏度' % (f,c))