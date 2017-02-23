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
$ /usr/sbin/shutdown -i 0 -g 0

   ```
       -i:要转入的运行级别.(关闭系统为0)
       -g:执行时间.(0表示立即执行)
   ```

   ##修改角色
###修改角色名
rolemod -l new_role_name role_name
-l:表示修改登录名

   > *修改角色名称后,该角色用户不会随之改变,必须人工对用户重新分配角色
###修改角色主目录
rolemod -d home_dir
home_dir:表示实际存在的物理路径,且角色需要拥有读写权限
-d:如果指定了不存在的路径,则需要使用-m选项.(如果不使用-m选项,系统不会报错)
###修改角色的主组
rolemod -g primary_group -G supplementary_group role_name
primary_group:主组名
supplementary_group:备用组名
###修改角色有效期
rolemod -e expire_date
expire_date:指定到期时间(/etc/datemsk)
到期之后任何用户都不可以使用该角色
###修改角色默认Shell
角色默认shell为/usr/bin/pfsh,称为pfsh,是因为它是专门由于权限配置文件(profile)的Shell程序之一.
rolemod -s shell_dir
-s:修改默认shell
shell_dir:指定shell路径
###修改角色授权
rolemod -A authorization
-A:修改权限
authorization:表示具体的授权,多个授权之间用逗号隔开
eg:将磁盘管理的权限赋予角色role1
   > 
   > ```
   > rolemod -A solaris.admin.diskmgr.write role1
   > ```
   > 
   > ##删除角色
###使用默认选项删除角色
roledel role_name
实际上是从/etc/passwd文件中删除角色的有关记录
###删除角色主目录
roledel -r -role_name
-r:删除(remove)
同时删除角色的主目录

 

#UNIX文件,目录和档案的操作

###文件类型

- 普通文件:

  > 文本文件,常用来存储文本数据
二进制文件:可执行文件,图像,视频,音频.

- 目录:用来组织和访问其他文件:

  > 每个子目录和文件都在其父目录中拥有一条记录,包括:
I:文件名
II:文件或目录的唯一标识(inode节点)

- 伪文件:

  > ```
  >         I:设备文件,如键盘,显示器等.
  >        II:命名管道:将一个命令的输出连接到另一个命令的输出上面.
  >       III:proc文件,可以访问内核信息.
  > ```
  > 
  > ###目录和子目录
tree / -L 2
-L:输出目录的层数
Solaris系统没有提供tree命令
###链接文件
硬链接:不能跨文件系统.硬链接与源文件是同一文件.创建一个硬链接后,系统本身无法区分那个为源###文件(inode值相同).
软链接:符号链接,可以跨文件系统.
###创建链接文件
ln [options] file_name link_name
options:
-s:建立软链接
###查看inode值
ls -li
inode_value primer link_num owner group size date file_name
  > 
  > >  inode_value:inode值
primer:权限
link_num:链接数
owner:所有者
group:组群
size:文件大小
date:创建日期
file_name:文件名
  > > 
  > > > 删除硬连接不会释放inode节点,只会是指向该inode节点的链接数减1,直到链接数为0时,才会释放该inode节点
####创建软链接
删除原文件后,软链接无变化,但无法访问.
创建软链接时,使用相对路径,保证最大化可移植性.
设备文件
用来表示物理设备的伪文件
①   硬件设备文件
  > > > 
  > > > ```
  > > >   软盘,IDE硬盘,SCSI,SATA或者SAS硬盘,打印机等.
  > > > ```
  > > > 
  > > > ②   终端设备文件
  > > > 
  > > > ```
  > > >   终端,控制台/虚拟控制台,伪终端
  > > > ```
  > > > 
  > > > ③   伪设备文件(/dev/null, /dev/zero)
cat /etc/passwd>/dev/null
cat /etc/passwd>/dev/zero
  > > > 
  > > > ```
  > > >   当处理输出时,这两个伪设备文件的作用相同.
  > > >   当处理输入时,从/dev/null中读取数据,不管请求多少字节,其结果总是eof,从/dev/zero中请求数据,则会返回请求数量的字符,并且这些字符值都为0.
  > > > ```
  > > > 
  > > > eg:创建一个1000字节的文件
