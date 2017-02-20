# UNIX

标签： UNIX

---

## YUM软件包

## CentOS软件包仓库

###使用yum命令列出软件包
    yum list [options] package
    options:
            all:可用的及安装的软件包名
            available:可用的软件包名
            updates:可更新的软件包
            installed:已安装的软件包
            obsoletes:旧的软件包
            recent:最近加入软件仓库的软件包
    package:指定要列出的软件包名称,可以使用通配符*.

### 使用yum命令安装软件包

###使用yum命令删除软件包
    yum remove <package>或yum earse <package>
        package所有以来的软件包也会被删除

###使用yum命令更新软件包
    yum update <package>
    yum upgrade <package>
    yum update-to <package>
    yum upgrade-to <package>
    yum check-update <package>

###更新所有软件包:yum update

###使用yum命令查看软件包
    yum info [options] <package>
    options:
    all:可用的及安装的软件包名
    available:可用的软件包名
    updates:可更新的软件包
    installed:已安装的软件包
    obsoletes:旧的软件包
    recent:最近加入软件仓库的软件包

###软件包组管理
    yum [option] <packageground>
    option:
    grouplist:列出软件包组
    groupinfo:显示软件包信息
    groupinstall:安装软件包组
    groupremove:删除软件包组
    groupupdate:更新软件包组

###Ubuntu软件包命名约定
    <软件包名称>_<版本>-<修订号>_<平台>.deb

### 安装tar.gz源代码包

#### tar zxvf ***.tar.gz     // 解压并提取源代码

### 安装tar.bz2源代码包

#### tar zxvf ***.tar.bz2        // 解压并提取源代码

#### ***    cd ***      // 进入释放文件后自动生成的目录

#### ./configure –prifix=/usr/local/***      //安装配置编译环境,安装目录为/usr/local/***

#### 

#### listuses        // 查看所有用户

#### useradd -g      // 指定主用户组

## OpenSolaris中包括3种类型的系统管理员角色(Role Based Acess Control,RBAC)

### 与用户有关的配置文件

###cat /etc/show
    login:password:lastchanged:mindays:maxdays:warn:incative:expire:reserve 
        login:用户登录名
        password:加密后的密码.密码至少应包含6个字符,加密后至少包含13个字符.如果为空或者为NP,则用户没有设置密码.如果前4个字符为*LK*,则表示用户已经被锁定,处于锁定状态的用户无法登录.如果值为NONE,则表示该用户尚未设置密码,当该用户下次登录是,会要求该用户设定密码.
        lastchanged:表示从1970年1月1日至最近一次修改密码之日的天数.
        mindays:表示用户保持密码不变的最少天数,如果不满足该值,则用户不能修改密码.只有当该值大于或等于0时,才会启用用户密码的有效期检查.
        maxdays:表示用户保持密码不变的最多天数,如果超过这个天数,系统会强制要求用户修改密码,否则不能登录系统.
        warn:表示用户到期多少天前向用户发出警告.
        inactive:表示用户密码到期之后,保持用户信息的最多天数,如果超过这个天数,用户为改密,则锁定账户.
        expire:有效期.用来指定用户有效期的截止日期.
        reserve:保留列.都为空.
    /etc/group
        关于用户组的主要配置文件,存储当前系统中所有用户组以及该组的成员.
     group_name:password:gid:user_list 
        group_name:用户组名称.
        password:用户组密码.通常为空.
        gid:组标识符.无符整数.
        user_list:用户列表.如果组中有多个用户,则每个用户之间用逗号隔开.
    /etc/skel   (root)
        用来存放用户启动文件的目录.
        当使用useradd命令添加用户时,这个目录的启动文件会作为模板自动复制到新用户的目录下.可通过修改,添加,删除/etc/skel目录下的文件来为用户提供一个统一标准的,默认的用户环境.如果通过修改/etc/passwd文件添加用户,则需要手动创建用户的主目录,并把/etc/skel下的文件复制到用户的主目录下,最后在修改这些文件的所有者为新用户.

###添加用户
    useradd username
    passwd username
    通过useradd命令添加的用户为锁定用户,需通过passwd命令设置密码后,方可登录,但无主目录.

####指定主目录
    useradd -d /***/home/username -m username
    -d:为新用户指定主目录(可以是已存在的,也可以是不存在)
    -m:当-d路径不存在时,自动创建,并将所有者设为新用户

####指定默认Shell
    useradd -d /***/home/username -m -s /bin/*** username
    -s:设置默认Shell为/bin/***
    在命令行中输入Shell名称,即可切换为对应的Shell

####指定组
    useradd -g *** -G ***,***,… -d /***/home/username -m username
    -g:设置主组(只有一个)
    -G:设置备用组(多个用逗号隔开)
    可以通过groups username命令来查看用户所属的组

####指定UID
    useradd -m -d /***/home/username -u *** username
    -u:为用户指定UID(如果UID已使用,则系统会提示已占用).可以通过修改/etc/passwd文件使多个登录名共用一个UID
使用/etc/passwd
    vi /etc/passwd
按j↓按a切换到编辑模式,输入
        username:x:110:0:0:/p-d-userhome:/bin/sh
为用户创建主目录
    mkdir /p-d-userhome
将新目录的所有者更改为username
    chown -R username:root /p-d-username
为用户添加信息 /etc/shadow
    vi /etc/shadow
添加
    username:NONE:::::::
为用户设置密码
    passwd username
如果未设置/etc/shadow则会出现错误
    passwd username does not exit
    Permission denied

##修改用户
    usermod [options] login

##修改用户登录名
    usermod -l new_login_name old_login_name

##修改登录名有效期
    usermod -e expire_date login_name
    expire_date常用格式(/etc/datemsk文件中的格式)
        %m/%d/%y %H:%M          %m/%d/%Y %H:%M
        %m/%d/%y                %m/%d/%Y
        %m,%d,%y,%M,%Y,月,日,年,小时,分钟

###修改用户所属组
    usermod -g new_primary_group -G new_supplementary_group login_name
    new_primary_group       新的主组
    new_supplementary_group 新的备用组

###修改用户主目录
    usermod -d home_dir login_name
    修改主目录权限
        chown -R login_name home_dir
    -R:包含所有子目录

###修改用户默认的Shell
    usermod -s shell_name login_name

###删除用户
    userdel login_name
    该命令并不删除用户目录

###删除用户及其主目录
    userdel -r login_name

###添加组(组名长度一般不超过8个字符)

###使用默认选项添加组
    groupadd group_name
    FreeBSD命令
    pw groupadd -n group_name -M users
    -n:新用户组组名
    -M:新用户组成员(多个成员之间用逗号隔开)

###指定组ID