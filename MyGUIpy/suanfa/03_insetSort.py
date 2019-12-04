# 基本思路在要排序的一组数中，嘉定前n-1个数已经排序号，现在将第n个数插到前面的有序数列中，使得这n个数也拍好顺序的。如此反复循环，知道全部排好顺序


def insert_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, 0, -1):
            if array[j] < array[j - 1]:
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
            else:
                break
    return array


# mynewArr = [1, 2, 3, 4, 5, 6]
#
# my2arr = mynewArr[3::-1]
#
# for value in mynewArr[3:1:-1]:
#     print(value)
#
# print(my2arr)

arr = [3, 4, 1, 5, 12, 87, 100, 5]

newArr = insert_sort(arr)
print('排序后的额newarr=', newArr)
