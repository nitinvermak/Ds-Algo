import concurrent.futures
import time
from typing import final
import requests

number_of_calls=50
start = time.perf_counter()
api_url = "https://jsonplaceholder.typicode.com/users" 

def do_something(i):
    print('--Started--No-{}'.format(i))
    response = requests.get(api_url)
    result = response.json()
    #print(result)
    print('--Finished-No-{}'.format(i))
    return result


with concurrent.futures.ProcessPoolExecutor() as executor:
    num = [i for i in range(number_of_calls)]
    results = executor.map(do_something, num)
    final_result = []
    for item in results:
        final_result.append(item)

#print(final_result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

start = time.perf_counter()
for x in range(number_of_calls):
    do_something(x)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')