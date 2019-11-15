# 冒泡排序
# 1. 从后向前两两比较，最终最小数会被交换到起始位置，这样第一个最小数的位置就排好了
# 2. 继续重复上述过程，依次将2，3.。n-1个最小数进行排序
# 参考网站https://www.runoob.com/w3cnote/sort-algorithm-summary.html

def bubble_sort(numbers):
    for i in range(len(numbers)):
        flag = False  # 每次遍历都要标记状态为false，
        for j in range(len(numbers) - 1):
            t = (len(numbers) - 1) - j
            if t <= i:
                break
            if numbers[t] < numbers[t - 1]:
                temp = numbers[t]
                numbers[t] = numbers[t - 1]
                numbers[t - 1] = temp
                flag = True  # 发生了交换，flag就标记为true，说明已经排序好了
        if flag == False:
            break
        print('循环次数',i)
    return numbers


def sayHello(name):
    print('welcome', name)


newNumber = bubble_sort([1, 2, 3, 9, 4, 5, 7, 15, 80, 5, 5, 5, 5])
print('newnumbers:', newNumber)

# sayHello('hhh嘿嘿嘿')
