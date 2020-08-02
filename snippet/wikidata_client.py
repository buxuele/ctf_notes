"""about:
1. a library for wikidata api
    https://github.com/dahlia/wikidata
2. pip3 install Wikidata

2020/5/25  运行一下，长时间没反应，可能是网络被封锁，或者是这个库有点老了
"""


import webbrowser
from wikidata.client import Client

c = Client()

# 一个词条
item = c.get("Q20145", load=True)
print(item)
print(item.description)

# 一个图片
img_prop = c.get("P18")
img = item[img_prop]
print(img)
print(img.image_resolution)
print(img.image_url)
webbrowser.open_new(img.image_url)

