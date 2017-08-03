import os
i = 1
fuck = open('docs/{}'.format(i))
while fuck:
    s = fuck.readline()
    ss = fuck.readline()
    #s = input('请输入题面:')
    #ss = input('请输入答案:')
    f = open('rem.info', 'r')
    cnt = int(f.readline())
    with open('prob/%03d'%(cnt+1), 'w') as F:
        F.write(s)
    with open('ans/%03d'%(cnt+1), 'w') as F:
        F.write(ss)
    cnt += 1
    F = open('rem.info.tem', 'a')
    F.write(str(cnt)+'\n')
    s = f.readlines()
    for line in s:
        F.write(line)
    F.write('%03d 0 0 0 0'%(cnt))
    os.system('mv rem.info.tem rem.info')
    os.system('rm docs/{}'.format(i))
    i+=1
    f.close()
    fuck.close()
    fuck = open('docs/{}'.format(i))
