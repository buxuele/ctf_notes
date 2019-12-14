import timy
import requests

# pip3 install timy


@timy.timer(ident="net_speed", loops=5)     # run this func 5 times
def net_ok():
    resp = requests.get("https://www.baidu.com")
    print(resp.status_code)


if __name__ == '__main__':
    net_ok()
