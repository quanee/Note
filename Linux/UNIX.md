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
    dmesg               查看系统日志
    devfsadm            为新的磁盘创建适当的设备文件

###格式化磁盘
    UNIX系统的格式化相当于Windows中的低级格式化
    UNIX系统的创建系统文件相当于Windows中的格式化或高级格式化

###HP-UX系统
    mediainit

###Solaris系统
    format
    disk:选择磁盘
    type:选择或定义磁盘类型
    partition:选择当前磁盘的描述信息
    current:显示当前磁盘的描述信息
    format:格式化磁盘
    fdisk:创建fdisk分区
    repair:修复有缺陷的扇区
    label:将磁盘标签写入磁盘
    analyze:分析磁盘表面
    defect:缺陷列表管理
    backup:搜索备份盘标签
    verify:读取和显示磁盘标签
    save:保存新的磁盘/分区定义
    inquire:显示磁盘标识
    volname:设置最多8个字的卷名
    !:执行命令
    quit:退出format命令

###创建Solaris fdisk分区
    fdisk分区是基于x86平台的Solaris系统所特有的功能
    format>fdisk

###磁盘分片和标记磁盘
    format>partition
    partition:
    0~n:分别设置磁盘分片0~n的属性
    select:选择预定义的分区表
    modify:修改预定义的分区表
    name:命名当前分区表
    print:显示当前分区表
    label:将分片映射和磁盘标签写入磁盘
    !:执行命令
    quit:退出partition命令

###创建文件系统
    nesfs /dev/rdsk/c4todoso
    创建一个标准的UFS文件系统
    FreeBSD
    sysinstall

##监控文件系统

###监控磁盘剩余空间display free disk space
    df [options] [filesystem]
    options:
    -a:统计所有的文件系统的剩余空间,包含设置了MNT_IGNORE选项的文件系统
    -b:FreeBSD:使用512字节的数据块来显示,覆盖当前环境的BLOCKSIZE变量
                Solaris:以KB为单位显示文件系统总的可用空间
    -g:FreeBSD:以GB为单位显示磁盘情况
                 Solaris:显示整个statvfs结构
    -H或-h:使用容易阅读的格式来显示
    -k:以KB为单位显示磁盘空间情况
    filesystem:要显示其剩余空间情况的文件系统.缺省表示当前系统

###监控磁盘使用情况(disk usage)
    du [options] file…
    options:
    -h:以容易阅读的格式显示
    -d:FreeBSD:显示目录树级别
                     Solaris:只统计指定的文件系统的信息
    -s:对于指定的文件或者目录,只显示一条输出结果
    -t:FreeBSD:指定文件大小阈值,超过该阈值的文件才会显示
                    Solaris无该选项

###创建文件系统

####newfs命令及其选项(new file system)
    newfs [options] specialfile
    options:
    -E:在创建文件系统前清除磁盘上的数,不适用于Solaris
    -L:为新文件系统指定卷标,不适用于Solaris
    -N:只输出文件系统参数,而不是真正创建文件系统
    -O:指定文件系统类型,如果指定为1,则创建UFS1系统,如果为2,则创建UFS2文件系统,默认创建UFS2.不适用于Solaris
    -U:在新文件系统上启动soft updates技术,仅适用于FreeBSD
    -b:指定文件系统块的大小,值必须为2的n次方
                    FreeBSD缺省为16384
                    Solaris缺省为8192
    -c:每个柱面组包含的块的数量
    -f:磁盘磁片的大小
    -i:指定文件系统中i节点的密度.默认情况下每4个字节创建1个i节点
    -m:为普通用户保留的磁盘空间的百分比.默认为8%
    -n:在FreeBSD中,不要在文件系统中创建.snap目录(会导致该文件系统中不支持快照)
    -p:指定要创建文件系统的BSD分区,其值为a~h
    specilafile:要创建文件系统的特殊设备文件名称

###挂载和卸载文件系统

####挂载
    mount [options]
    options:
    -p: 列出当前系统已挂载的文件系统
    -v: 开启冗余模式(verbose mode)显示一些附加信息

####文件系统挂载选项
    -a: 使用该选项,mount命令将挂载/etc/fstab文件中描述的所有文件系统,除了被标记为noauto,late或者-t标志排除的文件系统,以及已挂载的文件系统.
    -f:强制挂载个不干净的文件系统
    -o:指定挂载选项
| 
| ---------------------------------------------------
| async |为文件系统启用异步I/O
| force |与-f相同
| fstab |与-u配合使用时,表示应用/etc/fstab文件中关于该文件系统的所有选项
| late  |当使用-a选项时,制定该选项的文件将被忽略
| noasync   |元数据的I/O采用同步的方式,数据的I/O采用异步方式,默认.
| noatime   |当读取文件时不要更新最近访问时间属性,通常用于文件系统中文件非常多,对于性能要求又非常高的场合.
| noauto    |当使-a选项时,包含该标志的文件系统将不会被挂载
| noexec    |不允许在被挂载的文件系统中执行任何二进制文件
| nosuid    |不允许粘滞位发生作用
| ro    |以只读的方式挂载文件系统,与-r相同
| snapshot  |允许文件系统的快照
| sync  |所有的I/O操作都将以同步的方式进步
| union |使用联合文件系统,挂载点中原有的内容与被挂载的文件系统中的内容同时可用.
|   -r: 只读挂载指定的文件系统
|   -t: 指定要挂载的文件系统的类型,默认值为ufs
|   -w: 文件系统以读写的方式挂载,不适用于Solaris

