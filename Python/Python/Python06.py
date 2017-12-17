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
