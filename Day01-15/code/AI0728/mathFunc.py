import matplotlib.pyplot as plt
import numpy as np
import sys

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # -n to+n的256个值
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)
# 在ipython的交互环境中需要这句话才能显示出来
plt.show()

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('测试的arr1=(arr1)')
print('Python %s on %s' % (sys.version, sys.platform))
