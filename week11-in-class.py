#1、写一个装饰器 inject，在 __init__ 时自动给类注入参数。
def inject(func):
    def wrapper(*args,**kwargs):
        #print(func.__name__)
        #print(args[0])
        #print(args[0].__dict__)
        #print(kwargs)
        args[0].__dict__.update(kwargs)
        #print('='*10)
        #print(args[0].__dict__)
        func(*args,**kwargs)
    return wrapper

class Test:
    @inject
    def __init__(self,x,y,z):
        #self.x=x
        #self.y=y
        #self.z=z
        pass


if __name__=='__main__':
    t=Test(x=4,y=5,z=6)
    print(t.x,t.y,t.z)


#2、实现一个类，可以完成链式调用
from functools import reduce
class Seq:
    def __init__(self,*args):
        self.args=args

    def map(self,expr):
        return self.eval_func(map,expr)

    def filter(self,expr):
        return self.eval_func(filter,expr)

    def reduce(self,expr):
        return self.eval_func(reduce,expr)

    def eval_func(self,func,expr):
        self.args=func(expr,self.args)
        return self

    def __repr__(self):
        return str(self.args)

if __name__=='__main__':
    s=Seq(1,2,3,4).map(lambda  x:x*2).filter(lambda x:x>4).reduce(lambda x,y:x+y)
    print(s)

#3、使用 with 写一个函数调用计时的上下文管理器，提示：魔术方法 __enter__、__exit__，time模块、ContextDecorator
import time
import ContextDecorator
class Timed:
    def __enter__(self):
        self.start_time=time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost_time=time.time()-self.start_time
        print('Cost:',cost_time)

with Timed():
    time.sleep(2)


@ContextDecorator
class Timed2:
    def __enter__(self):
        self.start_time=time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost_time=time.time()-self.start_time
        print('Cost:',cost_time)

@Timed2
def f():
    time.sleep(2)


#4、使用 Python 读取一个 10G 文件，如何更快、更省内存呢？
#使用下面的两种方式：
f=open(...)
ls=f.readlines()
f.close()


#或者

with open(...) as f:
    for line in f:
        pass