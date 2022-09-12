import random

numbers = random.sample(range(1,1000), 10)
search = random.randint(1,100)

def linear_sot(array):
    count = 1
    min = 0
    for a in range(len(array)):
        print('--------------a={}'.format(a))
        min = array[a]
        for b in range(count,len(array)):
            print('--------------b={}'.format(b))
            if array[b] < min:
                min =array[b]
                temp = array[a]
                array[a] = array[b]
                array[b] = temp
                print(array)
            
        count+=1
    return array


print(numbers)
print(linear_sot(numbers))

