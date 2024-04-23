# 任务1

## 1.VM 虚拟机的联网：
**桥接**+**复制物理机网络状态**
>或者NAT模式然后改地址，但是推荐上面那个。

## 2.VScode ，git的安装：
>官网下载VScode
```
cd  /home/"用户名"/下载
sudo dpkg -i  "安装的code名"
```

>git的安装：
```
sudo apt-get install git
>如果报“E：有未能满足的........”的话，下面这段代码本人*亲测*是有用的：
sudo apt --fix-broken install
>还有几句更新源文件的代码，也许有效.
sudo apt-get update -y
sudo apt-get upgrade -y
```

## 3.git工作流程及VScode上传至github操作：
![alt text](<pictures/git workflow.jpeg>)

### 终端中操作：
* 1.先将文件传入仓库文件夹下,再进入目标文件
* 2.``` git add *("*"表示将所有上传)```
* 3.```git commit  -m “commint说明”```
* 4.```git  git push -u origin master```，输入账号密码就好了
* >如果报 *鉴权失败*  ，应该是github里没有设置Personal access tokens，然后去setting里找Developer settings，然后在Developer settings里找access tokens。通常是没有才鉴权失败，当然也有过期的情况，因为在new access tokens的时候有个时间选择，可以选择某个时间长度(一个月、三个月什么的，因为我个人用的就选择的永不过期)，然后创建成功后会有个token，**把它当作密码**，在你重新推送你项目的时候，命令行提示你输入邮箱和密码的时候，把这个token当密码输入(复制即可)。
  
* 原文链接：https://blog.csdn.net/qq_33320324/article/details/121893271

### VScode操作如下：
* 1.点击左侧第三个**源代码管理**，新建仓库(已有可以选直接上传)
* 2.绑定github
* 3.再进入**源代码管理**可以看到有新文件夹出现，点击“+”暂存(Stage)。随后将出现新文件夹Staged changes
* 4.点击右上角“..."，进行commit操作，**此次需要添加commit说明**
* 5.再进行“push”操作.
* >如果报错：“*没有对应的上游分支*”，则在终端写入```git push --set-upstream origin master```
  
## 附录：Linux中的指令：
### 常用指令：
![alt text](<Linux command.jpeg>)