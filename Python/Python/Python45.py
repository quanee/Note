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