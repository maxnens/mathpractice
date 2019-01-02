from random import randint
from time import time

start = time()
score = 0
elapsed = time() - start
while elapsed < 60:
    x = randint(2,12)
    y = randint(2,12)
    result = "wrong"
    try:
        answer = int(input("{} x {} = ".format(x,y)))
        if answer == x * y:
            score += 1
            result = "good"
    except ValueError:
        result = "BAD"
    elapsed = time() - start
    print("{:0.3f}] {}: {}".format(elapsed, result, score))

print("DONE! {} correct answers".format(score))
