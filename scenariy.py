# Эта программа/скрипт запускает браузер с
# адресом yoytube.com, после чего автоматическм
# через 5 сек. запускает указанную в скрипте
# программу (блокнот) на ПК.

import os
import time

os.system('start ' + 'https://www.youtube.com/')
time.sleep(5)
os.startfile('C:/Windows/system32/notepad.exe')
