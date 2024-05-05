#Author: Ad_closeNN
#Create by: Ad_closeNN
#Create time: 2024/5
#Powered by Python 3.12.2
#Build by Microsoft Visual Studio Code
#IDE version: Microsoft Visual Studio Code 1.83.1 (32-bit) (user setup)
#Encoding with: UTF-8

import source.adlogging.time_on
import source.adlogging.time_off
import source.sync.sync_time
import os

if not os.path.exists('AdLog'):
    os.makedirs('AdLog')
    create_rootdir_path = open('AdLog//log.log', 'w')
    create_rootdir_path.write("")
    create_rootdir_path.close()
    exec(open("AdLog.py", encoding="utf-8").read())
if os.path.exists('AdLog'):
    if not os.path.isfile('AdLog//log.log'):
        def clog():
            clog = open('AdLog//log.log', 'w')
            clog.write("")
            clog.close()
        clog()
os.system('cls')
print('欢迎使用 AdLog 应用程序！本程序由 Adsoftapp 打造而成。')
print('现在的时间是: ', source.sync.sync_time.now_time_is)
now_time = source.sync.sync_time.now_time_is
while True:
    Logs = input('请在此处填写日志: ')
    time_on_off = input('是否追加时间（是/否）：')
    if  time_on_off == '是':
        log_time = now_time
        source.adlogging.time_on.adlogging(log_time, Logs)
    if time_on_off == '':
        log_time = now_time
        source.adlogging.time_on.adlogging(log_time, Logs)
    else:
        source.adlogging.time_off.adlogging(Logs)
    os.system('cls')