###卸载文件系统
    umount [options] special_file | node
    options:
    -a:卸载fstab文件中描述的所有文件系统
    -A:卸载当前已挂载的所有文件系统,除根文件系统之外,只适用于FreeBSD
    -F:指定fstab配置文件,只适用于FreeBSD
    -f:强制卸载某个文件系统
    -t:指定要卸载的文件类型

###查看文件系统使用者
    fuser [options] file
    options:
    -c:显示包含指定文件的文件系统中关于任何打开的文件的报告
    -f:仅报告指定文件的使用情况
    -k:将SIGKILL信号发送到每个本地进程
    -u:为进程号后圆括号中的本地进程提供登录名

###挂载MS-DOS文件系统
    mount_msdosfs [options] special_file node
    options:
    -o:指定挂载选项
large   支持超过128G的大文件系统
longnames   支持Windows长文件名
shortnames  只支持Windows短文件名,即文件名的长度不超过8个字符,扩展名长度不超过301个字符
nowin95 忽略Windows95的扩展的文件信息
    -u:指定文件系统中文件的所有者
    -g:指定文件系统中文件的所属的组
    -m:指定文件系统中文件权限掩码
    -s:强制忽略Windows的长文件名
    -l:强制列出Windows的长文件名
    special_file:要挂载的文件系统所对应的特殊文件
    node:挂载点

###挂载NTFS文件系统
    mount_ntfs [options] special_file node

###挂载Linux文件系统
    mount t ext2fs special_file node

###挂载和卸载基于CD-ROM的文件系统
    mount_cd9860 [options] special_file node

###检查和修复文件系统

####fsck命令简介
    进入单用户模式
    FreeBSD
    init 1
    shutdown +5
    Solaris
        init s | init S
    fsck [options] special_file | node
    options:
    -f:强制检查所有的文件系统,即使某个文件系统被标记为clean
    -n:对于检查过程的所有问题都默认给否定(no).除CONTINUE以外.
    -p:进入整理(preen)模式,可以修复一些轻微的错误
    -y:对检查过程中所有问题都回答(Yes)
    -m:适用于Solaris,之检查,不修复.
    -F:适用于Solaris,指定要检查的文件系统类型
    -t:适用于FreeBSD,指定要检查的文件系统类型
    special_file:要检查的文件系统所对应的特殊文件
    node:文件系统的挂载点

####fsck命令的工作过程

1. 检查inode节点格式的正确性
如果inode有问题,标识为BAD
如果有问题且已被另外的文件所引用,则标识为DUP
2. 查找i节点号越界的块
从操作系统根目录检查所有的目录项,检查在第一步中发现的i节点号越界的块,默认情况下,删除整个目录或者文件
3. 查找没有被引用的目录
在UNIX操作系统中,默认情况下每个文件系统下都有lost+found这个系统目录,在fsck命令修复时,查找没有被引用的目录,并保存到此目录.
4. 核对i节点的链接数与目录文件的记录数
逐个核对i节点的链接数与目录文件的记录数.并给出相应的提示与操作.该过程会最大限度修复被损文件
5. 检查超级块
将可用块数与保持在超级块中的块数进行比较
如果发现问题会提示系统管理员,是否进行自动修复
如果自动修复,会利用新计算出的块列表替换旧的错误的块列表
使用fsck检查和修复文件系统
单用户模式:首选的执行文件系统检查的环境
多用户模式:卸载被检查文件系统后执行fsck命令
##磁盘配额

   >   磁盘配额需要UNIX内核支持
FreeBSD的磁盘配额内置于GENERIC内核
重新编译自定义内核,并在内核中加入一行
options QUOTA
编译并安装完自定义内核后,在/etc/rc.conf文件中加入
quota_enable=”YES”
check_quota=”NO”
   > 
   > ```
   > 启用磁盘配额服务
   > 启动时跳过一致性检查
   > ```
   > 
   > ###分配磁盘配额
在/etc/fstab文件中需要应用配额的文件系统设置配额选项
在fstab文件第4列中加上userquota或groupquota选项
验证文件系统的磁盘配额是否启用
FreeBSD
##edquota -u username
-u:要设置磁盘配额的用户
-v:验证是否分配成功
-p:将配额应用到ID在某个范围之内的所有用户
 
