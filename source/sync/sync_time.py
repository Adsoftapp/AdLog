#Author: Ad_closeNN
#Create by: Ad_closeNN
#Create time: 2024/5
#Powered by Python 3.12.2
#Build by Microsoft Visual Studio Code
#IDE version: Microsoft Visual Studio Code 1.83.1 (32-bit) (user setup)
#Encoding with: UTF-8

import ntplib
from datetime import datetime

def get_ntp_time(server="time.windows.com"): #使用 Microsoft 给予的 NTP 时钟服务器来同步时间，确保时间准确无误
    try:
        client = ntplib.NTPClient()
        response = client.request(server, version=3)
        ntp_time = datetime.fromtimestamp(response.tx_time)
        return ntp_time
    except Exception as e:
        print("Error:", e)
        return None

def custom_time_format(time_obj):
    formatted_time = time_obj.strftime("%Y/%m/%d %H:%M:%S")  # 自定义时间格式
    return formatted_time

def get_time():
    global get_ntp_time
    global custom_time_format
    global ntp_time
    ntp_time = get_ntp_time()
    if ntp_time:
        print("[time.windows.com] 上的时间:", custom_time_format(ntp_time))
    else:
        print("无法同步NTP服务器[time.windows.com]的时钟。正在尝试获取另一个NTP服务器[pool.ntp.org]的时钟。")

        sync_server2 = "pool.ntp.org" #全球志愿者打造的公共NTP时间池
        def get_ntp_time(server=sync_server2): #使用 Microsoft 给予的 NTP 时钟服务器来同步时间，确保时间准确无误
            try:
                client = ntplib.NTPClient()
                response = client.request(server, version=3)
                ntp_time = datetime.fromtimestamp(response.tx_time)
                return ntp_time
            except Exception as e:
                print("Error:", e)
                return None
        def custom_time_format(time_obj):
            formatted_time = time_obj.strftime("%Y/%m/%d %H:%M:%S")  # 自定义时间格式
            return formatted_time
        if ntp_time:
            print("[pool.ntp.org] 上的时间:", custom_time_format(ntp_time))
        else:
            print("无法同步NTP服务器[pool.ntp.org]的时钟。正在尝试获取另一个NTP服务器[time.apple.com]的时钟。")

            sync_server3 = "time.apple.com" #Apple Inc.苹果公司打造的公共NTP时间池
            def get_ntp_time(server=sync_server3): #使用Apple Inc.苹果公司给予的 NTP 时钟服务器来同步时间，确保时间准确无误
                try:
                    client = ntplib.NTPClient()
                    response = client.request(server, version=3)
                    ntp_time = datetime.fromtimestamp(response.tx_time)
                    return ntp_time
                except Exception as e:
                    print("Error:", e)
                    return None
            def custom_time_format(time_obj):
                formatted_time = time_obj.strftime("%Y/%m/%d %H:%M:%S")  # 自定义时间格式
                return formatted_time
            if ntp_time:
                print("[time.apple.com] 上的时间:", custom_time_format(ntp_time))
            else:
                print("无法同步NTP服务器[time.apple.com]的时钟。正在尝试获取另一个NTP服务器[time.nist.gov]的时钟。")

                sync_server4 = "time.nist.gov" #美国国家标准与技术研究所（NIST）打造的公共NTP时间池
                def get_ntp_time(server=sync_server4): #使用美国国家标准与技术研究所（NIST）给予的 NTP 时钟服务器来同步时间，确保时间准确无误
                    try:
                        client = ntplib.NTPClient()
                        response = client.request(server, version=3)
                        ntp_time = datetime.fromtimestamp(response.tx_time)
                        return ntp_time
                    except Exception as e:
                        print("Error:", e)
                        return None
                def custom_time_format(time_obj):
                    formatted_time = time_obj.strftime("%Y/%m/%d %H:%M:%S")  # 自定义时间格式
                    return formatted_time
                if ntp_time:
                    print("[time.nist.gov] 上的时间:", custom_time_format(ntp_time))
                else:
                    print("无法同步NTP服务器[time.nist.gov]的时钟。正在尝试获取另一个NTP服务器[time.amazon.com]的时钟。")

                    sync_server5 = "time.amazon.com" #亚马逊打造的公共NTP时间池
                    def get_ntp_time(server=sync_server5): #使用亚马逊给予的 NTP 时钟服务器来同步时间，确保时间准确无误
                        try:
                            client = ntplib.NTPClient()
                            response = client.request(server, version=3)
                            ntp_time = datetime.fromtimestamp(response.tx_time)
                            return ntp_time
                        except Exception as e:
                            print("Error:", e)
                            return None
                    def custom_time_format(time_obj):
                        formatted_time = time_obj.strftime("%Y/%m/%d %H:%M:%S")  # 自定义时间格式
                        return formatted_time
                    if ntp_time:
                        print("[time.amazon.com] 上的时间:", custom_time_format(ntp_time))
                    else:
                        print("无法同步NTP服务器[time.amazon.com]的时钟。正在尝试获取本地时钟。")

                        from datetime import datetime
                        local_time = datetime.now() #直接使用本地时间
                        formatted_time = local_time.strftime("%Y/%m/%d %H:%M:%S")  # 自定义时间格式
                        print("[本地] 上的时间:", formatted_time)
    return custom_time_format(ntp_time)

now_time_is = get_time()