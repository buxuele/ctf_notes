# date: 2019/03/21 7:54 PM
# author: fanchuang
# github: https://github.com/buxuele/
# email: baogebuxuele@163.com
"""about:
1. 

"""

import uuid


def get_uuid():
    # pure-string, length=32
    return ''.join(str(uuid.uuid1()).split('-'))


x = get_uuid()
print(x)



