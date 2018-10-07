#my_math.py
m,n=10,5
def add(m,n):
    return m+n

def sub(m,n):
    return m - n

def mul(m,n):
    return m*n

def div(m,n):
    try:
        return m/n
    except ZeroDivisionError:
        print("  除数不能为0")
