#Author: Ad_closeNN
#Create by: Ad_closeNN
#Create time: 2024/5
#Powered by Python 3.12.2
#Build by Microsoft Visual Studio Code
#IDE version: Microsoft Visual Studio Code 1.83.1 (32-bit) (user setup)
#Encoding with: UTF-8

def adlogging(log_time, Logs):
    with open('AdLog//Log.log', 'a', encoding="utf-8")as log:
        log.write(str(f'[{log_time}] {Logs}\n'))