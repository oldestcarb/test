### 写爬虫过程中遇到的问题

1. Bus error (core dumped)
在linux上运行爬虫脚本时报错，如下：
    ```
    Bus error (core dumped)
    ```
    通过查询，原因为磁盘空间已满，Linux下通过 `df -lh` 查看磁盘使用情况,可以看到已使用为100%。
    ```
    df -lh
    Filesystem            Size  Used Avail Use%     Mounted on
    /dev/mapper/VolGroup-lv_root
                           50G   50G     0 100%     /
    tmpfs                  16G  4.0K   16G   1%     /dev/shm
    /dev/sda1             485M   67M  393M  15%     /boot
    /dev/mapper/VolGroup-lv_home
                          1.1T  269G  712G  28%     /home

    ```

2. 通过csv.writer写入数据每行都会增加一个空行
    ```python
    import csv
    import sys

    with open(sys.path[0] + '/1.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter = ',')
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csvfile,    fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'id': '10001', 'name':'Mike', 'age': 20})

    ```
    读取结果：
    ```
    ['id', 'name', 'age']  
    []  
    ['10001', 'Mike', '20']  
    []  
    ```
    python关于CSV标准库的介绍中有写到:
    > If csvfile is a file object, it should be opened with newline=''. 
    
    打开时加上`newline=''`即可：
    ```
    with open(sys.path[0] + '/1.csv' , 'w', newline='')
    ```