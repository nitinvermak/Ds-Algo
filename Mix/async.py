import asyncio
import time
from datetime import datetime

async def normal_function(n):
    print('Normal function call {}'.format(n))
    time.sleep(1)

async def async_function(n):
    print('Async function call {}'.format(n))
    await asyncio.sleep(1)

async def counter():
    start=datetime.now()
    normal_list= []
    for i in range(0,5):
        normal_list.append(normal_function(i))
    
    await asyncio.gather(*normal_list)
    wait = (datetime.now()-start).total_seconds()
    print('Sync wait= {}'.format(wait))

    start1=datetime.now()
    async_list = []
    for j in range(0,5):
        async_list.append( async_function(j))   

    await asyncio.gather(*async_list)

    wait1 = (datetime.now()-start1).total_seconds()
    print('Async wait= {}'.format(wait1))

asyncio.run(counter())
