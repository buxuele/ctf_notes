import requests

"""
get random images for test:
"""

def get_image():
    query = {'page': "10", 'count': "20"}
    url = 'https://api.apiopen.top/getImages'
    resp = requests.get(url, params=query)

    # print(resp.text)
    python_obj = resp.json()      # type(python_obj): dict
    # print(python_obj)

    imgs = python_obj["result"]     # sum = 5
    for i in imgs:
        print(i["img"])


if __name__ == '__main__':
    get_image()

