from Rectangle import Rectangle
#Creates a surface class to show the reactangle class
class Surface():
  def __init__(self, filename, x, y, w, h):
    self.rect = Rectangle(x,y,w,h)
    self.image = filename
  #A method that returns the initialized varibale self.rect to main.py
  def getRect(self):
    return self.rect
  