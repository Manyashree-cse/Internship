import time

def execution_time(func):
    def wrapper(n):
        start=time.time()
        func(n)
        end=time.time()
        print("elapsed:",end-start)
    return wrapper

@execution_time
def first_n(n):
    sum=0
    for i in range(n):
        sum=sum+i
    print(sum)

first_n(30)