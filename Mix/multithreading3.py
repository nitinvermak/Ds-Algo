import threading
import time

def print_square(list1):
    print('Printing Square of List')
    for item in list1:
        time.sleep(0.3)
        print('square={}'.format(item*item))

def print_cube(list1):
    print('Printing Cube of List')
    for item in list1:
        time.sleep(0.3)
        print('cube={}'.format(item*item*item))

def main():
    t = time.time()
    print('Main')
    lst = [1,2,3,4,5,6,7,8,9,10]

    print_square(lst)
    print_cube(lst)

    print('Total time taken={}'.format(time.time()-t))

def main_thread():
    t = time.time()
    print('Main')

    lst = [1,2,3,4,5,6,7,8,9,10]

    t1 = threading.Thread(target=print_square,args=(lst,))
    t2 = threading.Thread(target=print_cube,args=(lst,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('Total time taken={}'.format(time.time()-t))

main()
main_thread()


