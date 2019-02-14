height = float(raw_input("Height in meters: "))

m3 = float(1000)
grav = float(9.81)

def calcPressure(h, s, g):
    pressure = h * s * g
    bar = pressure / 100000
    print("%s bar") % bar

calcPressure(height, m3, grav)

raw_input()
