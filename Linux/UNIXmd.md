# UNIX
标签： UNIX
## YUM软件包
#### yum [options] [command] [package]
> options:
> -y:对安装过程所有问题都回答”yes” <br>
> --enablerepo=repoidglob:启用某个已禁用的软件仓库 <br>
> --disablerepo=repoidglob:禁用某个软件仓库 <br>
--nogpgcheck:跳过GPG签名 <br>
command: <br>
install:安装软件包 <br>
update:更新软件包 <br>
update-to:将软件更新至某个版本 <br>
check-update:检查某个软件包是否存在更新  <br>
upgrade:升级软件包,删除旧的软件包并用新的替换  <br>
upgrade-to:升级软件包到某个版本,并删除旧的软件包 <br>
remove或earse:删除软件包 <br>
list:列出软件包 <br>
info:查看软件包信息 <br>
groupinstall:安装软件包组 <br>
groupupdate:更新软件包组 <br>
grouplist:列出已安装的软件包组 <br>
groupremove:删除软件包组 <br>
groupinfo:查看软件包组信息 <br>
search:搜索软件包 <br>
ropolist [all | enable | disable]:查看已经配置的软件仓库  <br>
package:要执行安装,更新或删除等操作的软件包名称,多个软件包之间用空格隔开 
## CentOS软件包仓库 
base:构成CentOS发行版的基本软件包,和光盘上内容相同. 
updates:base仓库中软件的更新版本. addons:已编译的但不在基本软件包中的软件包. 
extras:附加的软件包. centosplus:用于增强一些现有软件包的功能.

