'''
configparser 配置模块
re模块
'''



import configparser
# configparser 配置模块


config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

with open('example.ini', 'w') as configfile:
    config.write(configfile)

config.read('example.ini')
print(config.sections())
print(config.defaults())

print('bitbucket.org' in config)
print('bitbucket.com' in config)

print(config['bitbucket.org']['User'])

for key in config['bitbucket.org']:
    print(key)
# 删除节点
config.remove_section('topsecret.server.com')
# 修改值
config.set('bitbucket.org', 'user', 'moon')
# 删除键值对
config.remove_option('DEFAULT', 'compression')
# 判断键
print(config.has_section('topsecret.server.com'))
# 增加节点
config.add_section('topsecret.server.com')
# 写入
config.write(open('example.ini', 'w'))


import re
# re模块 正则表达式 匹配字符串
'''
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c


'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
'\s'    匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'

'(?P<name>...)' 分组匹配 re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city") 结果{'province': '3714', 'city': '81', 'birthday': '1993'}
'''

# 元字符 . ^ $ * + ? { } [ ] | ( ) \

# re.match 从头开始匹配 返回对象
ret = re.match('hello', 'hellosdf')
print(ret.group())

# re.search 匹配包含 返回对象
ret = re.search('hello', 'fsdfhelloshellodf')
print(ret.group())
# ret.span 返回匹配字符串的起始结束位置
print('span:', ret.span())

# re.findall 把所有匹配到的字符放到以列表中的元素返回
# 返回分组中组的内容
ret = re.findall('\w(hello)', 'dghahellonbossahellodsf')  # 完全匹配
print(ret)
# 返回匹配的全部内容
ret = re.findall('\w(?:hello)', 'dghahellonbossahellodsf')  # 完全匹配
print(ret)

# re.split 以匹配到的字符当做列表分隔符
ret = re.split('s', 'abcsdefsghi')  # 完全匹配
print(ret)

# re.sub  匹配字符并替换
ret = re.sub('s', 'x', 'moonboss', 1)
print(ret)
# re.sub  匹配字符并替换 并返回替換次
ret = re.subn('s', 'x', 'moonboss', 1)
print(ret)