dd if=/dev/zero of=temp bs=200 count=5
dd:输入输出工具
if:文件输入
of:文件输出
bs:块大小
count:快的数量
##命令管道 
匿名管道表示方法:|
从功能上讲,匿名管道与命名管道基本相同,都是将一个进程的输出连接到另一个进程的输入.
从特性上讲,两者有明显的区别,首先命名管道必须显式的创建,其次,命名管道不会自动消失,除非用户手动删除命名管道,否则命名管道会一直存在,因此,命名管道可以重复使用.
###创建管道
mkfifo [-m mode] pipe
###删除管道
rm fifo_name
###proc文件
一种提供多种系统信息的伪文件,proc文件直接从系统内核中获取信息,所有proc文件都存储在/proc目录中.
##文件操作
创建文件(vi,>,cp)
创建空白文件
####I.touch [-acm] [-r ref_file|-t tim|-d date_tim] file…
-a:改变访问控制时间
-c:如果目标文件不存在,则不创建该文件
-m:改变修改时间
-r:指定参考文件,touch会依据该文件的事件属性来修改目标文件的时间属性
-t:指定时间属性
-d:指定日期和时间属性
file:要修改其属性的目标文件
####日期和时间格式
[YYYY]MMDDhhmm[.SS]
YYYY.年.MM.月.DD.天.hh.小时.mm.分钟.SS.秒
touch命令可以创建多个文件,文件名之间用空格隔开:
####II.cat file
将file内容输出到屏幕
cat>file
将输入内容,输出到file,按Ctrl+D结束输入
####III.>file
直接创建一个空白文件
###命名文件
####I.  文件名长度可达255个字符
####II. 文件名可以含有除/和null字符之外的任何字符
尽量不使用-作为文件名的首字符,不是使用分号,空格,>,<,|,!等字符(有特殊含义)
尽量选择大写,小写,数字,点,下划线及连字符作为文件名
如果含有分号和空格等字符,在引用文件名时可加入转义字符/.
####复制文件
cp [options] source_file target_file
options:
-i:交互式操作
-p:保留源文件的内容,访问权限,最后访问时间,最后修改时间以及所有者
当目标文件不存在时,cp命令会首先创建它
当目标文件已存在时,cp命令会覆盖它
将一个文件的内容追加到另一个文件的末尾
cat source_file>>target_file
将文件复制到目录
cp [options] filelist directory
###移动文件
mv [options] source_file target_file
options:
-f:直接移动文件或者目录,如果目标文件或者目录已经存在后直接覆盖
-i:交互式移动
  > > > 
  > > > ```
  > > >   mv命令会移动整个目录树
  > > > ```
  > > > 
  > > > ###重命名文件
mv [options] old_file_name new_file_name
options:
-i:交互式重命名
-f:强制重命名
###删除文件
rm [options] file_list
options:
-f:强制删除,不进行任何提示,及时文件被保护
-i:交互式删除,每个文件都需要用户确认
-r或-R:递归删除,删除指定目录,及其子目录的内容
  > > > 
  > > > ```
  > > >           filelist:待删除文件名,多个文件之间用空格隔开(可以使用通配符*)
  > > > ```
  > > > 
  > > > ###防止误删除文件
  > > > 
  > > > ```
  > > >   设置别名
  > > >       alias rm=”rm -i”
  > > >   避免使用root用户删除文件
  > > > ```
  > > > 
  > > > ##目录操作
###显示当前路径
  > > > 
  > > > ```
  > > >   pwd
  > > > ```
  > > > 
  > > > ###切换工作目录
  > > > 
  > > > ```
  > > >   cd [directory]
  > > > ```
  > > > 
  > > > ###创建目录
  > > > 
  > > > ```
  > > >   mkdir [-p] dir…
  > > >   -p:自动创建所有不存在的文件目录
  > > >   dir:目录名称,多个目录之间使用空格隔开(名称使用小写字母可读性强)
  > > > ```
  > > > 
  > > > ###删除目录
