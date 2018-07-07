

py = '''print("aaa")'''

with open('rl.py', 'w') as f:
    f.write(py)
    f.flush()
    f.close()


import rl


py = '''print("bbb")'''
with open('rl.py', 'a') as f:
    f.write(py)
    f.flush()
    f.close()

from imp import reload

reload(rl)