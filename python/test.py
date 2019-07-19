from multiprocessing import Process,Pool
# -*- coding:utf-8 -*-

import time
from multiprocessing import Process

def test(a):
    print(a)
    time.sleep(5)
    print('------{}----------'.format(a))

if __name__ == '__main__':
    print('start', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    start = time.time()

    p = Pool(4)
    for i in  range(15):
        p.apply_async(test, args=(i,))
    p.close()
    p.join()
    print('=============')
    print('stop', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('all', time.time()-start)