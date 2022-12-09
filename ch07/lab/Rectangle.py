#Creates the rectangle class and sets up the variables
class Rectangle():
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h
  # returns a string contaning the init variables above
  def __str__(self):
    return "x: " + self.x + ", y: " + self.y + ", width: " + self.width + ", height: " + self.height
  