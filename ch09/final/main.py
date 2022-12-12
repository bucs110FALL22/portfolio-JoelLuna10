import catAPI
import catboyAPI

def main():
  #Proxy Class
    #Ask user to type cat or catboy
    AskUser = str(input("Type cat to learn random facts about cats or type catboy to see what catboy will say: "))
    #if cat is type the programm will ask the user to type any number, which chooses a fact based on the number picked
    if AskUser == 'cat':
      number = input("Type in any number to learn any random facts about cats: ")
      capi = catAPI.catAPI(number)
      results = capi.get()
      print(results)
    #if catboy is type the programm will print out a random generated text from catboy
    elif AskUser == 'catboy':
      catbapi = catboyAPI.catboyAPI()
      results = catbapi.get()
      print(results)
    #if neither cat anf catboy are typed then it returns nothing
    else:
      None

main()
