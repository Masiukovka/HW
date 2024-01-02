def summ(x):
    def summ_2(y):
        return x * y
    return summ_2

summs = []
for x in range(1, 4):
    summs.append(summ(x))

s_1, s_2, s_3 = summs

print(s_1(10))
print(s_2(10))
print(s_3(10))

def say():
    slovo = "Привет"
    print(hex(id(slovo)))
    def repeet():
        print(hex(id(slovo)))
        print(slovo)
    return repeet

func = say()
print(func.__code__.co_freevars)
print(func.__closure__)