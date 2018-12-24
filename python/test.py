2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
import multiprocessing
import time
 
def process(num):
    time.sleep(num)
    print ('Process:', num)
 
if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()
 
    print('CPU number:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))
 
    print('Process Ended')