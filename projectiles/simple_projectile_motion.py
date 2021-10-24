import vpython as vp
from math import sin, cos, pi, sqrt

vp.scene.height = 600
vp.scene.width = 1100

def get_time(a, b, c):
    s1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    s2 = (-b-sqrt(b**2-4*a*c))/(2*a)
    return max(s1, s2)

def get_height_change(time, initial_velocity, gravity):
    delta_y = initial_velocity*time+0.5*gravity*(time**2)
    return delta_y

x0 = 0
y0 = 50
obj = vp.box(pos=vp.vector(x0, y0, 0), size=vp.vector(1, 1, 1), color=vp.color.red, make_trail=True)

launch_angle = pi/4
frequency = 1000
velocity = 20 # 20 m/s


t = 0
dt = 1/frequency
g = -9.81

vx = cos(launch_angle)*velocity
vy = sin(launch_angle)*velocity
max_t = get_time(0.5*g, vy, y0)
y = y0
x= x0

while t < max_t:
    vp.rate(frequency)
    x=vx*t
    y = y0+get_height_change(time=t, initial_velocity=vy, gravity=g)
    obj.pos = vp.vector(x, y, 0)
    t+=dt
