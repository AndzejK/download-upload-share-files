#https://dev.filestack.com
from mega import Mega
import requests
from filestack import Client

api_key='###'

client=Client(api_key)
new_link=client.upload(filepath='randomFile.txt')

print(new_link.url)
  

  