##进程和作业
##监视进程
ps [options]
options:
-a:列出与任何用户标识和终端相关的进程信息
-A:列出所有的进程,包括守候进程,该选项的作用与-e选项相同
-e: 列出所有的进程,包括守候进程
-f:显示每个进程的完整信息
-l:以长格式显示每个进程
-o:指定显示格式
-p:显示指定进程ID的进程信息
-u:显示与指定用户ID相关的进程的信息
-t:只显示与某个终端相连的进程的信息
缺省只列出与当前用户和终端有关的进程
###BSD版本
a:显示所有用户和终端相连的进程
e:同时显示进程运行的环境
p:显示指定进程ID的进程
u:显示与指定用户ID有关的进程
###Solaris中的ps命令的常见列及其涵义
ADDR    进程的内存地址
C       处理器的利用率
CMD 正在被执行的命令的完整文件名以及参数
NI  进程的nice值,用于设置进程的优先级
PID 进程ID
PPID    父进程ID
PRI 进程优先级
S       进程状态,包括O,S,W,R,T和Z
STIME   进程运行的总时间
TIME        进程累计CPU时间
TTY 进程的控制终端名称,如果没用控制,则显示一个问号
UID 进程的用户ID
###FreeBSD的ps命令的常见列及其涵义
%cpu            处理器(CPU)的使用百分比
%mem            真实内存的使用百分比
cmd         正在被执行的命令的名称
command 正在被执行的命令的完整名称,包括参数
cpu         短期处理器的使用
nice或者ni    nice值,用于设置进程优先级
pgid            进程组ID
pid         进程ID
ppid            父进程ID
pri         调度优先级
re          内存驻留时间,以秒为单位
rss         内存驻留空间大小
sl          睡眠时间,以秒为单位
stat            状态码,包括D,I,L,R,S,T,W以及Z
time            累计CPU时间
tsize       文本大小,以KB为单位
tt          控制终端的缩写,通常是两个字母
tty         控制终端的完整名称
uid         用户标识
user            用户名
vsz         虚拟内存大小
###Solaris的状态码
O:正在运行
S:可中断睡眠状态,进程在等待某个事件的发生
R:可运行状态,正在运行队列中等待
W:进程正在等待CPU的使用率降低至阈值以下
T:挂起状态,有作业控制信号或者因为追踪而被挂起
Z:僵死状态
###FreeBSD&Linux
D:不可中断的睡眠状态,等待事件的结果,通常是I/O
I:空闲状态,超过20秒的睡眠,仅适用于FreeBSD
R:可运行状态
S:睡眠状态,少于20秒
T:挂起状态,有作业控制信号或者因为追踪而被挂起
Z:僵死进程
###搜索进程
pgrep [options] pattern
options:
-g:指定要搜索的进程的组ID
-G:指定要搜索的进程所属的真实组ID
-l:以长格式显示匹配结果,包括进程ID和进程名称
-P:匹配父进程为指定ID的进程
-u:匹配有效用户ID为指定ID的进程
-U:匹配真实用户ID为指定ID的进程
###监控进程 (Solaris)
top [options] [number] (动态)
options:
-I:不显示空闲进程
-S:显示进程
-C:显示完整的命令名称
-i:交互模式
-q:快速模式,top进程本事的nice将变为-20,获得更高的优先级
-d:只显示指定次数然后退出top命令
-o:指定用来排序的列
   > 
   > > ####运行时命令:
o:指定排序标准
p:以CPU时间的占用百分比排序
q:退出top命令
r:改变进程优先级
s:改变屏幕刷新时间间隔
T:以进程所使用的系统和用户时间排序
prstat [options] [interval [count]]
options:
-n:该选项用来指定prstat命令输出的行数
-p:指定要显示的进程ID列表
-s:指定作为降序排列标准的列
-S: 指定作为升序排列标准的列
-t:统计每个用户的资源使用情况
-u:只列出有效用户ID出现在指定列表中的进程
-U:该选项只列出真实用户ID出现在指定列表的进程
###显示进程树
ptree [options] [pid|user]…
options:
-a:显示所有进程
###BSD&Linux
pstree [options] [pid|username]
options:
-g n:指定使用图形字符绘制进程树分支
   > > 
   > > ```
   > >              n为1,2,3时,分别表示使用IBM-850,VT100以及UTF-8
   > > ```
   > > 
   > > -l n:指定进程树的深度为n
-u:只显示指定用户的进程
-p:只显示包含指定进程ID的分支
##控制进程
###设置进程优先级
nice [-n increment] command
-n:指定优先级,increment是由符号十进制整数(-20~19),代表优先级,值越大,优先级越低,默认为10
HP-UX的nice值范围是0~39
###改变进程优先级
Ctrl+Z:挂起进程
Ctrl+C:终止进程
###将进程移动到后台
bg %n
n:后台作业号
renice [-n increment] -p processed…
-n:指定新的优先级
-p:指定进程ID列表
###杀死进程
kill命令分为内部命令和外部命令
   > > 
   > > ```
   > > 一般为外部命令
   > > ```
   > > 
   > > kill [-9] pid…|jobid…
pid:进程ID
jobid:作业ID
pkill [options] [pattern]
options:
-g:进程所属的用户组ID或者用户组名
-G:进程的真实组ID或者组名
-n:最新(newest)创建的进程
-o:最旧(oldest)的进程
-P:进程的父进程ID
-u:进程的有效用户ID或者用户名
-U:进程的真实用户ID或者用户名
pattern参数表示要匹配的模式
 
##信号
###UNIX系统中的常见信号
| 编号    |名称 |缩写|    说明|
| -------|------|-----|---------------------------------|
| 1 |SIGHUP |HUP    |中止:注销或者终端失去连接时发送给进程
| 2 |SIGINT|INT |中断:当按下Ctrl+C组合键时发送
| 9 |SIGKILL|KILL|  杀死:立即终止,进程不能捕获
| 15    |SIGTERM|   TERM|   终止:请求终止,进程不能捕获
| 18|   SIGCONT |CONT   |继续:恢复挂起的进程,由fg或者bg发送
| 19    |SIGSTOP|   STOP|   停止(挂起):当按下Ctrl+Z组合键时发送
###查看当前系统支持的信号
kill -l
尽量使用信号名称或者缩写来代替具体的编号
可以通过signal.h文件查看当前系统中支持的信号
more /usr/include/sys/signal.h
###kill命令信号发送
kill -s signal_name pid…
或者
kill [-signal_name] pid…
或者
kill [-signal_number] pid…

#10.4作业控制

