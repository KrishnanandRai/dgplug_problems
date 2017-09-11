import requests

def get_image(url):
    ext = ['.jpg', '.png', '.svg']
    if url.endswith(tuple(ext)):
        img = requests.get(url)
        with open('image', 'wb') as photo:
            photo.write(img.content)

get_image('https://dgplug.org/assets/img/header.png')
