import catAPI
import catboyAPI

def main():
  #Proxy Class
    AskUser = str(input("Type cat to learn random facts about cats or type catboy to see what catboy will say: "))
    if AskUser == 'cat':
      number = input("Type in any number to learn any random facts about cats: ")
      capi = catAPI.catAPI(number)
      results = capi.get()
      print(results)
    elif AskUser == 'catboy':
      catbapi = catboyAPI.catboyAPI()
      results = catbapi.get()
      print(results)
    else:
      None

main()
