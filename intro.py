import requests
url='https://s1.qwant.com/thumbr/0x380/1/6/dcb8f55c4971c243a7d5c89c80f0c38905a686551431a6b5e1d1e7a048d8d4/pexels-photo-443446.jpeg?u=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F443446%2Fpexels-photo-443446.jpeg%3Fcs%3Dsrgb%26dl%3Ddaylight-forest-glossy-443446.jpg%26fm%3Djpg&q=0&b=1&p=0&a=0'
req=requests.get(url)
print(req.content)
with open('img1.jpg','wb') as img: # writing binary values
    img.write(req.content)