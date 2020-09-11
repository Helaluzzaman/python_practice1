import time

def timer(func):
    def wrapper(*args,**kwargs):
        before = time.time()
        func()
        print("function took :", time.time()-before, "seconds")
    return wrapper

@timer
def name():
    print("After 2 seconds programe will resume: wait")
    time.sleep(2)
    for i in range(1000):
        print("nothing just for killing some time ", i)

name()