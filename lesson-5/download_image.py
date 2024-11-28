import requests

img_address = "https://i0.wp.com/picjumbo.com/wp-content/uploads/beautiful-nature-mountain-scenery-with-flowers-free-photo.jpg?w=2210&quality=70"

res = requests.get(img_address)

with open('nature.png', 'wb') as f:
    f.write(res.content)
    print('Done')

