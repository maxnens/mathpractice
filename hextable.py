from random import randint
from time import time

start = time()
score = 0
elapsed = time() - start
while elapsed < 60:
    x = randint(0,256)
    result = "wrong"
    try:
        answer = int(input("0x{:02X} = ".format(x)))
        if answer == x:
            score += 1
            result = "good"
    except ValueError:
        result = "BAD"
    elapsed = time() - start
    print("{:0.3f}] {}: {}".format(elapsed, result, score))

print("DONE! {} correct answers".format(score))
