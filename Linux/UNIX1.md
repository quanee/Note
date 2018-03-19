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