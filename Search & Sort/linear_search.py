import random

def linear_search(numbers,item):
    for number in numbers:
        if item == number:
            print(numbers)
            print(item)
            return "Found"
    return "Not Found" 

numbers = random.sample(range(1,1500), 50)

for _ in range(1,100):
    print(linear_search(numbers, random.randint(1,1500)))
