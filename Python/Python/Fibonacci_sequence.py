def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    print(a)

# 打印前10项
for i in range(10):