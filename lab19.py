def cashe(func):
    cashe={}
    def wrapper(*args):
        if args in cashe:
            return cashe[args]
        else:
            result=func(*args)
            cashe[args]=result
            return result
    return wrapper

@cashe
def calculate_sum(a, b):
    return a + b

print(calculate_sum(3,4))
print(calculate_sum(99,4))
print(calculate_sum(3,4))
