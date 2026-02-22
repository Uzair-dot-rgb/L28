class vehicle:
    def __init__(self, max_milage, speed):
        self.max_milage = max_milage
        self.speed = speed
model1 = vehicle(100,200)
print("The max milage of the vehicle is", model1.max_milage)
print("The speed of this vehicle is", model1.speed)
model2 = vehicle(200,300)
print("The max milage of this model is", model2.max_milage)
print("The speed of this model is", model2.speed)
