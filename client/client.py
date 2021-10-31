#!/usr/bin/env python3

import hashlib

import requests
from nanoid import generate


def get_checksum(text):
    return hashlib.md5(text.encode()).hexdigest()

content = requests.get('http://server:1234/')
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
    