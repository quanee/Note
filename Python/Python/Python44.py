import string
'''string摸板'''

a = string.Template('$who is $role')
print(a.substitute(who='ee', role='linux'))
