import random
import time

def binary_search(numbers,item):
    result = False
    length = len(numbers)
    if length == 1:
        if numbers[0] == item:
            return True
        else:
            return False
    mid = length//2
    if item > numbers[mid]:
        result = binary_search(numbers[mid:],item)
    elif item < numbers[mid]:
        result = binary_search(numbers[0:mid],item)
    elif item == numbers[mid]:
        return True 

    return  result

def ternary_search(numbers,item):
    result = False
    length = len(numbers)
    if length == 1:
        if numbers[0] == item:
            return True
        else:
            return False

    if length == 2:
        if item in numbers:
            return True
        else:
            return False   

    part1 = length//3
    part2 = part1*2

    if item < numbers[part1]:
        result = ternary_search(numbers[0:part1],item)        
    elif item > numbers[part1] and item < numbers[part2]:
        result = ternary_search(numbers[part1:part2],item)
    elif item > numbers[part2]:
        result = ternary_search(numbers[part2:],item)
    elif item == numbers[part1] or item == numbers[part2]:
        return True 
    return  result

def quad_search(numbers,item):
    result = False
    length = len(numbers)
    if length == 1:
        if numbers[0] == item:
            return True
        else:
            return False

    if length == 2 or length == 3:
        if item in numbers:
            return True
        else:
            return False   

    part1 = length//4
    part2 = part1*2
    part3 = part1*3

    if item < numbers[part1]:
        result = quad_search(numbers[0:part1],item)        
    elif item > numbers[part1] and item < numbers[part2]:
        result = quad_search(numbers[part1:part2],item)
    elif item > numbers[part2] and  item < numbers[part3]:
        result = quad_search(numbers[part2:part3],item)
    elif item > numbers[part3]:
        result = quad_search(numbers[part3:],item)
    elif item == numbers[part1] or item == numbers[part2] or item == numbers[part3]:
        return True 
    return  result


def penta_search(numbers,item):
    result = False
    length = len(numbers)
    if length == 1:
        if numbers[0] == item:
            return True
        else:
            return False

    if length == 2 or length == 3 or length == 4:
        if binary_search(numbers,item):
            return True
        else:
            return False   

    part1 = length//5
    part2 = part1*2
    part3 = part1*3
    part4 = part1*3

    if item < numbers[part1]:
        result = penta_search(numbers[0:part1],item)        
    elif item > numbers[part1] and item < numbers[part2]:
        result = penta_search(numbers[part1:part2],item)
    elif item > numbers[part2] and  item < numbers[part3]:
        result = penta_search(numbers[part2:part3],item)
    elif item > numbers[part3] and  item < numbers[part4]:
        result = penta_search(numbers[part3:part4],item)
    elif item > numbers[part4]:
        result = penta_search(numbers[part3:],item)
    elif binary_search([part1,part2,part3,part4],item):
        return True 
    return  result




start = time.time()
# Sorted array with random items
numbers = sorted(random.sample(range(1,11000000), 10000000))

print('Random List Creation- Time taken: {} seconds'.format(time.time() -start))


# Just to increase the work load  ||  Will Search a random Int that many time
iterations = 100

start = time.time()
for _ in range(iterations):
    search = random.randint(1,11000000)
    result = binary_search(numbers,search)
 
print('Binary Search Time taken: {} seconds'.format(time.time() -start))

start = time.time()
for _ in range(iterations):
    search = random.randint(1,11000000)
    result = ternary_search(numbers,search)
 
print('Ternary Search Time taken: {} seconds'.format(time.time() -start))

start = time.time()
for _ in range(iterations):
    search = random.randint(1,11000000)
    result = quad_search(numbers,search)   
 
print('Quad Search Time taken: {} seconds'.format(time.time() -start))

start = time.time()
for _ in range(iterations):
    search = random.randint(1,11000000)
    result = penta_search(numbers,search)

print('Penta Search Time taken: {} seconds'.format(time.time() -start))