##10.4.1    作业
    进程加作业控制为作业,一个作业可能包含多个进程(多个进程ID),但只有一个作业ID

##10.4.2    后台运行作业
    在命令末尾附加&符号,可以将命令放到后台运行

##10.4.3    挂起作业
    Ctrl+Z
    作业的3种状态:前台运行,后台运行及暂停并等待信号恢复运行

##10.4.4挂起Shell
    suspend [-f]
    -f:强制执行命令

##10.4.5显示作业列表
    jobs [options]
    options:
    -l:显示进程ID及工作目录

##10.4.6将作业移至后台
     I.在命令后加&
    II.Ctrl+Z
        bg [%jobid]
            +:当前作业
            -:上一个作业

##10.4.7将作业移至前台

###将当前作业移至前台
fg [ |%%|%+]

###将上一个作业移至前台
    fg %-

###将作业ID为n的作业移至前台
    fg %n

##10.4.8作业调度:cron
    在使用cron的系统中,都有一个crond守护进程,这个进程会定期检查是否有预定的作业需要执行,通常情况下,间隔1分钟.crond进程读取的作业都存储在一个名称为crontab的文件中.
    crontab文件格式
|   *   |       *   |       *   |       *   |       *   |       要执行的命令|
| ----------------------------------------------------------------
  |分钟   |  小时   |   日   |    月   |    周|
星期日可以使用0或者7来表示
如果日期和星期同时被设定,那么只要其中的一个条件被满足时,指令便会被执行

###crontab [options] [file]
    option:
    -u:指定要处理的crontab文件所属的文件
    -l:列出crontab文件的内容
    -r:删除crontab文件的内容
    -e:编辑crontab文件的内容

##10.5常见问题

###10.5.1理解交换进程与init进程
    在UNIX系统中,进程ID为0的进程为交换进程(swapper),又称为调度进程.该进程不调用磁盘上的任何程序,是内核的一部分.
    进程ID为1的进程为init进程,在系统引导结束时,由内核创建,先由调度进程创建一个内核线程,然后由该线程通过exec系统调用执行/sbin/init程序,从而创建出init进程.init进程读取初始化文件(/etc/rc脚本文件),并将系统引导至某个特定的状态.

###10.5.2Shell进程
    Shell进程负责解释用户输入的命令,提供内核与用户之间的接口
    Shell进程的执行过程    :
    (1) 读取用户输入的命令
    (2) 分析命令以及配置参数
    (3) 创建子进程
    (4) 对于前台作业,Shell进程会调用wait系统调用来等待子进程的结束
    (5) 子进程结束后,会返回执行状态并唤醒父进程,打印出命令提示符,等待用户的下一个命令
 

#网络管理

##11.1TCP/IP协议简介

###11.1.1TCP/IP协议和Internet

> - 1941年,第一部电子计算机
>   
>   > - 20世纪70年代,NCP(Network Control Protocol)协议
>   >   
>   >   > > - 1972年,罗伯特 卡恩研究卫星数据包网路和地面无线数据报网络,1973年春天,NCP协议开发者文顿 瑟夫加入.
>   >   > >   
>   >   > >   > > > > - 1973年夏天,开发出基本改进形式,网络协议之间的不同通过一个公有互联网络协议隐藏,随后开发出TCP v1,TCP v2,TCP/IP v3,及目前仍在使用的TCP/IP v4互联网标准协议
>   >   > >   > > > > >   >   > >   > > > > - 1975年,TCP/IP在斯坦福和伦敦大学之间进行测试,1977年11月,TCP/IP在美国,英国和挪威之间测试.1983年1月1日,ARPANET完全转换到TCP/IP
>   >   > >   > > > > >   >   > >   > > > > - 1984年,美国国防部将TCP/IP作为所有计算机网络的标准

##11.1.2TCP/IP协议网络模型

- 1983年国际标准化组织(International Organization for Standardization, ISO)提出开放式通信系统互联参考模型(Open System Interconnection Recference Model, OSI)
- OSI模型将计算机网络体系结构分为7层:
- 应用层(Application Layer)
- 通过应用层应用程序接口与具体的应用程序沟通
- 表示层(Presentation Layer)
- 向应用程序提供信息和数据的表示方式,使不同表达方式的系统之间能够通信
- 会话层(Session Layer)
- 管理参与会话的实体之间的对话连接
- 传输层(Transport Layer)
- TCP/IP协议所在层,也是最重要的一层.总体的数据传输和数据传输控制,数据的传输单位:段(segment)
网络层(Network Layer)
提供路由和寻址,数据的传输单位:数据报(datagram)
数据链路层(Data Link Layer)
管理两个网络实体之间的数据链路连接的建立,维持和释放等,数据的传输单位:帧(frame)
物理层(Data Link Layer)
规定了数据传输时所需要的物理链路的一系列的电子,电气特性,确保原始的电子信号能够在各种物理介质上传输,数据的传输单位:比特(bit),即位.
TCP/IP参考模型

 

###11.1.3端口
    常见服务及其默认端口
服务  默认端口    服务  默认端口
FTP数据传输 20  FTP控制命令 21
远程登录(SSH)   22  电子邮件(SMTP)  25
电子邮件(POP3)  110 安全超文本传输(HTTPS)  443
DHCP客户端 546 DHCP服务  547
11.2IP地址
11.2.1IP地址分类
    IPv4
