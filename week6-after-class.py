#1、实现一个装饰器：检查被装饰的函数所传入的参数，如果是字符串类型，且含有小写字母，则将小写字母全部转为大写字母
def do(fn):
    def wrapper(a):
        if isinstance(a,str) is True and a.lower():
            print(a.upper())
        else:
            print('none')
    return wrapper


@do
def fun(a):
    print(a)


a='sfdsSDFDSF'
fun(a)







#2、实现一个生成器函数：读取文件时每次只返回固定的长度，此长度可由用户调用时设置


#这个程序要先在桌面建一个note.txt文件并写入内容
# 此程序最好在cmd的python命令行实现,因为r的可读性不好
#def readlen():
#    with open('note.txt','r') as f:
#        p=int(input('指定读取的长度'))
#        a=f.read(p)
#         yield a


#g=readlen()
#print(next(g))




#3、实现一个生成器函数：模拟数据库中的主键自增，即生成的值为主键自增的结果
def increment(id=1):
    while True:
        yield id
        id=id+1

g1=increment()
print(next(g1))
print(g1.__next__())
print(g1.__next__())
print(g1.__next__())




#4、实现一个生成器表达式：生成 50 以内的偶数，并用 for 循环打印出每个值
g=(i for i in range(50) if i%2==0)

for i in g:
    print(i)







#5、实现一个生成器函数：读取操作系统 C 盘中的所有文件的名字
import os
def main():
    g=(filename for filename in os.listdir('c:\\'))
    for f in g:
        print(f)


print(main())
