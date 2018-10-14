#1、使用偏应用函数实现一个函数求2和其他整数的积
from functools import partial
def mul(x,y):
    print(x * y)

mul_p=partial(mul,2)
mul_p(3)


#2、将柯里化的例子用偏应用函数 partial 实现
def add(x,y,z):
    print(x+y+z)

addA=partial(add,x=1,y=2,z=3)
addA()







#3、实现一个装饰器：计时函数从执行开始到执行完毕所花费的时间
import time
def timeit(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        print('start')
        for i in range(150):
            print(i)
        rs=func(*args,**kwargs)
        print('Consume time:',time.time()-start_time)
        return rs
    return wrapper

@timeit
def add(x,y,z):
    return x+y+z


add(100,200,300)


#4、实现一个装饰器：检查除法函数传入的参数，避免除法函数抛 ZeroDivisionError 异常
def do(fn):
    def wrapper(*args,**kwargs):
        try:
            fn(*args,**kwargs)
        except ZeroDivisionError:
            print('除数不能为0')
        else:
            print(fn(*args,**kwargs))
    return wrapper

@do
def fun(x,y):
    return x/y



fun(10,0)




#5、实现一个装饰器：使被装饰的函数在每次执行完毕后打印’Done’和当前时间（精确到秒）
def do(fn):
    def wrapper(*args,**kwargs):
        print('Done')
        rs=fn(*args,**kwargs)
        from datetime import datetime
        print(datetime.now())
        return rs
    return wrapper


@do
def  add(x,y):
    return x + y


add(1,2)