import random

random.seed(id(1))

def main(a):
    i=0
    n = 0
    while i!=a:
        n = n + random.randint(0,10)
        i = i+1
        
    return float(n/a)

print (main(100000))