rm [options] -r directory
options:
-f:强制删除
-i:交互式删除
###将目录复制到目录
cp [-r|-R] [options] source_directory target_directory
-r|-R:递归复制
source_directory:源目录多个目录之间用空格隔开
###列出目录内容
ls [options] [name]
options:
-a:列出所有的条目,包括隐藏的,点开头文件,工作目录(.),父目录(..)
-A:列出所有的条目,除工作目录(.)和父目录(..)以外的所有目录
-C:多栏输出
-d:如果是目录,则不列出目录内容,只列出目录名称
-F:在文件名后追加表示文件类型的符号
-g:列出条目信息,除所有者
-l:列出条目详细信息
-r:反向排序
-R:递归列出所有子目录的条目
-1:数字1,一行显示一个条目
###通配符
*:匹配任意多个字符构成的序列
?:匹配任意多个字符

```
[list]:匹配list中指定的任意字符
[^list]:匹配不在list中的任意字符
[string1|string2|…]:匹配其中指定的字符串
```

###显示目录树
    Solaris
    find -type d -print|sed -e ‘s;[^/]*/;|___;g;s;___l;l;g’
    FreeBSD
    tree [options] [directory…]
    options:
    -a:显示所有文件,包括隐藏文件
    -d:只显示目录
    -f:显示完整的文件名,包含路径
    -L:显示目录树的深度

##文件和目录权限

###相对权限设置
    chomod [-fR] permissions file..
    -f:强制修改文件权限
    -R:递归设置权限
只有所有者和超级用户才能修改文件权限
相对权限设置只修改参数中指定的权限,而其他地方的权限保持不变

> 用户类型   操作  权限
u:所有者   +:赋予权限  r:读
g:组 -:取消权限  w:写
o:其它组   =:赋予绝对权限    x:执行
a:所有者       
> 
> ####绝对权限
        直接为文件指定最终的权限,而原先的对应权限被清除
> 
> ####递归权限设置
    chomod -R promission file
    递归设置子目录的文件权限
> 
> ###改变文件的所有权
    chown [options] owner [group] file…
    options:
    -f:强制更改所有者
    -R:递归更改所有者
    owner:新的所有者,当前系统中已有的用户登录名
    group:指定文件的组的所有权
    file:要修改的文件列表或目录列表,多个文件和目录之间用空格隔开
> 
> ###改变文件组的所有权
    chgrp [options] group file…
> 
> ###特殊权限
        setuid权限        (s 4000) 所有者
        允许普通用户以root的特权来执行某个命令
> 
> ###仅对可执行文件设置,非可执行文件不可设置,目录可设置,但无效.
setgid权限        (s 2000) 组群
使任意使用者执行设置了setuid权限的文件时,都绑定文件所属的组的权限,任何用户在被设置了setgid权限的目录下新建的文件所属的组都是该目录所属的组,而文件所有者是创建者
粘滞位 (t 1000) 其它(目录)
    使目录下的文件的所有者可以更改,重命名文件,其它用户只有新建,修改权限
> 
> ###权限掩码
    umask [mask]
    mask:权限掩码
    777与mask相减后,为当前创建文件的权限
> 
> ###目录权限
    读:读取目录中的文件名列表
    写:创建,移动,复制,删除以及重命名文件
    执行:进入目录,并搜索目录中的文件
> 
> ###搜索文件
    whereis     (效率高,不全面)
    whereis [-options] program
    options:
    -a:显示指定类型的所有的匹配结果
    -b:只查找二进制文件
    -m:只查找帮助手册
    -s:搜索源代码文件
    -B:指定搜索可执行文件的路径
    -M:指定搜索帮助文件的路径
    -S:指定搜索源代码文件路径
    -f:当用户指定了相关的查找路径时(使用了-B,-M或-S时),就应该使用-f找出所要查找的文件
    -u:查找默认或者指定目录中没有源文件或帮助文档的命令
