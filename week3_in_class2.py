# 1、写一个函数：获取用户输入的名字（name）和年龄（age），计算一下该用户到哪一年（返回值）为100岁，并打印结果”{用户名字}在XXXX年为100岁”
def prt_user():
    name=input('name:')
    age=int(input('age:'))
    year=2018+100-age
    r=f'{name}在{year}年为100岁'
    print(r)
    return year

prt_user()

# 2、写一个函数：获取用户输入的整数，如果它是奇数则打印”您输入的是奇数”，如果是偶数则打印”您输入的是偶数”
def get():
    num=int(input("请输入一个整数！"))
    if  num % 2==1:
        print("你输入的是基数")
    else:
        print("你输入的是偶数")

print(get())



# 3、写一个函数：输入参数是一个 list，判断该 list 中是否有空对象（至少用三种方法实现）

def has_null_value(lst):
    flag=True
    for x in lst:
        if not bool(x):
            break
        else:
            flag=False
    return flag


print(has_null_value(['',0.0,4,'heelo']))
print(has_null_value([2.0, 4, 'hello']))
#######################################################
def has_null_value(lst):
    return list(filter(None,lst))==lst


print(has_null_value(['',0.0,4,'heelo']))
print(has_null_value([2.0, 4, 'hello']))
#######################################################
def has_null_value(lst):
    return all(lst)  #一假即假


print(has_null_value(['',0.0,4,'heelo']))
print(has_null_value([2.0, 4, 'hello']))


# 4、写一个函数：输入参数是一个整数列表，把该列表中每个整数都平方后返回新的列表（至少用两种方法实现）
def square(lst):
    return [x ** 2 for x in lst]

lst=[1,2,3,4]
print(square(lst))
########################################
def square(lst):
    return list(map(lambda x :x **2,lst))

lst=[1,2,3,4]
print(square(lst))

# 5、写一个函数：输入参数是一个整数列表，使用 reduce 函数实现求和后返回结果
def my_sum(lst):
    from functools import reduce
    return reduce(lambda x,y:x+y,lst)

print(my_sum([1,2,3,4]))

# 6、写一个函数：请用列表推导式实现立方
def triple(lst):
    return [x**3 for x in lst]

print(triple([1,2,3]))

# 7、写一个函数：输入参数是两个 list，请返回它们的共同元素所组成的新列表
def elements_in_common(m,n):
    s=set(m)&set(n)
    return list(s)

print(elements_in_common([1,2,3],[2,3,4]))



# 8、写一个函数：找出三个整数中的最大数（至少用两种方法实现）
def max_in_three(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    else:
        if y>z:
            return y
        else:
            return z

print(max_in_three(1,2,3))
#############################
def max_in_three(x,y,z):
    from functools import reduce
    return reduce(lambda x,y:x if x>y else y,(x,y,z))
print(max_in_three(1,2,3))