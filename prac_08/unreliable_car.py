from car import Car
import random

class UnreliableCar(Car):

    def __init__(self,name,fuel,reliability):
        super.__init__(name,fuel)
        self.reliability = reliability

    def drive(self,distance):
        rand_number = random.randint(0,100)
        if rand_number >= self.reliability:
            distance = 0
        drive_distance = super().drive(distance)
        return drive_distance