> 
> ####whereis命令只搜索二进制文件,说明文件和源文件
                 只搜索文件可能出现的位置,不能搜索整个文件系统
> 
> ####通过搜索数据库来搜索文件:locate命令(配合more或less使用)
        locate命令可以搜索整个文件系统,并且可以搜索各种类型文件,通过查询一个特殊的数据库来间接访问地达到搜索文件的目的,在该数据库中,包含所有可以公共访问的文件的路径名,形成一个包含文件名及其路径的索引
> 
> ###FreeBSD
    locate [options] pattern…
    options:
    -0:ASCII码中NUL字符(AISCII值为0)来分隔搜索结果中的多个路径,默认情况下使用换行符(ASCII值为10)来分隔多个路径.
    -S:只显示locate数据库的统计信息
    -c:显示搜索结果中匹配文件的总数,而不是实际的文件名
    -d:指定要搜索的数据库.可多次出现,每次指定一个数据库,也可以出现一次,后面跟随一个用冒号隔开的数据库列表
    -i:忽略字母的大小写
    pattern:要搜索的匹配模式
    Solaris
    slocate [options] pattern…
    options:
    -a:不显示错误
    -i:忽略大小写
    -d:指定所有数据库的路径
    -r:只用正则表达式搜索
    -n:限制搜索结果的数量
    -u:更新slocate数据库
    pattern:搜索的字符串
> 
> ###find命令   (效率低,功能强大)
    通过搜索目录树来搜索文件
    find path… express … action…
    path:路径
    express:条件
    action:操作
> 
> ###路径
    UNIX系统中find命令必须制定一个相对或绝对路径(Linux系统可以省略,为当前路径)
| 条件:               |           常用条件 | 
| ----------------------------------------------------------------------
| -name pattern |名称为pattern的文件或目录,使用通配符’*’,’?’或’[]’时字符串用单引号或转义字符| 
| -iname pattern    |名称为pattern的文件或目录,忽略大小写| 
| -type |文件类型,可以取值为d,f,b,c,p或l,分别表示目录,普通文件,块设备,字符设备,命令管道或链接| 
| -perm mode    |文件模式为mode的文件或目录| 
| -user userid  |所有者为userid的文件或目录| 
| -group groupid    |组为groupid的文件或目录| 
| -size [-+]n[cbkMG]    |指定文件大小,-小于指定大小,+大于指定大小,n具体大小,c,b,k,M或者G分别表示字符,块,千字节,兆字节和千兆字节| 
| -empty    | 空文件| 
| -amin n   | n分钟之前访问的目录或文件| 
| -atime n  | n天之前访问的目录或文件| 
| -cmin n   | 状态在n分钟之前发生改变的文件或目录| 
| -ctime n  | 状态在n天之前发生改变的文件或目录| 
| -mmin n   | n分钟之前被修改的文件或目录| 
| -mtime n  | n天之前被修改的文件或目录| 

##在使用求反运算符时必须前后都有一个空格
运算符一定要放在单引号中或使用转义字符
| 操作                        |   常用操作 | 
| --------------------------------------------------------------| 
| -print    | 将搜索结果写入到标准输出,默认操作
| -fprint file  | 将结果写入file文件中(UNIX不支持),使用>
| -ls   | 显示详细目录列表
| -fls file | 将结果写入file文件中(UNIX不支持),使用>
| -delete   | 将搜索结果文件从磁盘删除
| -exec command{}\; | 执行command参数指定的命令
| -ok command{}\;   | 同-exec,执行命令时要求用户确认

##文件压缩与归档

####压缩与解压缩(gzip和gunzip)

###压缩(.gz格式)
    gzip [options] [name…]
    options:
    -d:解压缩文件
    -l:列出被压缩文件信息
    -r:递归压缩,包括目录中所有的文件和子目录
    -v:显示压缩过程中每个被压缩文件的信息
    -c:将文件压缩或解压缩至标准输出
    name:被压缩文件列表.多个文件之间用空格隔开

