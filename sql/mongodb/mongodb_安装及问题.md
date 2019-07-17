### mongodb安装教程

1. 下载
    >  [mongodb](https://www.mongodb.com/download-center/community)

2. win下安装
    选择安装路径：
    ```
    D:\program\progran_databases\MongoDB\Server\4.0\data\
    ```
    进入安装目录，bin目录位置新建同级目录data，进入data新建文件夹db，作为数据储存目录
    以管理员进入bin目录，设置mongodb服务
    ```
    mongod --bind_ip 0.0.0.0 --logpath  "D:\program\program_databases\MongoDB\Server\4.0\log\mongodb.log" --logappend --dbpath   "D:\program\program_databases\MongoDB\Server\4.0\data\db" --port 27017 --serviceName  "MongoDB" --serviceDisplayName "MongoDB" --install
    # 绑定 IP 为 0.0.0.0，即任意 IP 均可访问，指定日志路径、数据库路径、端口，指定服务名称
    ```
    添加环境变量
    ```
    D:\program\program_databases\MongoDB\Server\4.0\bin
    ```
### 安装pymongo
```
pip3 install pymongo
```

### robomongo
[robomongo](https://robomongo.org/download)