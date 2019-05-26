## IMPORTS GO HERE
from math import pi
## END OF IMPORTS


#### YOUR CODE FOR get_area GOES HERE ####
def get_area(radius):
    a = radius**2 * pi
    return a

#### End OF MARKER


#### YOUR CODE FOR output_parameter GOES HERE ####
def output_parameter(radius):
    parameter = 2 * pi * radius
    print "The parameter of the circle with radius", (radius), "is", (parameter)





if __name__ == '__main__':
    print get_area(2)
    print output_parameter(1.0)
