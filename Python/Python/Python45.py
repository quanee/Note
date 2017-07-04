import jinja2
'''jinja2语法'''


# 基本语法
{# This is jinja code
    # 控制结构
    {% for file in filenames %}
        # 取值
        {{ file }}
    {% endfor %}
#}

# jinja2变量
# jinja2支持python中所有的Python数据类型比如列表、字段、对象等。
<p>this is a dicectory:{{ mydict['key'] }} </p>
<p>this is a list:{{ mylist[3] }} </p>
<p>this is a object:{{ myobject.something() }} </p>

# jinja2中的过滤器
# 过滤器名称           说明    
#     safe         渲染时值不转义
#   capitialize    把值的首字母转换成大写，其他子母转换为小写
#     lower        把值转换成小写形式 
#     upper        把值转换成大写形式 
#     title        把值中每个单词的首字母都转换成大写
#     trim         把值的首尾空格去掉
#    striptags     渲染之前把值中所有的HTML标签都删掉
#     join         拼接多个值为字符串
#     replace      替换字符串的值
#     round        默认对数字进行四舍五入，也可以用参数进行控制
#     int          把值转换成整型

{{ 'abc' | captialize  }}
# Abc
 
{{ 'abc' | upper  }}
# ABC
 
{{ 'hello world' | title  }}
# Hello World
 
{{ "hello world" | replace('world','daxin') | upper }}
# HELLO DAXIN
 
{{ 18.18 | round | int }}
# 18

# jinja2的控制结构
# jinja2中的if语句类似与Python的if语句，它也具有单分支，多分支等多种结构，不同的是，条件语句不需要使用冒号结尾，而结束控制语句，需要使用endif关键字。
{% if daxin.safe %}
daxin is safe.
{% elif daxin.dead %}
daxin is dead
{% else %}
daxin is okay
{% endif %}

# jinja2的for循环
# 迭代列表
<ul>
{% for user in users %}
<li>{{ user.username|title }}</li>
{% endfor %}
</ul>

# 迭代字典
<dl>
{% for key, value in my_dict.iteritems() %}
<dt>{{ key }}</dt>
<dd>{{ value}}</dd>
{% endfor %}
</dl>

# 变量              描述
# loop.index        当前迭代的索引（从1开始）
# loop.index0       当前迭代的索引（从0开始）
# loop.first        是否是第一次迭代，返回bool
# loop.last         是否是最后一次迭代，返回bool
# loop.length       序列中的项目数量
# loop.revindex     到循环结束的次数（从1开始）
# loop.revindex0    到循环结束的次数(从0开始）


# jinja2的宏
# 宏类似于Python中的函数，我们在宏中定义行为，还可以进行传递参数，就像Python中的函数一样一样儿的。
# 在宏中定义一个宏的关键字是macro，后面跟其 宏的名称和参数等
{% macro input(name,age=18) %}   # 参数age的默认值为18
    <input type='text' name="{{ name }}" value="{{ age }}" >
{% endmacro %}

# 调用方法也和Python的类似
<p>{{ input('daxin') }} </p>
<p>{{ input('daxin',age=20) }} </p>

# jinja2的继承和Super函数
# jinja2中最强大的部分就是模板继承。模板继承允许我们创建一个基本(骨架)文件，其他文件从该骨架文件继承，然后针对自己需要的地方进行修改。
# jinja2的骨架文件中，利用block关键字表示其包涵的内容可以进行修改。
# 以下面的骨架文件base.html为例：
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
    <link rel="stylesheet" href="style.css"/>
    <title>{% block title %}{% endblock %} - My Webpage</title>
    {% endblock %}
</head>
<body>
<div id="content">{% block content %}{% endblock %}</div>
<div id="footer">
    {% block  footer %}
    <script>This is javascript code </script>
    {% endblock %}
</div>
</body>
</html>
# 这里定义了四处 block，即：head，title，content，footer。那怎么进行继承和变量替换呢？注意看下面的文件
{% extend "base.html" %}       # 继承base.html文件
 
{% block title %} Dachenzi {% endblock %}   # 定制title部分的内容
 
{% block head %}
    {{  super()  }}        # 用于获取原有的信息
    <style type='text/css'>
    .important { color: #FFFFFF }
    </style>
{% endblock %}   
 
# 其他不修改的原封不同的继承



# 利用jinja2进行渲染
# jinja2模块中有一个名为Enviroment的类，这个类的实例用于存储配置和全局对象，然后从文件系统或其他位置中加载模板。

# 基本使用方法
# 　　大多数应用都在初始化的时候撞见一个Environment对象，并用它加载模板。Environment支持两种加载方式：

# PackageLoader：包加载器
# FileSystemLoader：文件系统加载器
# PackageLoader
#     使用包加载器来加载文档的最简单的方式如下：
from jinja2 import PackageLoader,Environment
env = Environment(loader=PackageLoader('python_project','templates'))    # 创建一个包加载器对象
 
template = env.get_template('bast.html')    # 获取一个模板文件
template.render(name='daxin',age=18)   # 渲染
# 其中：
# PackageLoader()的两个参数为：python包的名称，以及模板目录名称。
# get_template()：获取模板目录下的某个具体文件。