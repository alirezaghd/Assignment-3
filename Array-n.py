import random

Array = []
n = 30
while True:
    num = random.randint(0, n)

    if num not in Array :
        Array.append(num)
    
    
    if len(Array) == n :
        print(Array)
        break
    

    