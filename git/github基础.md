### 向GitHub提交代码

#### 参考
> [从0开始学习 GitHub 系列之「向GitHub 提交代码」](https://mp.weixin.qq.com/s?__biz=MzA4NTQwNDcyMA==&mid=2650661821&idx=1&sn=c6116ed82bff2d083bb152fbd8cbc38d&scene=21#wechat_redirect)

1. SSH
你拥有了一个 GitHub 账号之后，就可以自由的 clone 或者下载其他项目，也可以创建自己的项目，但是你没法提交代码。 GitHub 上一般都是基于 SSH 授权的。而大多数 Git 服务器都会选择使用 SSH 公钥来进行授权，所以想要在 GitHub 提交代码的第一步就是要先添加 SSH key 配置。  

2. 生成SSH key
在终端（win下在 Git Bash 里）输入 ssh ,紧接着输入 `ssh-keygen -t rsa` ，指定 rsa 算法生成密钥，接着连续三个回车键（不需要输入密码），然后就会生成两个文件 `id_rsa` 和 `id_rsa.pub` ，id_rsa 是密钥，id_rsa.pub 就是公钥。这两文件默认分别在如下目录里生成：Linux/Mac 系统 在 ~/.ssh 下，win系统在 /c/Documents and Settings/username/.ssh 下，接下来要做的是把 id_rsa.pub 的内容添加到 GitHub 上，这样你本地的 id_rsa 密钥跟 GitHub 上的 id_rsa.pub 公钥进行配对，授权成功才可以提交代码。  

3. GitHub 上添加 SSH key
    - 第一步先在 GitHub 上的设置页面，点击最左侧 SSH and GPG keys
    - 然后点击右上角的 New SSH key 按钮：
    - 需要做的只是在 Key 那栏把 id_rsa.pub 公钥文件里的内容复制粘贴进去就可以了，Title 那栏不需要填写，点击 Add SSH key 按钮就ok了。
    - SSH key 添加成功之后，输入 `ssh -T git@github.com` 进行测试

4. Push & Pull
    - `git push origin master`
    > 把本地代码推到远程 master 分支。   
    - `git pull origin master`
    >把远程最新的代码更新到本地。一般我们在 push 之前都会先 pull ，这样不容易冲突。
5. 提交代码
添加 SSH key 成功之后，我们就有权限向 GitHub 上我们自己的项目提交代码了，而提交代码有两种方法：
    - Clone自己的项目
`git clone git@github.com:stormzhang/test.git`
    - 代码提交
`git push origin master`
    - 关联本地已有项目
切换到 test2 目录，执行如下命令：
`git remote add origin git@github.com:stormzhang/test.git`  

什么意思呢？就是添加一个远程仓库，他的地址是`git@github.com:stormzhang/test.git` ，而 origin 是给这个项目的远程仓库起的名字，是的，名字你可以随便取，只不过大家公认的只有一个远程仓库时名字就是 origin ，为什么要给远程仓库取名字？因为我们可能一个项目有多个远程仓库？比如 GitHub 一个，比如公司一个，这样的话提交到不同的远程仓库就需要指定不同的仓库名字了。
查看我们当前项目有哪些远程仓库可以执行如下命令：
`git remote -v`
接下来，我们本地的仓库就可以向远程仓库进行代码提交了：
`git push origin master`
就是默认向 GitHub 上的 test 目录提交了代码，而这个代码是在 master 分支。当然你可以提交到指定的分支，这个之后的文章再详细讲解。
对了，友情提醒，在提交代码之前先要设置下自己的用户名与邮箱，这些信息会出现在所有的 commit 记录里，执行以下代码就可以设置：
`git config —global user.name "stormzhang"`
`git config —global user.email "stormzhang.dev@gmail.com"`