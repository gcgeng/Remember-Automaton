import math
import time
from operator import itemgetter
cnt = 0
with open('rem.info', 'r') as f:
    x = []
    lines = f.readlines()
    for line in lines:
        a = line.rstrip().split()
        if(len(a) > 1):
            if(int(a[1]) != 0):
                #s = int(a[2]) / int(a[3])
                s = 1
                r = math.e ** -((int(time.time()) - int(a[1])) / s)
            else: r = 0
            d = dict(no = a[0], t= a[1], n = a[2], N = a[3], R = r)
            x.append(d)
        else: cnt = int(a[0])
x = sorted(x, key = itemgetter('R'))
print(x)
