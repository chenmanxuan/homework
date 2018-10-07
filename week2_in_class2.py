# 1、将字符串'hello, world'中的 l 替换为 *
print('hello, world'.replace('l', '*'))



# 2、现有字符串 'Good' ，期望结果 'good!good!good!'，至少用两种方法实现

string='Good'
string = string.lower()+"!"
print(string*3)


################################################

string = 'Good'.lower()
lst=[string]*3
print('!'.join(lst)+'!')


# 3、将字符串 'Fh1qoWe92QbvC' 中的大写替换为小写，小写替换为大写（提示：Python 字符串有内置方法支持，请找到这个方法来实现）
print('Fh1qoWe92QbvC'.swapcase())

###################################################
def switch_case(string):
    lst=[]
    for x in string:
        if x.isalpha():   #测字符串是否只由字母组成
            if x.islower():
                x=x.upper()
            else:
                x=x.lower()
        lst.append(x)
    return ''.join(lst)

print(switch_case('Fh1qoWe92QbvC'))


# 4、请将字符串 'Fh1qoWe92QbvC' 中的数字按序取出，组成新的字符串并打印出来（提示：Python 字符串有内置方法可判断字符串是否为纯数字）

nums=[]
for c in 'Fh1qoWe92QbvC':
    if c.isdigit():
        nums.append(c)

print(''.join(nums))

#############################
import re
text='Fh1qoWe92QbvC'
text=''.join(re.findall('\d+',text))
print(text)


# 5、现有列表 lst = [2, 0, 3, 6, 9]，请打印出从小到大排列的列表 lst（不改变列表元素的原有顺序）
lst=[2,0,3,6,9]
print(sorted(lst))


# 6、现有一个列表 l = [2, 3, 1, 2, 4, 3]，请实现 l = [2, 3, 1, 4]
def unique_list(lst):
    seen = set()
    seen_add=seen.add
    return [x for x in lst if x not in seen and not seen_add(x)]

lst=[2,3,1,2,4,3]
print(unique_list(lst))

####################################
l = [2, 3, 1, 2, 4, 3]
formatList = list(set(l))
formatList.sort(key=l.index)
l=formatList
print (l)


# 7、现有字符串 'aasdebbcaa'，请统计字符串中每个字符出现的次数，将统计结果存储在一个字典里
string='aasddebbcaa'
d_counter={}
for c in set(string):
    d_counter[c]=string.count(c)

print(d_counter)

###################################
from collections import Counter
def austin_test():
    c = Counter()
    for i in 'aasdebbcaa':
        c[i] = c[i] + 1
    print(c)

print(austin_test())
# 8、完成一个函数，计算传入的字符串中的【数字】、【字母】、【空格】和【其他】的个数后返回
def str_counter(string):
    counter={'number':0,'letter':0,'space':0,'others':0}
    for c in list(string):
        if c.isdigit():
            counter['number']+=1
        elif c.isalpha():
            counter['letter']+=1
        elif c.isspace():
            counter['space']+=1
        else:
            counter['others']+=1
    return counter
print(str_counter('sgh13fs   jfdksfk'))


# 9、完成一个函数，检查传入的字符串是否含有空格，如果有空格则删去字符串中的空格并返回结果
def remove_spaces(string):
    return ''.join([s for s in string if not s.isspace()])

print(remove_spaces('assf asfas asf'))


# 10、完成一个函数：随机产生一个数，让用户来猜，猜中则屏幕打印"恭喜你猜对了"并结束，若猜错，则提示用户是猜大了还是猜小了（提示：内置的 random 模块有产生随机数
def guess_number():
    import random
    result=random.randint(0,100)
    guess_times=5
    while guess_times>0:
        guess=int(input('请输入一个数:'))
        if result==guess:
            print("恭喜你猜对了")
            break
        elif result>guess:
            print("很遗憾，你猜小了")
        elif result<guess:
            print("很遗憾，你猜大了")
        guess_times-=1


print(guess_number())
