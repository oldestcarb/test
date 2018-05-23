###　Settings Sync
Sync : Invalid / Expired GitHub Token. Please generate new token with scopes mentioned in readme. Exception Logged in Console.


这个问题大部分是由于gist id的访问令牌token失效了，只需要重新生成一下gist id的token并保存在配置文件里面即可

Regenerate token




注意：这里重新生成之后，有关此gist id引用到的地方的访问令牌也需要同步更新，否则没办法使用。
Replace token
复制重新生成好的token，修改配置文件

Win下：C:\Users\Administrator\AppData\Roaming\Code\User
Mac下：~/Library/Application Support/Code/User/syncLocalSettings.json
Linux下：~/.config/Code/User/syncLocalSettings.json
进入目录后，找到 syncLocalSettings.json 这个文件，查找token，并替换后面复制的值，就可以顺利进行同步配置信息了。