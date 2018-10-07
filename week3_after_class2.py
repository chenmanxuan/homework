# 1、编写一个函数完成密码生成器的功能，输入参数有密码长度和密码组成的内容，密码组成的内容可以有大写字母（A-Z）、小写字母（a-z）、数字（0-9）、特殊符号（~!@#$
def passwd_gen(p_len,lower_case=True,upper_case=True,number=True,special_char=True):
    import string,random
    lower_case_set=set(list(string.ascii_lowercase))
    upper_case_set=set(list(string.ascii_uppercase))
    number_set=set([x for x in range(10)])
    special_set=set(list('!@#$%^&*()~'))
    user_choice=set()
    if lower_case:
        user_choice = user_choice |lower_case_set
    if upper_case:
        user_choice = user_choice | upper_case_set
    if number:
        user_choice = user_choice | number_set
    if special_char:
        user_choice = user_choice | special_set
    passwd_lst=random.sample(user_choice,p_len)
    return '' .join(passwd_lst)

# 2、编写一个函数：输入参数为一个整数列表和一个整数，判断该整数是否存在于该列表中。如果存在，是在列表的左半边还是右半边
def xx2(number,lst):
    b=-1
    c=0
    d=[]
    for a in lst:
        if a==number:
            print("列表里有元素%d" %(number))
            c=1
            break
    if c==0:
            print("列表里不存在元素%d,将返回None" %(number))
            return None
    else:
        try:
            while True:
                b=lst.index(number,b+1) #该方法返回查找对象的索引位置，如果没有找到对象则抛出异常
                d.append(b)
        except:
            print("进入except")
        finally:
            for a in d:
                if (len(lst)-1)//2>a:
                     print("left")
                elif (len(lst)-1)//2<a:
                     print("right")
                else:
                     print("正好在中间有一个")

lst=[1,2,3]
xx2(1,lst)


# 3、编写一个函数：过滤1-100中的素数
def is_prime(x):
    if x==1:
        return False
    elif x==2:
        return True
    else:
        for n in range(2,x):
            if not x%n:
                return False
            return True

print(list(filter(is_prime,range(1,101))))

# 4、编写一个模块，要求里面有变量x和y，两数相加add(x, y)，两数相减sub(x, y)，两数相乘mul(x, y)，两数相除div(x, y)这四个方法的实现
import my_math
print(my_math.add(2,3))
print(my_math.sub(4,2))
print(my_math.mul(2,3))
print(my_math.div(4,2))




# 5、编写一个函数：输入参数是一个整数列表，请找出该列表中最小的整数并返回
def minnumber(lst):
    from functools import reduce
    return reduce(lambda x,y:x if x<y else y,lst)


print(minnumber([1,2,3]))