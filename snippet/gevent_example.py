from gevent import monkey
monkey.patch_all()

import os
import time
import requests
import gevent
from gevent import pool


# https://dadi-bo.com/20190130/0jRvPCfk/800kb/hls/KTVIA8392184.ts
def gen():
    us = []
    for i in open('index.m3u8'):
        if i[0] != "#":
            url = 'https://dadi-bo.com' + i.strip()
            # yield url
            us.append(url)
    return us
    # print(url)


def download(url):
    s = requests.Session()
    cont = s.get(url).content
    fn = url.split('/')[-1]
    with open(fn, 'wb') as f:
        f.write(cont)


def get_mp4():
    # os.system('cat *.ts > all.ts')
    # os.system('ffmpeg -i all.ts -acodec copy -vcodec copy j2.mp4')
    os.system("ffmpeg -allowed_extensions ALL -i index.m3u8 -c copy j2.mp4")
    os.system('rm *.ts')
    os.system('ls -a')


def main():
    t1 = time.time()
    print("start: ", t1)
    urls = gen()
    poo = pool.Pool(30)
    jobs = []
    for u in urls:
        jobs.append(poo.spawn(download, u))
    gevent.joinall(jobs)

    t2 = time.time()
    print("cost time: ", t2 - t1)


if __name__ == '__main__':
    main()
    print("Done! Convert to mp4 now ?")
    answer = input("Type 'y' to do it: ")
    if answer == "y":
        get_mp4()



    '''
    option 1 (no-key is needed):
        cat *.ts > all.ts   
        ffmpeg -i all.ts -acodec copy -vcodec copy  a.mp4
    
    option 2(need key):
        1. change *.m3u8: 
            #EXT-X-KEY:METHOD=AES-128,URI=key.key !!! no-quote-marks
        2. run : 
            # ffmpeg -allowed_extensions ALL -i index.m3u8 -c copy j2.mp4
    
    option 3(not sure about this):
        ffmpeg -i index.m3u8 -c copy rename_me.mp4
    '''


