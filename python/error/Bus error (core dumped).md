### Bus error (core dumped)


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