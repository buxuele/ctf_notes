#!/usr/bin/python3
# Time: 2019/07/10 6:22 PM
# About: 

from geopy.geocoders import DataBC

"""
pip3 install geopy
test geo:
1. 可用的API: DataBC

"""

g = DataBC(user_agent="aaaaa")
location = g.geocode('175 5th Avenue NYC')
print(location.address)

print(location.latitude, location.longitude)
print(location.raw)

print(dir(location))































