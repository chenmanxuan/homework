# 1、使用 ThreadPoolExecutor 和多线程搭配，要求：a). 用一个线程监视当然已完成的进度；b). 用 ThreadPoolExecutor 创建3个线程执行 fib 函数；c). 用另外一个线程作为生产者（提示：使用submit方法提交新的任务）
# 输出如下：
# fib(26) = 121393
# fib(28) = 317811
# fib(27) = 196418
# …

from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import asyncio
def NUMBER():
    lst=[]
    for i in range(26,30):
        lst.append(i)
    yield lst

def fib(n):
    if n<=2:
        return 1
    return fib(n-2)+fib(n-1)
if __name__=='__main__':
    start=NUMBER().__next__()
    with ProcessPoolExecutor(max_workers=3) as executor:
        for num,result in zip(start,executor.map(fib,start)):
            print(f"fib({num})={result}")






# 2、写一个异步生成器，要求：a). 用到 async for，b). 抓取10个”http://httpbin.org/get?a=X"这样的url (X为0-9这十个数字)，并打印a的值
import asyncio
import aiohttp


async def produce():
    a = 0
    while (a < 10):
        print(f'a{a}')
        yield f"http://httpbin.org/get?a={a}"
        a = a + 1


async def consumer():
    async for v in produce():
        print(v)
        async with aiohttp.ClientSession() as session:
            async with session.get(v) as response:
                z = await response.json()
                print(f"a={z.get('args').get('a')}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(consumer())
