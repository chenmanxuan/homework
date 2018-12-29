#1
def triple(lst):
    return [x**3 for x in lst]


lst=[1,2,3]
print(triple(lst))

#2
from functools import reduce
def add(lst):
    return reduce(lambda x,y:x+y,lst)

lst=[1,2,3]
print(add(lst))


#3
path=''
def read_file(path,size=1024):
    with open(path,'rb') as f:
        while True:
            data = f.read(size)
            if not data:
                break
            yield data

print(read_file(path))






#4
def has_null_value(lst):
    return list(filter(None,lst))==lst

lst=['',[],'sdfd']
print(has_null_value(lst))


def has_null_value(lst2):
    return all(lst2)

lst2=['',[],'safdsf']
print(has_null_value(lst2))


#5
def fib_number(n):
    if n==0 or n==1:
        return 1
    return fib_number(n-2)+fib_number(n-1)

def fib(n):
    result=[]
    for i in range(n):
        value=fib_number(i)
        if value> n:
            break
        result.append(value)
    return result

print(fib(10))


#6.
def passwrd(len,lower=True,upper=True,number=True,special=True):
    import string,random
    lower_set=set(list(string.ascii_lowercase))
    upper_set=set(list(string.ascii_uppercase))
    number_set=set([x for x in range(10)])
    special_set=set(list('~!@#$^%*()'))
    user_choice=set()
    if lower:
        user_choice=user_choice | lower_set
    if upper:
            user_choice = user_choice | upper_set
    if number:
        user_choice=user_choice | number_set
    if special:
        user_choice=user_choice | special_set
    passwrd=random.sample(user_choice,len)
    return ''.join(passwrd)

len=6
print(passwrd(len))


#7

from functools import partial
def mul_by_type(n):
    result=partial(lambda x,y:x*y,2)
    return result(n)

print(mul_by_type(3))


#8
from functools import wraps
import time
def time_add(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.time()
        f=func(*args,**kwargs)
        print('counter_time:',time.time()-start_time)
        return f
    return wrapper


@time_add
def add(x,y):
    time.sleep(3)
    return x+y


print(add(1,2))



