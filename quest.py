import os
import pre
import math
import time
K = int(input('How much would you like to review? :    '))
x = pre.x
cnt = pre.cnt
print(pre.x[0])
for i in range(0, K):
    dd = x[i]
    f = open('prob/{}'.format(dd['no']))
    s = f.read()
    print(s)
    ans = int(input('Do you know how to solve this problem?\n Yes enter 1, No enter 2 :\n'))
    if(ans == 1):
        dd['n']=int(dd['n']) + 1
    dd['N']=int(dd['N']) + 1
    dd['t'] = int(time.time())
    ff = open('ans/{}'.format(dd['no']))
    s = ff.read()
    print(s)
    x[i] = dd
    f.close()
    ff.close()

with open('rem.info', 'w') as f:
    f.write('{}\n'.format(cnt))
    for d in x:
        f.write('{} {} {} {} {}\n'.format(d['no'], d['t'], d['n'], d['N'], d['R']))


