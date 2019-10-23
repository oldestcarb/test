1. 进入centos的yum文件夹，用wget下载repo文件
```
cd  /etc/yum.repos.d/
wget  http://mirrors.aliyun.com/repo/Centos-7.repo
```
1. 备份系统原来的repo文件
```
mv CentOS-Base.repo CentOS-Base.repo.bak
```
3. 替换系统原理的repo文件
```
mv Centos-7.repo CentOs-Base.repo
```
1. yum源更新
```
yum clean all
yum makecache
yum update
```