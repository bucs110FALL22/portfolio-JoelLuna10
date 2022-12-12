import requests
#cat api, uses this to get the cat answers
class catboyAPI:
  def __init__(self):
    #self.url = f'http://dog-api.kinduff.com/api/facts?number={number}'
    self.url = f'https://api.catboys.com/catboy'

  def get(self):
    site = requests.get(self.url)
    info = site.json()
    return info
