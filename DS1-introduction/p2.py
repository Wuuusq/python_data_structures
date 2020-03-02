"""
T(n) = 3*n² + 2n + 4
n越大，常量的影响越小
O(n) = O(n²)
"""

a = 5  # 一个赋值1
b = 6  # 一个赋值1
g = 9  # 一个赋值1

for i in range(n):  # 两层循环，三个赋值，3*n²
    for j in range(n):
        x = j * i
        s = j * j
        d = i * i

for i in range(n):  # 一层循环，两个赋值，2n
    x = i * i
    s = i * i

f = 1566  # 一个赋值1
