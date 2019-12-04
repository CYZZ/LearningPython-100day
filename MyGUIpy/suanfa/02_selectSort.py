# 选择排序
# *基本思路
# 在长度N的无序数组中，第一次遍历n-1个数，找到最小的数值与第一个元素交换；
# 第二次遍历n-2个数，找到最小的数值与第二个元素交换
# 。。。
# 第n-1遍历，找到最小的数值与第n-1个元素进行交换，排序完成

def select_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if j < len(arr):
                if array[j] < array[min_index]:
                    min_index = j
        if min_index != i:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
    return array


arr = [2, 4, 5, 10, 5, 60, 43, 2, 1]
newArr = select_sort(arr)
print('newArr=', newArr)