> - gzip命令会删除源文件
###解压缩
gunzip [options] [name…]
options:
-r:递归解压
-v:显示解压过程的详细信息
-c:将数据解压是标准输出
大部分软件先用tar命令归档,然后再用gzip压缩
gzcat命令,可以将.gz压缩文件的内容输出到标准文件
###压缩与解压缩命令:bzip2和bunzip2       (.bz2)
bzip2 [options] [filename…]
options:
-d:解压缩文件
-c:将文件压缩或解压缩至标准输出
-t:测试压缩文件的完整性,不解压文件
-v:显示压缩或解压缩的详细信息
###归档命令:tar
tar fuctions tarfile file…
functions:
c:创建新的tar文件
x:解开tar文件
t:列出tar文件中包含的文件的信息
r:追加新的文件到指定的tar文件
u:用新的文件更新tar文件中相应的文件
f:指定归档文件名称.可以使用-表示标准输入或标准输出.
v:tar命令详细的处理过程,即列出每一步处理涉及的文件的信息
z:调用gzip命令对生成的tar归档文件执行压缩,仅在c模式下使用,x或t模式下,忽略
Z:调用compress命令对生成的归档文件执行压缩,仅在c模式下使用,x或t模式下,忽略
j:调用bzip2命令对生成的tar归档文件执行压缩,仅在c模式下使用,x或t模式下,忽略
##文件处理命令
###文件类型识别:file(不一定能够完全准确识别)
file filename…
file命令是根据幻数(magic number)来判断文件类型的
幻数保存在文件的开头几个字节里面,每个文件都有一个幻数
###统计行数,字数以及字符数:wc
wc [options] file
options:
-c:统计字节数
-C:统一字符数
-l:统计行数
-m:统计字符数,同-C
-w:统计字数,字与字之间用空格隔开换行符隔开
###数据的八进制显示:od (octal dump)
od [options] file…
options:
-b:以八进制显示每个字节
-c:显示ASCII字符
-x:以十六进制显示每个字节
###文件对比:cmp (compare)
cmp fiel1 file2
如果file1和file2完全相同,则表示输出
否则,cmp命令会输出第1处不同所在的字节及行号,然后忽略后面的不同之处,执行退出
-l:列出两个文件的所有不同之处
###找出两个文件的相同之处: comm
comm [options] file1 file2
options:
-1:数字1,不输出file1独有的部分
-2:数字2,不输出file2独有的部分
-3:数字3,不输出两个文件共有的部分
默认都输出(分别为第1列,第2列,第3列)
###显示文件的差异:diff和diff3
提示如何对第1个文件进行修改,就可以与第2个文件相同
diff [options] file1 file2
options:
-i:忽略字母大小写
-w:忽略空格以及制表符
-e:只生成一组指令,已提供给其他程序使用
>   
>   ```
>     eg:num1,num2[op]num3,num4
>         op:
>   ```
>   
>     a:  (append)追加
d:  (delete)删除
c:  (change)修改
diff3用来比较3个文件的内容
###文件内容的排序:sort
sort [options] file…
options:
-c:检查排序是否正确
-m:仅仅执行合并操作,该选项会假设指定的多个文件的内容都是有序的.
-o:指定输出文件,缺省默认输出到屏幕
###搜索文件内容:grep
grep [options] pattern file
options:
-c:只输出到符合指定匹配模式的行数
-i:在比较的过程中忽略大小写
-n:显示符合指定模式的行号
-v:输出除符合指定模式以外的所有行
pattern:指定具体的匹配模式,可以同时指定多个模式,也可以使用正则表达式
file:指定要搜索的文件,可以同时指定多个文件,也可以使用通配符
###显示文件内容:cat
cat [options] file…
options:
-b:显示行号,并且忽略空行
-n:显示行号,包括空行
###分页显示文件内容:more和less
more file…
-f:水平方向过长
Enter键:向上移动一行
空格键:向上滚动一屏
###more只向上滚动
less file
Space或f键:向前滚动一屏
b键:向后滚动负一屏
u键:向后滚动半屏
###less双向滚动
###显示前面n行内容
head [-number|-n number] file…
###显示文件后面n行内容:tail
tail [-number|-n number] file…
###vi文本编辑器(Visual Interface)
文本编辑器ex的可视化结果
vi工作模式