A,B以及C类网络的相关参数
网络类别    前缀位 最大网络数   第一个可用的网络号   最后一个可用的网络号  每个网络中的最大主机数
A   0   126 1   126 16777214
B   10  16382   128.1   191.255 65534
C   110 2097150 192.0.1 223.255.255 254

1. A类IP地址(最优)
xxxx.xxxx.xxxx.xxxx
网络地址   主机地址

2. B类IP地址
xxxx.xxxx.xxxx.xxxx
网络地址   主机地址

3. C类IP地址
xxxx.xxxx.xxxx.xxxx
网络地址   主机地址
11.2.2子网和子网掩码
子网(subnet):从分类网络中划分出来的一部分网络
包括网络地址,子网号以及主机地址.1
子网掩码(subnet mask):用来区分IP地址的网络地址位和主机地址位
子网掩码的左边表示网络地址位用二进制1表示,1的个数等于指定IP地址中网络地址所占的二进制位数;右边是主机地址位,用二进制0表示,0的个数等于指定IP地址中主机地址所占的二进制位数
11.2.3专用地址和NAT
互联网号码分配局(Internet Assigned Numbers Authority, IANA)分配的IP地址称为公用地址
A类网络专用IP地址  10.0.0.1~10.255.255.254
子网掩码:255.0.0.0
B类网络专用IP地址  172.16.0.1~172.31.255.254
子网掩码:255.240.0.0
C类网络专用IP地址  192.168.0.1~192.168.255.254
子网掩码:255.255.255.0
专用地址不能从互联网接受对方发过来的数据,如果某台主机使用专用地址,同时又要与互联网上的其他主机进行通信,则该专用地址必须转换成公用地址,这个过程称为为网络地址转换(Network Address Translation, NAT)
###11.2.4IPv6寻址
IPv6使用128位的地址,消除了对网络地址转换的依赖
###11.3网络接口设置
###11.3.1ifconfig命令
ifconfig [interface] [options] [address_family] [address] [/prefix_length] [dest_address] [parameters]
dc表示DEC/Intel以太网卡驱动程序
em表示Intel(R) PRO/1000千兆以太网卡驱动
sis表示SiS 900,SiS 7016以及NS DP83815/DP83816
Solaris网络接口命名规则:
<driver-name><instance-number>
options:
-a:列出所有指定类型的网络接口
-d:仅仅将ifconfig命令应用于处于禁止状态(down)的网络接口
-u: 仅仅将ifconfig命令应用于处于启用状态(up)的网络接口
address_family:地址类型
address:网络接口的网络地址
up:激活网络接口,使其处于工作状态
down:关闭网络接口,时期停止工作
delete:从接口删除指定的IP地址
detach:从网络接口列表中删除一个网络接口
netmask mask:指出子网掩码
mtu value:设置系统最大的IP包大小,value变量可以是从60~65535的任意整数值
##11.3.2列出可用的网络接口
ifcongig -a
11.3.3修改网络接口参数
ifconfig interface [up|down]
up:启用网络接口
down:禁用网络接口
设置IP地址以及子网掩码
ifconfig interface inet ipaddress netmask mask
inet:设置IPv4的IP地址,可省略
ipaddress:具体的IPv4地址
netmask:指定子网掩码
mask:子网掩码
ifconfig命令为临时配置
可更改/etc/hostname.interface和/etc/netmasks配置文件,需要重新启动
11.3.4给一个网络配置多个IP地址
ifconfig interface inet ipaddress netmask mask[add|alias]
ipaddress:要分配的IP地址
mask:子网掩码
add|alias:指定的网络接口分配别名地址
删除地址
ifconfig interface inet ipaddress delete
11.3.5配置DHCP支持
动态主机设置协议(Dynamic Host Configuration Protocol, DHCP)是一个局域网的网络协议
DHCP配置文件/etc/default/dhcpagent和etc/dhcp.interface
eg:为名称为e1000g0的网络接口配置DHCP
(1) 创建DHCP文件.
使用vi命令在/etc目录中创建一个新的文件,名称为dhcp.e1000g0,内容如下:
wait 30
(2) 初始化网络接口
ifconfig interface [inet6] dhcp start
inet6表示IPv6地址,默认表示IPv4地址
dhcp关键字表示启用DHCP客户端
start关键字表示启用并初始化改网络接口
(3) 查看网络接口的DHCP配置状态
ifconfig interface [inet6] dhcp status
status:查询指定网络接口的状态
(4) 请求租用期延长
ifconfig interface [inet6] dhcp extend
extend表示延长IP地址租用时间
(5) 释放IP地址
ifconfig interface [inet6] dhcp release
release表示释放已经分配的IP地址
(6) 删除IP地址
ifconfig interface [inet6] dhcp drop
drop表示删除已分配的IP地址
为某个网络接口配置DHCP客户端时,需要在rc.conf文件添加
ifconfig_interface=”DHCP”
11.3.6关闭或激活网络接口
关闭网络接口
ifconfig interface down
激活网络接口
ifconfig interface up
11.4路由
11.4.1路由表
一般情况下,路由表为与路由器(router)中,主机可以拥有自己的有路由表,称为主路由表
查看路由表
netstat [-r|-n]
-n:不使用主机名表示
11.4.2静态路由
手工操纵路由表,进行静态路由设置
route [options] command [[modifiers] destination gateway [netmask]]
command:
add:增加一条路由
flush:删除路由表中所有的路由信息
delete:删除某条特定的路由
change:修改某条特定的路由
get:查询并显示某个目的地的路由信息
monitor:监控路由信息
modifiers表示修饰符,指定目的地类型
-inet:将指定目的地强制解释为一个IPv4地址
-inet6:将指定目的地强制解释为一个IPv6地址
-host:将指定目的地强制解释为一个主机
-net:将指定目的地强制解释为一个网络
destination:目的地,可以是主机或者网络
gateway:数据宝贝发送到的下一个节点
netmask:子网掩码
11.4.3默认路由
默认路由是一种特殊的静态路由
添加默认路由
route add default -gateway gateway -interface
interface
default:指定添加的是默认路由
-gateway:默认路由的网关地址
-interface:默认路由的网络接口
11.5名称解析
11.5.1主机名和域名
1.主机名(hostname)
在局域网中为主机赋予的名称
主机名解析/etc/hosts
[Internet addres] [official hostname] [alias1] [alias2]
Internet address:主机的IP地址
official hostname:主机的正式名称,一般是域名
alias1|alias2:主机的别名(主机名),可以拥有多个
2.域名
由一串用圆点分隔的字符组成的Internet上某一台主机或者一组主机上的名称
11.5.2DNS客户端配置
DNS配置
/etc/resolv.conf
11.6常见问题
 
