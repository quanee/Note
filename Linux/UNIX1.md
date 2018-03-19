## YUM软件包
#### yum [options] [command] [package]
> options:
> -y:对安装过程所有问题都回答”yes” <br>
> --enablerepo=repoidglob:启用某个已禁用的软件仓库 <br>
> --disablerepo=repoidglob:禁用某个软件仓库 <br>
--nogpgcheck:跳过GPG签名 <br>
command: <br>
&nbsp;install:安装软件包 <br>
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
###安装tar.bz2源代码包
tar zxvf .tar.bz2 // 解压并提取源代码
cd *** // 进入释放文件后自动生成的目录
./configure –prifix=/usr/local/ //安装配置编译环境,安装目录为/usr/local/*** 
make&&make install // 编译和安装 