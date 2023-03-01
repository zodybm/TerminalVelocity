import math
import random

def func(density, coef, area, mass) :
    gravity = 9.8
    return math.sqrt((2*mass*gravity)/(density*coef*area))

def main() :
    density = 0.075
    coef = 0.5
    area = 1.9
    mass = 80
    velocity = func(density, coef, area, mass)
    count = 1
    for i in range(1,100000) :
        tempDensity = random.random() + density
        velocity += func(tempDensity, coef, area, mass)
        i += 1
        count += 1
    velocity /= count
    print(velocity)

main()