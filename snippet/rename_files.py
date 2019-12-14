import os
import glob

'''
# rename a single file,just like this:

import os
os.rename('a.py', 'b.py')
'''


# rename a lot of files:
n = 0
for f in glob.glob("*.py"):
    # print(f)
    # print(type(f))

    filename = os.path.splitext(f)[0]
    extension = os.path.splitext(f)[1]

    newname = str(n) + "_" + filename + extension
    n += 1

    try:
        os.rename(f, newname)
    except OSError as e:
        print(e)
    else:
        print(f"Rename {f} to:   {newname} \t")

