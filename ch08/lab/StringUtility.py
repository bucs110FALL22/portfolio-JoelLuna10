maxVowels = 5

class StringUtility():
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    self.count = 0
    for i in self.string:
      if i in "aeiouAEIOU":
        self.count += 1
    if self.count >= maxVowels:
      return "many"

  def bothEnds(self):
    if len(self.string) > 2:
      return self.string[0:2] + self.string[-2]
    else:
      return ""
    
  def fixStart(self):
    self.string[0] = ""
    if len(self.string) <= 1:
      return self.string
    else:
      return "" + self.string[1:].replace("","*")

  def asciiSum(self):
    self.sum = 0
    for i in self.string:
      self.sum += ord(i)
    return self.sum

  def cipher(self):
    self.encodedString =  ""
    for i in self.string:
      if i.isalpha() and i.isupper():
        if ord(i) + len(self.string) < 122:
          self.encodedString += chr(ord(words) + len(self.string) -26)
      if i.isalpha() and i.islower():
        if ord(i) + len(self.string) < 122:
          self.encodedString += chr(ord(i) + len(self.string) -26)
      else: 
        self.encodedString +=i

    return self.encodedString
      
    
  
    