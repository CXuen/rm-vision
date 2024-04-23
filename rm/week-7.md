# 任务1

## 1.VM 虚拟机的联网：
**桥接**+**复制物理机网络状态**
>或者NAT模式然后改地址，但是推荐上面那个。

## 2.VScode ，git的安装：

>官网下载VScode

```bash
cd  /home/"用户名"/下载
sudo dpkg -i  "安装的code文件名"
```

>git的安装：

```bash
sudo apt-get install git
# 如果报 “E：有未能满足的........” 的话，下面这段代码本人*亲测*是有用的：
sudo apt --fix-broken install

# 还有几句更新源文件的代码，也许有效.
sudo apt-get update -y
sudo apt-get upgrade -y
```

## 3.git工作流程及VScode上传至github操作：
![alt text](<pictures/git workflow.jpeg>)

### 操作如下：
* 1.点击左侧第三个**源代码管理**，新建仓库(已有可以选直接上传)
* 2.绑定github
* 3.再进入**源代码管理**可以看到有新文件夹出现，点击“+”暂存(Stage)。随后将出现新文件夹Staged changes
* 4.点击右上角“..."，进行commit操作，**此次需要添加commit说明**
* 5.再进行“push”操作.
* 如果报错：“*没有对应的上游分支*”，则在终端写入

```bash
git push --set-upstream origin master
```
  
## 附录：Linux中的指令：

### 常用指令：
![alt text](<pictures/Linux command.png>)
