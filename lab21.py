import time

def timing (func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        time_result=(end-start)*1000
        print(f"Время выполнения функции: {time_result}")
        return result
    return wrapper

@timing
def fast_function():
    return "Я работаю быстро"

@timing
def calculate_sum(a, b):
    return a + b

fast_function()
calculate_sum(10, 20)


    




        
       