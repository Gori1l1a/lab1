def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(types)):
                if not isinstance(args[i], types[i]):
                    raise TypeError("Неправильный тип данных")
            return func(*args)
        return wrapper
    return decorator

@type_check(int, int)
def add(a,b):
    return a+b

print("Результат:", add(5,10))

try:
    print("Результат:", add("5", 10))
except TypeError as e:
    print("Ошибка:", e)