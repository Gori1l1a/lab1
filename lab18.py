import datetime
def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M:%S")
            args_str = ""
            for arg in args:
                args_str = args_str + str(arg) + " "
                
            result = func(*args, **kwargs)
            
            f = open(filename, 'a', encoding='utf-8')
            f.write(f"[{time_str}] Вызвана функция {func.__name__} с аргументами: {args_str}. Результат: {result}\n")
            f.close()
            return result
        return wrapper
    return decorator

@log_calls("laba18.txt")
def calculate_sum(a, b):
    return a + b

calculate_sum(5, 10)
calculate_sum(2, 2)