###一般模式

> 移动光标
  复制
  粘贴
删除字符
 删除行
> 
> ###编辑模式
   插入替换

###命令模式
保存
退出
搜索

按a,A,i,I
o,O,r或者R键
 按Esc键

按:,/或?键
按Esc键

| vi的3种模式之间的切换                     |
| -------------------------------- |
| 编辑模式:                            |
| 按下i或I键:进入插入状态                    |
| 按下o或O键:插入一行后进入插入状态               |
| 按下a或A键:光标停留在原处,然后进入插入状态          |
| 按下r或R键:进入替换状态                    |
| 按下Esc键:进入一般状态                    |
| -------------------------------- |
| 命令模式:                            |
| 按下:进入命令模式                        |
| 按下/正向查找                          |
| 按下?反向查找                          |
| w 保存      q 退出        q! 保存不退出   |
|                                  |
| 移动光标                             |
| H                                |
| ← J                              |
| ↓ K                              |
| ↑ L                              |
| →                                |
|                                  |
| 0 将光标移动到所在行行首                    |
| $ 将光标移动到所在行行尾                    |
| Ctrl+D    向下移动半屏                 |
| Ctrl+U    向上移动半屏                 |
| Ctrl+B    向上移动一屏                 |
| Ctrl+F    向下移动一屏                 |
| H 移动到窗口第一行                       |
| M 移动到窗口中间行                       |
| L 移动到窗口最后一行                      |
| B 移动到上个字第一个字符                    |
| W 移动到下个字第一个字符                    |
| E 移动到下个字最后一个字符                   |
| ^ 移动到所在行的第一个非空字符                 |
| n-    向上移动n行                     |
| n+    向下移动n行                     |
| nG    直接移动到第n行                   |

###搜索和替换
    搜索:在一般模式按下?或/:输入要搜索的字符串
    替换:     eg:
                        :1,5  s/a/b/g       //替换1~5中的a为b
                        :g/a/s//b/g         //将a全部替换为b

###显示行号
    set number 或 set nu

##隐藏行号
    set nonumber 或 set nonu
| ##插入文本 | -----
| ------------ | ----------------------------------
| i | 在光标所在位置插入文本
| I | 在光标所在行首插入
| a | 在光标所在位置后面插入
| A | 在光标所在行尾插入
| o | 在光标所在行的上面插入一行,然后在行首插入
| O | 在光标所在行的下面插入一行,然后在行首插入
| s | 删除光标后面一个字符然后插入
| S | 清除光标所在行然后插入
| r | 修改光标所在位置字符,然后插入
| R | 从光标所在位置开始,进入改写状态,直到按下Esc键
| 
| -------------------------------------------------------------
| ## 删除文本
| x     | 删除光标所在的一个字符
| nx    | 删除光标所在的n个字符
| dw    | 删除一个单词
| ndw   | 删除n个单词
| dd    | 删除光标所在行
| ndd   | 删除光标开始向下的n行
| d$    | 删除光标到行尾的内容
| U   | 撤销或重复改变
| -----------------------
| 复制和粘贴文本
| yw    | 将光标所在位置至字尾的字符复制到缓冲区
| yy    | 复制光标所在行
| nyy   | 复制光标起的n行
| p | 将缓冲去的文本粘贴到光标处

 

#磁盘管理

##在Solaris中安装磁盘

###创建磁盘文件
    probe -scsi     检查所有SCSI设备的目标号
    boot -r             引导Solaris系统正确配置磁盘文件