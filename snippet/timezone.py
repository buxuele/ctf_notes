# when: 2019/03/22 10:11 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. figure out what your local timezone is

"""

from tzlocal import get_localzone

tz = get_localzone()
print(tz)   # Asia/Shanghai
