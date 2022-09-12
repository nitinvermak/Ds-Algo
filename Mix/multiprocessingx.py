# Written - 7 Sep 2022 -NV 

import time
import multiprocessing 


start = time.perf_counter()
def do_something():
    print('Will wait for 1 sec')
    time.sleep(1)
    print('Finished')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

processes = []

for _ in range(1000):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for i in processes:
    i.join()



finish = time.perf_counter()

print(f'Time taken = {finish -start} Seconds')

