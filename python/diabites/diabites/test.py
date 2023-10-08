import os

file_path = 'static/background images/Screenshot(2).png'

if os.path.isfile(file_path):
    print('File exists')
else:
    print('File does not exist')