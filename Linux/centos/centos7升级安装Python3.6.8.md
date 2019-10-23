1. 安装可能用到的依赖
```
yum install -y openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
```
2. 下载Python-3.6.8
```
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
```
3. 解压到当前目录
```
tar -zvxf Python-3.6.8.tgz
```
4. 进入解压后的目录，安装到/usr/local/python
```
cd Python-3.6.8
./configure --prefix=/usr/local/python
```
5. 编译,安装
```
make
make install
```
6. 进入/usr/bin目录,重命名python2的快捷方式,创建python3与pip3软连接
```
cd /usr/bin
mv python python.bak
mv pip pip.bak

ln -s /usr/local/python/bin/python3.6 /usr/bin/python
ln -s /usr/local/python/bin/pip3.6 /usr/bin/pip
```
7. 执行yum需要python2版本，修改yum的配置
```
vi /usr/bin/yum
#!/usr/bin/python改为#!/usr/bin/python2
```
8. 修改urlgrabber配置文件
```
vim /usr/libexec/urlgrabber-ext-down
把第一行#!/usr/bin/python 改为 #!/usr/bin/python2
```