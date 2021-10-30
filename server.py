import os
from flask import Flask,send_file
from nanoid import generate
import hashlib
KB = 1024
def save_generated_str():
    data = generate(size=KB)
    filename = generate()
    print(os.getcwd())
    full_path = f'serverdata/{filename}'

    f = open(full_path, 'a')
    f.write(data)
    f.close()
    return full_path

def get_checksum(filename):
    return hashlib.md5(filename).hexdigest()
app = Flask(__name__)

@app.route('/')
def index():
    file_path = save_generated_str()
    checksum = get_checksum(open(file_path, 'rb').read())
    response = send_file(file_path)
    response.headers['checksum'] = checksum
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234, debug=True)
