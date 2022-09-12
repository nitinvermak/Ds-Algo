
# Python program to illustrate the concept
# of threading
import threading
import os

global1 = 1

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    global global1
    global1+=5
    print('1Global1={}'.format(global1))
 
def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    global global1
    global1+=5
    print('2Global1={}'.format(global1))
 
if __name__ == "__main__":
 
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
 
    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))
 
    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2') 
 
    # starting threads
    t1.start()
    t2.start()
    print('3Global1={}'.format(global1))
 
    # wait until all threads finish
    t1.join()
    t2.join()