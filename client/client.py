#!/usr/bin/env python3

import hashlib

# Импортируем системную библиотеку Python.
# Она используется для загрузки файла 'index.html' с сервера.
# Ничего особенного устанавливать не нужно, эта библиотека устанавливается вместе с Python.

import requests
from nanoid import generate


def get_checksum(text):
    return hashlib.md5(text.encode()).hexdigest()


#fp = urllib.request.urlopen("http://localhost:1234/")

# 'encodedContent' соответствует закодированному ответу сервера нашего файла.
# 'decodedContent' соответствует раскодированному ответу сервера (тут будет то, что мы хотим вывести на экран).
content = requests.get('http://localhost:1234/')
#encodedContent = fp.read()
#decodedContent = encodedContent.decode("utf8")

# Выводим содержимое файла, полученного с сервера ('index.html').
original_checksum = content.headers['checksum']
file_content = content.text    
if original_checksum==get_checksum(file_content):
    filename = generate()
    f = open(f'clientdata/{filename}', 'a')
    f.write(str(file_content))
    f.close()
    print(f'Success! File {filename} was created')
    print('Checksum is correct!')
    print(content)
else:
    print('Checksum is wrong!')
    