### git学习笔记
```git
git clone git@github.com:oldestcrab/mybooks

git status

git add

git commit -m 'first commit'

git log

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

# 新建标签
git tag v1.0

# 切换到tagv1.0
git checkout v1.0

# 撤销还没有add进暂存区的文件改动
git checkout a.md

# 推送分支dev
git push origin dev

# 在本地创建和远程分支对应的分支，本地和远程分支的名称最好一致
git checkout -b dev origin/dev

# 建立本地分支和远程分支的关联
git branch --set-upstream dev origin/dev
```