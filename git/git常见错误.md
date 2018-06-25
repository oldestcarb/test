1. #### 远程仓库地址错误
> remote: This repository moved. Please use the new location [new location] 

解决命令： 
git remote -v 
git remote rm origin 
git remote add origin 远程地址  

2. #### 新建本地分支后将本地分支推送到远程库, 使用git pull 或者 git push 的时候报错

>gitThere is no tracking information for the current >branch.
>Please specify which branch you want to merge with.
>See git-pull(1) for details
>`git pull <remote> <branch>`
>If you wish to set tracking information for this >branch you can do so with:
>`git branch --set-upstream-to=origin/<branch> >merged0.9.6`  

是因为本地分支和远程分支没有建立联系  (使用git branch -vv  可以查看本地分支和远程分支的关联关系)  .根据命令行提示只需要执行以下命令即可
`git branch --set-upstream-to=origin/远程分支的名字 本地分支的名字`   

3. #### 拉取时报错`error: cannot lock ref `
> error: cannot lock ref 'refs/remotes/origin/master': is at b5ae02cb12a32a53d64ad37eecbf9ac7b3e3c66a but expected 0c303efba4d8841845f53eb40019825f6e64839a

解决办法
进入到项目根目录，执行下面命令：
```
rm .git/refs/remotes/origin/dev
git fetch
```