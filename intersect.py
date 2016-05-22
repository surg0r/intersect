# code to model two intersecting spheres and generate sphere segment volumes to allow a ratio of working volume to
# collision volume to be generated

__author__ = 'pete'

from math import pi, sqrt
import matplotlib.pyplot as plt

def schord_a(r, d):
    return 'chord a', sqrt(), 'radius', r, 'distance between trocars', d
    #return 2*(sqrt(((r*r) - (d/2*d/2)) ))


#cap height calculation, taking r and d
def cap_h(r,d):
    print 'cap h', (r-(0.5*d)), 'd',  d
    return (r-(0.5*d))
#cap radius generator taking cap height and circle radius as arguments
def schord_a(r, h):
    return sqrt((h*(2*r-h)))

#spherical cap volume
def scv_no_h(r,d):
    if d < 2*r or d > 0:
     v = (pi/(12*d))*(r+r-d)*(r+r-d)*( ((d*d)+(2*d*(r+r))-3*(r-r)*(r-r)))
     return v
    else:
     return

def scv_wolfram(r,d):
    if d<2*r or d > 0:

     v = pi/12*((4*r)+d)*(((2*r)-d)*((2*r)-d))
     return v
    else:
     return

#spherical cap volume taking circle radius and cap height as arguments
def scv_h(r,h):
    v = ((pi * h * h) / 3) * (3*r - h)
    s = volume_of_sphere(r)
    i = ((s-v)/s)*100
    print ' intersection volume:', v,'sphere volume',s, 'radius:', r, 'height: ', h, 'spherical cap radius', schord_a(r,h), 'intersection : working %', i
    #return v
    return v


def volume_of_sphere(r):
    return pi*r*r*r*4/3

def collision_vs_work_wolfram(r,d1,d2):

    sph = volume_of_sphere(r)
    y = []
    x = []
    fraction = []

    for d in range(d1,d2):
     x.append(d)
     y.append(scv_wolfram(r,d))
     fraction.append(((scv_wolfram(r,d))/sph)*100)

    return x, y, fraction


def collision_vs_work(r,d1,d2):

    sph = volume_of_sphere(r)
    y = []
    x = []
    fraction = []

    for d in range(d1,d2):
     x.append(d)
     y.append(scv_no_h(r,d))
     fraction.append(((scv_no_h(r,d))/sph)*100)

    return x, y, fraction


def work_vs_collision(r,d1,d2):

    sph = volume_of_sphere(r)
    y = []
    x = []
    fraction = []

    for d in range(d1,d2):
     x.append(d)
     y.append(scv_no_h(r,d))

     working_volume = sph-scv_no_h(r,d)
     working_fraction = (working_volume/sph)*100
     fraction.append(working_fraction)

    return x, y, fraction

def show_graph(x,y,xlabel,ylabel):
    plt.plot(x,y)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    return

