# a = [1, 3.14, 'hello', True]
# x = input("type")
# res = []
#
# if x == "int":
#     for i in a:
#         if type(i) == int:
#             res.append(i)



# def um(x, y):
#     z = x + y
#     return z
#
# print(um(8, 6))

# def fac():
#     n = int(input())
#     res = 1
#     while n >= 1:
#         res *= n
#         n -= 1
#     return res
#
# print(fac())

# a = 12.2
# print(isinstance(a, int))

def is_pr(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_pr(8))
