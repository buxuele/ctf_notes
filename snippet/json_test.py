import json

# basic usage of json
"""
see:
    https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file

1.  json, dump() dumps():
with an s take string parameters. The others take file streams.

with open('filename.txt', 'r') as handle:
    parsed = json.load(handle)
"""

json_file = '["foo", {"bar":["baz", null, 1.0, 2]}]'    # <class 'str'>
python_obj = json.loads(json_file)  # <class 'list'>

"""后面这2个参数最好是固定写法, 比较好看一些"""
print(json.dumps(python_obj, indent=4, sort_keys=True))