DNS服务器
12.1DNS的起源和背景
12.1.1DNS的历史
20世纪60年代,美国国防高级研究计划署(Advanced Research Projects Agency, ARPA),开始资助实验性的光与计算机网络,称为阿帕网(The Advanced Research Projects Agency NetWork, ARPANET)
20世纪80年代,TCP/IP协议成为ARPANET的标准网络协议,ARPANET成为基于TCP/IP协议的局域网和区域联合网的主干,被称为Internet
1988年,美国国家自然科学基金网络(National Science Foundation Network, NSFNET)取代阿帕网成为Internet的骨干网.1995年春天,Internet完成了由公共NSFNET作为骨干网到使用多个商业骨干网的转变
12.1.2DNS概述
www.tsinghuan.edu.cn
主机名.三级域.二级域.顶级域
12.1.3域名空间和体系结构
顶级域名:

4. 通用顶级域名

5. 基础设施顶级域名

6. 国家和地区顶级域

7. 国际化国家和地区顶级域
12.1.4域和域名
在DNS树中,域都是分支节点,而主机是叶子节点
12.1.5区域和域的不同
域:DNS树上面的一个分支节点以及所有的下面的节点
区域:把域的某个部分授权出去让别人代为管理,称为区域
12.1.6域名服务器的类型

   ```
   1.主域名服务器(Primary DNS Server)
   2.辅助域名服务器(Secondary DNS Server)
   3.高速缓存域名服务器(Cache DNS Server)
   4.转发服务器(Forwarding Server)
   ```

   12.1.7DNS基本原理

   ```
   首先,DNS系统以分布式数据库的方式提供域名解析服务.在分布式数据库中,每一条记录称为资源记录(resource record, RR)
   其次,DNS系统中的数据库采用分散式的方式来管理,没用任何一个域名服务器中的数据库会包含Internet上的所有资源记录.
   再次,同一个数据库可以由多台域名服务器来管理,查询其中任何一台域名服务器都可以得到相同的资源记录.反之,同一个域名服务器可以管理多个区域的数据库,不同的域名数据库查询都可能是由同一台域名服务器提供
   最后,将本来属于自己所管理的资源记录授予其他的域名服务器来管理,称之为授权(delegation).一经授权,上层的域名服务器都不在管理这些区域,完全依靠被授权的域名服务器来管理.
   ```

   12.2BIND及其安装方法
12.2.1关于BIND
BIND是互联网上使用最为广泛的域名服务器软件,约占90%市场
BIND(Berkeley Internet Name Domain)
1984年,柏克莱加州大学(University of California, Berkeley)计算机系统研究小组的4个研究生共同开发了UNIX系统上的第1个DNS协议
1985年,美国设备公司(Digital Equipment Corporation, DEC)的工程师Kevin Dunlap重写了这个最初的DNS实现,并正式命名为BIND
20世纪90年代,BIND被移植到Windows NT平台上.
BIND发展过程中经历了3个主要版本,分别是BIND 4,BIND 8和BIND 9,每个版本在架构上有显著变化.
BIND软件包包括:
   DNS服务器:名称为named的程序,是name daemon的缩写,主要功能是根据DNS协议标准的规定,响应收到的DNS查询
   DNS解析器:一个解析器是一个程序,通过发送请求到合适的服务器并且对服务器的响应做出合适的回应,来解析对一个域名的查询,一个解析库是程序组件的集合,可以在开发其他程序时使用,为这些程序提供域名解析的功能
   测试服务器的软件工具.例如,nslookup,dig以及host等
12.2.2以二进制软件包的方式安装Bind 9
以root身份登录,执行以下命令(Solaris)
pkg install pkg:/service/network/dns/bind
查看当前系统中安装的BIND的版本
named -v
FreeBSD命令
安装
cd /usr/ports/dns/bind98/
make && make install
查看BIND版本
named -v
12.2.3以源代码的方式安装BIND9
BIND9代码下载网址http://www.isc.org/downloads
tar zxvf bind-9.***.tar.gz
cd bind-9.***
./configure
make && make install
以源代码的方式安装BIND9需要gcc编译器
12.2.4启动和停止BIND 9
BIND 9最主要的服务进程为named
启动named服务
svcadm enable dns/serve
或者
svcadm enable dns/serve:default
停止named服务
svcadm disable dns/serve
或者
svcadm disable dns/serve:default
FreeBSD中需要先配置/etc/rc.conf文件,增加以下代码:
#add following line if not present
named_enable=”YES”
#the line below must replace the line named_program=”usr/sbin/named” if present

   # otherwise add it

   named_program=”/usr/local/sbin/named”
