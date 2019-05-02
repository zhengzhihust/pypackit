"""
time complexity O(N*logN)
"""


def merge(a, b):
    c = []
    h, j = 0, 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    return merge(left, right)


"""
time complexity O(log2N)
"""


def bin_search(data_list, val):
    low = 0  # 最小数下标
    high = len(data_list) - 1  # 最大数下标
    while low <= high:
        mid = (low + high) // 2  # 中间数下标
        if data_list[mid] == val:  # 如果中间数下标等于val, 返回
            return mid
        elif data_list[mid] > val:  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:  # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return  # val不存在, 返回None