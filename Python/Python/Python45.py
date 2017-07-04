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