启动named服务进程
/etc/rc.d/named start
停止named服务进程
/etc/rc.d/named stop
12.3配置BIND 9

12.3.1BIND配置文件概述
BIND组件以及位置
组件  Solaris FreeBSD
BIND主配置文件   /etc/named.conf /etc/named/named.conf
BIND可执行文件   
/usr/sbin/named
/usr/sbin/named-check
/usr/sbin/named-checkzone
/usr/sbin/named-compilezone /usr/sbin/named
/usr/sbin/named-checkconf
/usr/sbin/named-checkzone
/usr/sbin/named-compilezone
/usr/sbin/named.reconfig
/usr/sbin/named.reload
BIND数据库文件   /var/named  /var/named/etc/namedb
默认的提示文件的名称  未指定 named.root
启动named svcadm enable dns/server
或
svcadm enable dns/server:default    
/etc/rc.d/named start
关闭named svcadm disable dns/server
或
svcadm disable dns/server:default   
/etc/rc.d/named stop
12.3.2主配置文件named.conf
    named.conf文件中的语句的基本语法
    clause [argument]{
    /*块注释*/
        item;//注释
        item;#注释
        ……
};
named.conf文件中的常用语句及其涵义
语句  涵义
acl 定义一个IP地址表列名,用于访问控制
controls    定义系统管理员使用的,有关本地域名服务器操作的控制通道
include 包含一个外部文件
key 定义密钥,应用在通过TSIG进行授权和认证的配置中
logging 设置日志服务器和日志信息的发送地
options 控制服务器的全局配置选项和为其他语句设置默认值
server  在一个单服务器基础上设置特定的配置选项
trusted-keys    定义信任的DNSSED密钥
view    定义一个视图
zone    定义一个区域
12.3.3定义地址匹配列表
    acl语句用来定义地址匹配列表
    acl acl-name{
            address_match_list
};
    acl-name:要定义的地址匹配列表的名称
    address_match_list:地址列表,可以是IP地址,也可以是用大括号括起来的另一个地址匹配列表
    由于BIND采用了顺序优先匹配算法,所以一个小的范围定义一定要在更大的范围定义之前,不管知否带有!符号.
    BIND定义了一些常,表示某个范围的主机地址
    any:匹配所有主机
    none:不匹配任何主机
    localhost:匹配主机上所有IPv4的网络接口
    localnets:匹配所有IPv4本地网络的主机
12.3.4定义控制通道
    controls语句定义了系统管理员使用的,有关本地域名服务器操作的控制通道
    control{
        inet(ipv4_address|IPv6_address|*)
        [port(integer)]
        allow{address_match_list}
        [keys{key_list}];
        ……
}
如果想禁用所有的控制通道,则:
    controls{};
12.3.5包含外部文件
    include语句可以在该语句出现的地方插入指定的文件
    include “path”
12.3.6定义共享密钥
    key语句用来定义共享密钥
    key key_id{
        algorithm hmac_md5;
        secret string;
};
    key_id:密钥的名称,在其他地方可以通过该名称来引用该密钥
    algorithm:加密算法,目前只支持hmac-md5
    secret:指定一个用base-64编码的字符串作为密钥
12.3.7定义通道
    BIND的所有的日志都会输出到一个或者多个通道中.
    channel channel_name{
            (file path_name
[version(number|unlimited)]
[size filesize]
|syslog syslog_facility
|stderr
|null);
[severity(critical|error|warning|notice|info|debug|[level]|dynamic);]
[print-category yes or no;]
[print-severity yes or no;]
[print-time yes or no;]
};
    channel_name:通道名称
    file:通道的目标为一个磁盘文件,path_name表示目标文件名
    version:指定named自动保留的多个日志文件,number用来指定版本的个数,如果指定为unlimited,则表示不限制版本个数.
    size:指定每个文件的大小,filesize可以以K,B或者G为单位.
    syslog:表示通道的目标为系统日志
    stderr:表示将通道的目标为named的标准错误输出
    null:表示无日志输出
    severity:指定记录消息的级别,主要有critical,error,warning,notice,info,debug[level]以及dynamic等7个级别.定义某个级别后,系统会定义包括该级别以及比该级别更严重的级别的消息.
12.3.8使用通道分类
    category category_name{
                channel_item;
    }
    default:默认类别,匹配所有未明确指定通道的类别,但不匹配不属于任何类别的消息
    general:包括所有未明确分类的BIND消息
    database:named内部使用的分类,用来存储域和缓存数据的内部数据库信息
    security:接受和拒绝的请求
    config:配置文件分析和处理
    resolver:域名解析,包括对来自解析器的递归查询的处理.
    xfer-in:从远程域名服务器到本地域名服务器的区域传输
    xfer-out: 从本地域名服务器到远程域名服务器的区域传输
    notify:NOTIFY协议
    client:客户端请求的处理
    unmatched:由于没有匹配的视图,那么大无法确定的类别
    network:网络操作
    update:动态更新事件
    queries:查询请求
    dispatch:DNSSEC和TSIG协议的处理
    lame_serviers:未知服务器.由于其他DNS服务器中的错误配置 引起的
