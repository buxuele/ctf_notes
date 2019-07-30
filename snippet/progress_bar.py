#!/usr/bin/python3
# Time: 2019/07/06 10:08 PM
# About: 

import string
import time
from tqdm import tqdm

""" fun, cool """


bar = tqdm(list(string.ascii_lowercase))
for l in bar:
    bar.set_description(f"Processing {l}...")
    time.sleep(0.09)






