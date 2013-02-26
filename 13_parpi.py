from multiprocessing import Process, Value
import random

def worker(top, v):
    c = 0
    for i in range(top):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1:
            c += 1
    v.value = c
    
    
n = 10000000
ncores = 4
outs = [ Value("d", 0) for i in range(4) ]
processes = []

for i in range(ncores):
    p = Process(target = worker, args=(  n / ncores ,outs[i] ) )
    processes.append(p)
    p.start()

for p in processes:
    p.join() # Wait for completion

c = 0
for out in outs:
    c += out.value

print c / float(n) * 4