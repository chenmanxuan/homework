# 1、编写一个函数输出乘法口诀表，执行结果如图所示（提示：print 默认输出后会换行，可以通过 print 参数控制是否换行）
for i in range(1,10):
    for j in range(1,i + 1):
        print('{}*{}={}'.format(i,j,i*j), end='\t')
    print()


#####################################################
for i in range(1,10):
    for j in range(1,i+1):
        end_flag='\n' if i==j else'\t'
        print(f'{i}*{j}={i*j}',end=end_flag)

# 2、编写一个函数遍历并打印 1 到 100，如果数字能被3整除，显示 Fizz；如果数字能被 5 整除，显示 Buzz；如果能同时被 3 和 5
def fizz_buzz():
    for i in range(1,101):
        if i%3==0 and i % 5 ==0:
            print('FizzBuzz')
        elif i % 3 ==0:
            print('Fizz')
        elif i % 5 ==0:
            print('Buzz')
        else:
            print(i)

print(fizz_buzz())

# 3、编写一个函数，输出 10 以内的斐波那契数列
def f(n):
    i,j=0,1
    while i<n:
        print(i),
        i,j=j,i+j

print(f(10))