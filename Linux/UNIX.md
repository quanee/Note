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
    groupadd -g gid group_name
    FreeBSD命令
    pw groupadd -g gid -n group_name

###指定重复的组ID
    group -g gid -o group_name
    -o:表示使用已有的GID作为新租ID
    FreeBSD
    pw groupadd -g gid -o group_name

##修改组

###修改组名
    groupmod -n new_name group_name
    group_name:必须为当前系统中已存在的用户组名
    FreeBSD命令
    pw groupadd -l new_name -n group_name

###修改组ID
    groupmod -g gid group_name
    FreeBSD命令
    pw groupmod -g gid -n group_name

###修改为重复的组ID
    groupmod -o -g gid group_name

###删除组
    groupdel group_name
    只删除组,并不删除组成员
    (从/etc/group文件中删除组的定义)

##添加角色(类似用户)

###指定角色基目录
    roleadd -b base_dir -m role_name
    -b:指定角色基目录
    -m:当角色基目录不存在时自动创建主目录
passwd role_name
    角色创建之后还处于锁定状态,设置密码之后,才可以变为可用状态.
/etc/user_attr文件记录角色的扩展属性

#####在FreeBSD等BSD家族的UNIX发行版中,并未引入RBAC安全模型,再基于System V的UNIX发行版中,都引入了基于角色的访问控制模型.

##AIX
    mkrole [attribute=value…] role_name
    attribute=value是角色的一系列初始化属性
    role_name是角色名称

###指定角色主目录
    roleadd -d home_dir role_name
    -d:指定角色主目录
    home_dir:主目录的路径

###指定角色用户组
    roleadd -g primary_group -G supplementary_group role_name
    primary_group,supplementary_group必须为系统中已存在的组
    该角色的成员将成为该角色所在的用户组所在的成员

###指定角色的有效期
    roleadd -e expire role_name
    expire:角色的有效期,格式必须符合/etc/datemsk文件中定义的格式之一

###指定角色的ID
    roleadd -u uid role_name
    uid:必须为未使用的值

###指定角色默认的Shell
    roleadd -s shell role_name
    Shell:未设置默认为/bin/pfsh

###指定角色成员
    usermod -R role1,role2,…login_name
    role1,role2…当前系统中已存在的角色
login_name:当前系统中已存在的登录名
    在添加用户时指定角色
        useradd -R role1,role2,…login_name

###为角色授权
    /etc/user_attr(扩展用户属性数据库)
    该文件定义了用户与角色的关系,以及用户切换到角色后的权限配置文件
        login_name:qualifier:res1:res2:attr
        login_name:用户登录名,值不能为空
        qualifier:描述信息
        3~4列:保留列
        attr:一组用分号隔开的属性及其值的组合,属性形式: key=value
    /etc/security/prof_attr(权限配置属性数据库)
        该文件中定义权限配置文件的名称,说明,权限配置文件的授权以及帮助文件的位置
        profname:res1:res2:desc:attr
        profname:权限配置文件的名称
        2~3列:保留列
        desc:描述信息
        attr:一组由分号分隔开的键名和键值的组合,其中键名可选值有help和auths
    /etc/security/exec_attr(授权属性数据库)
        该文件定义了需要安全属性才能成功运行的命令
        name:policy:type:res1:res2:id:attr
        name:权限配置文件的名称
        policy:与此项相关联的安全策略(可取suser和solaris)
        type:指定实体的类型,目前只能取值为cmd,表示实体类型命令
        4~5列:保留列
        id:标识实体的字符串,对于命令来说应该具有全路径或通配符(*)
        attr:以分号分隔的关键字-值对的可选列表,用于说明将在执行时应用于实体的安全属性,可以指定零个或多个关键字,有效关键字的列表取决于强制执行的策略,对于suser策略,共有4个有效关键字,分别为euid,uid,egid,和gid.
    /etc/security/auth_attr
    该文件定义了所有的授权,这些授权可以直接赋给角色或者用户,写入/etc/user_attr文件中,可以赋给权限配置文件(profile),写入/etc/security/prof_attr文件,然后再将配置文件指定给角色.

######eg:创建一个拥有关闭系统能力的角色

```
1. 添加角色:名称shutdown,密码test
    roleadd -m -d /export/home/shutdown shutdown
2. 修改配置文件.在/etc/security/pro_attr文件中添加所使用的profile,命令:
    vi /etc/security/prof_attr
    在文件末尾添加
    Shut:::Ability to shutdown system
3. 修改定义执行属性文件/etc/security/exec_attr
    vi /etc/security/exec_attr
    在文件末尾添加
    Shut:suser:cmd:::/usr/sbin/shutdown:uid=0
4. 将权限配置文件指派给角色,命令:
    rolemod -P Shut shutdown
5. 添加用户,并为其指定角色
    useradd -m -d /export/home/alice -R shutdown alice
    passwd alice
6. 切换到alice用户,命令如下:
    su -alice
7. 查看用户配置文件
    /export/home/alice$ /usr/bin/profiles
```

8. 查看用户alice的角色

   ```
    /export/home/alice$ roles
   ```

   9. 切换到shutdown角色
/export/home/alice$ su – shutdown

9. 执行关闭系统命令