/etc/yum.repos.d CentOS-Base.repo:设置远程软件仓库 CentOS-Media.repo:设置本地软件仓库 
CentOS-Debuginfo.repo:用于调试的 软件仓库 .repo文件格式 repositoryis:软件仓库标识
name:软件仓库名称 
basurl:指定本仓库的URL
mirrorlist:仓库的镜像站点 
gpgcheck:检查软件包中的GPG签名
enabled:是否使用本地仓库.默认值为1,即可用
gpgkey:用于指定GPG签名文件的URL
### 使用yum命令列出软件包
yum list [options] package options: 
all:可用的及安装的软件包名 
available:可用的软件包名 
updates:可更新的软件包
installed:已安装的软件包 
obsoletes:旧的软件包 
recent:最近加入软件仓库的软件包 
package:指定要列出的软件包名称,可以使用通配符*. 
### 使用yum命令安装软件包 yum install <package>  
package:要安装的软件包的名称,不要求版本号,yum命令会自动查找适当的版本.
yum命令会自动检查依赖关系,并给出总的下载量(本地安装也是),提示确认下载. 
#### yum search [options] <keyword> 
options: 
all:搜索所有软件包信息 默认只搜索名称和摘要 
keyword:搜索关键字 
### 使用yum命令删除软件包 
yum remove <package>
或yum earse <package> package所有以来的软件包也会被删除 
### 使用yum命令更新软件包 
yum update <package> 
yum upgrade <package> 
yum update-to <package> 
yum upgrade-to <package> 
yum check-update <package> 
### 更新所有软件包:yum update 
### 使用yum命令查看软件包 
yum info [options] <package> 
options:
all:可用的及安装的软件包名
available:可用的软件包名
updates:可更新的软件包 
installed:已安装的软件包
obsoletes:旧的软件包 
recent:最近加入软件仓库的软件包
### 软件包组管理
yum [option] <packageground>
option:
grouplist:列出软件包组 
groupinfo:显示软件包信息 
groupinstall:安装软件包组 
groupremove:删除软件包组 
groupupdate:更新软件包组 
### Ubuntu软件包命名约定 <软件包名称><版本>-<修订号><平台>.deb
### 安装tar.gz源代码包
tar zxvf .tar.gz // 解压并提取源代码 
cd *** // 进入释放文件后自动生成的目录 
./configure –prifix=/usr/local/ //安装配置编译环境,安装目录为/usr/local/*** 
make&&make install // 编译和安装 
### 安装tar.bz2源代码包
tar zxvf .tar.bz2 // 解压并提取源代码
cd *** // 进入释放文件后自动生成的目录
./configure –prifix=/usr/local/ //安装配置编译环境,安装目录为/usr/local/*** 
make&&make install // 编译和安装 
listuses // 查看所有用户
useradd 
-g // 指定主用户组
-G // 指定备用用户组
## OpenSolaris中包括3种类型的系统管理员角色(Role Based Acess Control,RBAC) 主管理员(PA):负责为其他用户分派权限,并负责系统的安全问题,等效于root用户或超级用户等功能强的角色 
系统管理员(SA):负责与安全无关的日常管理工作
操作员(Operator):执行备份和设备维护操作 
### 与用户有关的配置文件 
/etc/passwd (-r--r—r- root other)
该文件中包含了所有用户登录名清单,为所有用户指定的主目录以及用户在登录时使用的Shell名称等信息 
cat /etc/passwd login:password:uid:gid:comment:home:shell
login:用户登录名.首字符必须是字母且至少包含一个小写字母
password:用户密码.若值为x,则该用户设有密码,且密码保存于/etc/shadow.
若值为*,则该用户无法正常登录.
uid:用户标识符.UNIX系统分配给用户的唯一的数字标识. 用户标识符是一个32位无符号整数,位于02,147,483,647之间.099是系统保留给用户使用的,普通用户的用户标识符应该位于100~60,000之间.
gid:用户组标识符.32位无符号整数.0~99保留给系统使用,每个用户至少属于一个用户组.
cemment:用户注释.可以包括用户真实用户姓名,电话号码以及电子邮件地址.
home:用户主目录.UNIX分配给给每个用户的私有目录,仅供个人存储文档使用,除root用户,其他普通用户无法访问其他用户的主目录,同时也是用户登录的初始目录.
shell:用户默认的Shell.Shell就是命令解释器,若值为空,默认使用/bin/sh,即Bourne Shell 
/etc/shadown (-r-------- root sys)
与/etc/password配合使用,保存加密后的用户密码,以及其他有关信息. 
### cat /etc/show login:password:lastchanged:mindays:maxdays:warn:incative:expire:reserve 
login:用户登录名 
password:加密后的密码.密码至少应包含6个字符,加密后至少包含13个字符.如果为空或者为NP,则用户没有设置密码.如果前4个字符为LK,则表示用户已经被锁定,处于锁定状态的用户无法登录.如果值为NONE,则表示该用户尚未设置密码,当该用户下次登录是,会要求该用户设定密码. 
lastchanged:表示从1970年1月1日至最近一次修改密码之日的天数.
mindays:表示用户保持密码不变的最少天数,如果不满足该值,则用户不能修改密码.只有当该值大于或等于0时,才会启用用户密码的有效期检查.
maxdays:表示用户保持密码不变的最多天数,如果超过这个天数,系统会强制要求用户修改密码,否则不能登录系统. 
warn:表示用户到期多少天前向用户发出警告.
inactive:表示用户密码到期之后,保持用户信息的最多天数,如果超过这个天数,用户为改密,则锁定账户. 
expire:有效期.用来指定用户有效期的截止日期. reserve:保留列.都为空.
/etc/group 关于用户组的主要配置文件,存储当前系统中所有用户组以及该组的成员. 
group_name:password:gid:user_list 
group_name:用户组名称. 
password:用户组密码.通常为空. 
gid:组标识符.无符整数.
user_list:用户列表.如果组中有多个用户,则每个用户之间用逗号隔开.
/etc/skel (root) 用来存放用户启动文件的目录. 当使用useradd命令添加用户时,这个目录的启动文件会作为模板自动复制到新用户的目录下.可通过修改,添加,删除/etc/skel目录下的文件来为用户提供一个统一标准的,默认的用户环境.如果通过修改/etc/passwd文件添加用户,则需要手动创建用户的主目录,并把/etc/skel下的文件复制到用户的主目录下,最后在修改这些文件的所有者为新用户. 
### 添加用户 useradd username passwd username
通过useradd命令添加的用户为锁定用户,需通过passwd命令设置密码后,方可登录,但无主目录. 
#### 指定主目录 
useradd -d //home/username -m username
-d:为新用户指定主目录(可以是已存在的,也可以是不存在)
-m:当-d路径不存在时,自动创建,并将所有者设为新用户 
#### 指定默认Shell
useradd -d //home/username -m -s /bin/*** username
-s:设置默认Shell为/bin/*** 在命令行中输入Shell名称,即可切换为对应的Shell
#### 指定组 useradd -g *** -G ,,… -d //home/username -m username
-g:设置主组(只有一个) 
-G:设置备用组(多个用逗号隔开) 可以通过groups username命令来查看用户所属的组 
#### 指定UID useradd -m -d //home/username -u *** username
-u:为用户指定UID(如果UID已使用,则系统会提示已占用).可以通过修改/etc/passwd文件使多个登录名共用一个UID 
使用/etc/passwd
vi /etc/passwd 按j↓按a切换到编辑模式,输入 username:x:110:0:0:/p-d-userhome:/bin/sh 
为用户创建主目录 mkdir /p-d-userhome 将新目录的所有者更改为username 
chown -R username:root /p-d-username 为用户添加信息
/etc/shadow vi /etc/shadow 添加 username:NONE::::::: 
为用户设置密码 
passwd username 如果未设置/etc/shadow则会出现错误 