import requests
#catboy api, uses this to get random generated text from catboy
class catboyAPI:
  def __init__(self):
    self.url = f'https://api.catboys.com/catboy'

  def get(self):
    site = requests.get(self.url)
    info = site.json()
    return info
