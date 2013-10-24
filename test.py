class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg
  def displayCar(self):
        print "This is a " + color + " " + model + " with " + str(mpg) + " MPG."

myCar = Car("DeLorean", "silver", 88)
print myCar.displayCar()
