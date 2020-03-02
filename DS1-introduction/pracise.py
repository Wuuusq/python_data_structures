import time


# 计算前n个整数的和
def sum0fn(n):
    strat_time = time.time()
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    end_time = time.time()
    return sum, end_time - strat_time


for i in range(5):
    print("计算结果是%d，需要%.9f秒" % sum0fn(10000))

print("-----------------------------------")


# 高斯函数
def sum0fn2(n):
    strat_time = time.time()
    sum = (n * (n + 1)) / 2
    end_time = time.time()
    return sum, end_time - strat_time


for i in range(5):
    print("计算结果是%d，需要%.9f秒" % sum0fn2(10000))
