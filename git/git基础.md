### git学习笔记
#### 基础
> 忽略某些文件时，在Git工作区的根目录下创建一个特殊的`.gitignore`文件，`.gitignore`文件本身要放到版本库里，并且可以对.gitignore做版本管理！
```git

git config --global user.name "oldestcrab"

git config --global user.email "oldestcrab@gmail.com"

# 已有的本地仓库与远程库关联
git remote add origin git@github.com:oldestcrab/mybooks.git

# 把当前分支master推送到远程master，-u参数，把本地的master分支和远程的master分支关联起来，后续可不用
git push -u origin master

git clone git@github.com:oldestcrab/mybooks.git

git status

git add

git commit -m 'first commit'

git log

# 查看difference
git diff README.md

# 撤销还没有add进暂存区的文件改动
git checkout a.md

```
#### 分支
```git
# 查看当前分支 
git branch

# 新建分支dev 
git branch dev

# 切换到dev分支 
git checkout dev

# 新建分支dev并切换当前分支为dev
git checkout -b dev

# 合并分支dev到主分支，当前分支为主分支 
git merge dev

# 删除dev分支 
git branch -d dev

# 强制删除dev分支
git branch -D dev

# 推送分支dev
git push origin dev

# 在本地创建和远程分支对应的分支，本地和远程分支的名称最好一致
git checkout -b dev origin/dev
  
# 建立本地分支和远程分支的关联
# git branch --set-upstream-to=origin/远程分支的名字 本地分支的名字
git branch --set-upstream-to=origin/dev dev
```

#### 标签
> 创建的标签都只存储在本地，不会自动推送到远程
```git
# 新建标签v1.0,默认为HEAD，也可以指定一个commit id
git tag v1.0

# 指定标签v1.0信息
git tag -a v1.0 -m "blablabla..."

# 查看所有标签信息
git tag

# 切换到tagv1.0
git checkout v1.0

# 推送一个本地标签v1.0
git push origin v1.0

# 推送全部未推送过的本地标签
git push origin --tags

# 删除一个本地标签v1.0
git tag -d v.10

# 删除一个远程标签
git push origin :refs/tags/v1.0
```