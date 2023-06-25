import asyncio
import time
import aiohttp
import requests

start = time.time()
# url = "https://www.wikidata.org/wiki/Q98854090"
url = "https://www.baidu.com"
symbols = {"xxx", "yyy", "zzz", "aaa", "bbb", "ccc"}

async def async_test():
    starttime = time.time()
    results = []
    for symbol in symbols:
        print('async working on symbol {}'.format(symbol))
        response = requests.get(url)
        results.append(response.text)
    endtime = time.time()
    totaltime = endtime - starttime
    print('async,it took {} seconds to make api calls'.format(totaltime,len(symbols)))


async def aiohttp_test():#有问题，不返回
    starttime = time.time()
    results = []
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print('aiohttp working on symbol {}'.format(symbol))
            response = await session.get(url,ssl=False)
            results.append(response.text)
        print(results)
    endtime = time.time()
    totaltime = endtime - starttime
    print('aiohttp,it took {} seconds to make api calls'.format(totaltime, len(symbols)))

def get_tasks(session):
    tasks = []
    for symbol in symbols:
        print('get_tasks aiohttp working on symbol {}'.format(symbol))
        # tasks.append(session.get(url,ssl=False))
        tasks.append(asyncio.create_task(session.get(url,ssl=False)))
    return tasks

async def aiohttp_battch_test():#有问题，不返回
    starttime = time.time()
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(response.text)
        print(results)
    endtime = time.time()
    totaltime = endtime - starttime
    print('aiohttp,it took {} seconds to make api calls'.format(totaltime, len(symbols)))
