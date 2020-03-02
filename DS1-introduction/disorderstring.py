import time

"""
乱序字符串：比较两个字符串的组成是否相同
"""

'''
# 穷举法：排除。原因：如果字符串过长，例如20个长度 时间复杂度为20！
def solutions1(s1, s2):
    alist = list(s2)

    pos1 = 0
    flag = True

    while flag and pos1 < len(s1):  # 第一层循环n
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:  # 第二层循环n   n^2
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
            pos1 = pos1 + 1
        else:
            flag = False

    return flag


print(solutions1('abcd', 'dbca'))
print(solutions1('pythoa', 'typhon'))
'''
'''
# 计数和比较法
# 计算每个字符出现的次数  26个字母为例
# 算法复杂度   T(n) = n+n+26 = 2n + 26    O(n)
def solutions2(s1,s2):
    c1 = [0]*26  # 记录s1中字母出现的次数
    c2 = [0]*26  # 记录s2中字母出现的次数

    # ord()  返回的是字符在阿斯克码中的数字
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')   # 一个循环n
        c1[pos] = c1[pos] + 1 

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')   # 一个循环n
        c2[pos] = c2[pos] + 1


    count = 0  # 如果某个字符在s1和s2中出现的次数相同，那么count+1
    flag = True

    while count < 26 and flag:
        if c1[count] == c2[count]:
            count = count + 1       #  26
        else:
            flag = False

    return flag


print(solutions2('asdfghjklc','lkjhgfdsa'))
print(solutions2('python','thonpy'))
'''

'''
# 排序和比较
# 我们可以按照从 a-z 排列每一个字符串，如果两个字符串相同，那这两个字符串就是乱序字符串
# 算法的复杂度：不是  O(n)  而是O(n^2)
def solutions3(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    # 排序   排序通常复杂度 O(n^2)或者 O(logn)
    alist1.sort()
    alist2.sort()

    flag = True

    pos = 0

    while pos < len(s1) and flag:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1  # n
        else:
            flag = False
    return flag


print(solutions3('asdfghjkl', 'lkjhgfdsac'))
print(solutions3('python', 'ythpna'))
'''
