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