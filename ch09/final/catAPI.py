import requests
#cat api, uses this to get the cat info
class catAPI:
  def __init__(self, number):
    self.url = f'https://meowfacts.herokuapp.com/?count={number}'

  def get(self):
    site = requests.get(self.url)
    info = site.json()
    return info


    