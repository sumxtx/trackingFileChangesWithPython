#read a file, read the contents of a file and passes those contents to the hash object

import hashlib

filename = './fileChecksumGen.py'
hasher = hashlib.md5()
with open(filename,'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
print(hasher)

#modified
