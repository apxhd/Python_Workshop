from math import pi

def circle(r=0.0):
    return (pi*r**2)


area = circle(2.5)
if area > 20:
    print("Greater than 20")
elif area < 20:
    print("Less than 20")
else:
    print("Equal to 20")
