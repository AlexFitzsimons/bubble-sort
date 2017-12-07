import time
import random
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(numbers)
print (numbers)
for n in numbers:
    x = 1
    i = 0
    while i < len(numbers) - x:
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
        else:
            pass
        i += 1
        time.sleep(0.1)
        print (numbers)