12.3.9设置选项
    options{
[version version_string;]
[directory path_name;]
[pid-file path_name;]
[notify yes_or_no|explicit;]
[recursion yes_or_no;]
[forward(only|first);]
[forwards{ip_addr[port ip_port];[ip_addr[port ip_port];..]};]
[allow-notify{address_match_list};]
[allow-query{address_match_list};]
[allow-transfer{address_match_list};]
[allow-recursion{address_match_list};]
[allow-v6-synthesis{address_match_list};]
[blackhole{address_match_list};]
[listen-on[port ip_port]{address_match_list};]
[listen-on-v6[port op_port]{address_match_list};]
[query-source[address(ip_addr|*)][port(ip_port|*)];]
[port ip_port]
}

1. 通用选项
   version:响应针对BIND服务器版本的请求时的内容,缺省返回服务器的真实内容
   directory:指定BIND服务器的工作目录.配置文件中所使用的相对路径.大多数服务器的输出文件都缺省生成在这个目录下.如果没有设定目录,工作目录缺省设置为服务器启动时的目录”.”.指定的目录应该是一个绝对路径
   pid-file:指定named进程ID文件的路径名.默认为/var/run/named.pid.是给需要向运行着的服务器发送信号的程序使用的
   statistics-file:当使用rndc stats命令的时候,服务器会统计信息追加到文件路径名.默认为named.stats,位于在服务器程序的当前目录中.
   port:指定服务器用来接收和发送DNS协议数据的UDP/TCP端口号,默认为53.主要用于服务器的检测,如果不使用53端口,服务器将不能与其他的DNS进行通信
2. 布尔选项
   notify:如果为yes,则用于服务器数据发生变化后,发送给其他服务器消息,然后从服务器和主服务器协商数据库副本的更新.如果为no,则不会发出任何报文.也可以设定在zone语句中.默认值为yes.
   recursion:指定named程序是否可以代表客户机查询其他的域名服务器,这称为递归查询.默认值为yes.
把recursion设为no不会阻止用户从服务器的缓存中得到数据,仅仅阻止新数据作为查询的结果被缓存.服务器的内部操作还是可以影响本地的缓存内容.
3. 转发选项
转发功能可以用于在一些域名服务器上产生一个大的缓存,从而减少到外部服务器网络上的流量.可以用在和Internet没有直接连接的内部域名服务器上,用来提供对外部域名的查询.只有当服务器是非授权时,并且缓存中没有相关记录时才进行转发
   forward:只有当forwarders子句的列表中有内容时才有意义.可以指定first和only两个值,如果为first,则域名服务器会先查询设置的forwarders的的服务器,如果没有回答,则会自己寻找答案;如果设定为only,服务器只会把请求转发到其他服务器上.默认值为first.
   forwarders:设定转发使用的IP地址.默认列表为空,即不转发.转发也可以设置在每个域上,这样全局选项中的转发设置就不会起作用了.可以将不同的域转发到服务器上,或者对不同的域可以实现forward only或者first的不同方式,也可以根本不转发
4. 访问控制选项
根据用户请求使用的IP地址进行限制
   allow-notify:用来设定除主域名外,还可以发送通知消息的主机,通知域中的从服务器区域数据库已经发生改变.默认情况下,区域中的域名服务器只接受来自主域名服务器的通知消息.
   allow-query:设定可以进行普通查询的主机.默认允许所有主机进行查询.
   allow-transfer:设定允许和本地服务器进行区域传输的主机.默认允许所有主机进行域传输.
   allow-recursion:设定可以递归查询本域名服务器的主机.默认允许所有主机之间进行递归查询.禁止递归查询不能阻止查询已经存在于服务器缓存中的数据.
   allow-v6-synthesis:设定能接受对IPv6响应的主机
   blackhole:设定一个地址列表,服务器不会接受来自这个列表的查询请求,或者解析这些地址.默认值为none.
5. 网络接口和端口选项
使用listen-on来设定.listen-on使用可选的端口和一个地址匹配列表.服务器将会监听所有匹配地址列表中所允许的端口.如果没有端口,则使用53.
listen-on port{

   ```
       address_match_list;
   ```

   }
port:指定监听的端口
adderess_match_list:有效的地址匹配列表
6. 查询地址选项
query-source {address ip_address port port_number}
ip_address:一个IPv4的地址
port_number:端口号
query-source-v6用来处理IPv6的地址
12.3.10定义远程服务器
server ip_addr{
[bogus yes_or_no;]
[provide-ixfr yes_or_no;]
[request-ixfr yes_or_no;]
[transfers number]
[transfer-format(one-answer|many-answers);]
[keys{string;[string;[…]]};]
}
ip_addr:远程服务器地址
bogus:如果值为yes,则named不会向该服务器发送任何查询
provide-ixfr:如果值为yes,则该服务器将执行增量区域传输,如果值为no,则所有对远端服务器的传输都将是非增量的.不设定,默认为yes.
request-ixfr:本从服务器是否向主服务器发送区域的增量传输请求.默认为yes
transfers:限制了来自远端服务器的并发的入站区域传输的数量
transfer-format:指定服务器进行区域传输的方式,分别有one-answer和many-answers,前者表示每个源数据传输使用一个DNS报文,后者表示在一个报文中汇集尽可能多的记录
keys:定义key_id,用于当与远程服务器通话时的安全处理
12.3.11定义视图
view语句包含一个控制谁能看到视图的访问控制列表,一些应用到视图中所有区域的选项以及区域定义本身