import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

g1 = 9.81
nu = 18.1 * 10e-6
ro = 1.2754
z_mas = [0]
x_mas = [0]
y_mas = [0]
h1 = 0.1
t = 0
x = 0
y = 0
z = 0


def f(t, x, y, z, vx1, vy, vz):
    return vx1


def g(t, x, y, z, vx, vy1, vz):
    return vy1


def h(t, x, y, z, vx, vy, vz1):
    return vz1


def j(t, x, y, z, vx1, vy1, vz1):
    return -vx1 * (6 * math.pi * nu * r) / m + 2 * s * ro * (vy1 * wz - vz1 * wy) / m


def p(t, x, y, z, vx1, vy1, vz1):
    return -vy1 * (6 * math.pi * nu * r) / m + 2 * s * ro * (vz1 * wx - vx1 * wz) / m


def b(t, x, y, z, vx1, vy1, vz1):
    return -vz1 * (6 * math.pi * nu * r) / m + 2 * s * ro * (vx1 * wy - vy1 * wx) / m - g1


def runge_kutt():
    global x, y, z, t, vx, vy, vz, h1
    while t < 100:
        t += h1
        k1 = h1 * f(t, x, y, z, vx, vy, vz)
        m1 = h1 * g(t, x, y, z, vx, vy, vz)
        r1 = h1 * h(t, x, y, z, vx, vy, vz)
        q1 = h1 * j(t, x, y, z, vx, vy, vz)
        n1 = h1 * p(t, x, y, z, vx, vy, vz)
        l1 = h1 * b(t, x, y, z, vx, vy, vz)

        k2 = h1 * f(t + h1 / 2, x+k1/2, y+m1/2, z+r1/2, vx+q1/2, vy+n1/2, vz+l1/2)
        m2 = h1 * g(t+h1/2, x+k1/2, y+m1/2, z+r1/2, vx+q1/2, vy+n1/2, vz+l1/2)
        r2 = h1 * h(t+h1/2, x+k1/2, y+m1/2, z+r1/2, vx+q1/2, vy+n1/2, vz+l1/2)
        q2 = h1 * j(t+h1/2, x+k1/2, y+m1/2, z+r1/2, vx+q1/2, vy+n1/2, vz+l1/2)
        n2 = h1 * p(t+h1/2, x+k1/2, y+m1/2, z+r1/2, vx+q1/2, vy+n1/2, vz+l1/2)
        l2 = h1 * b(t+h1/2, x+k1/2, y+m1/2, z+r1/2, vx+q1/2, vy+n1/2, vz+l1/2)

        k3 = h1 * f(t + h1 / 2, x + k2 / 2, y + m2 / 2, z + r2 / 2, vx + q2 / 2, vy + n2 / 2, vz + l2 / 2)
        m3 = h1 * g(t + h1 / 2, x + k2 / 2, y + m2 / 2, z + r2 / 2, vx + q2 / 2, vy + n2 / 2, vz + l2 / 2)
        r3 = h1 * h(t + h1 / 2, x + k2 / 2, y + m2 / 2, z + r2 / 2, vx + q2 / 2, vy + n2 / 2, vz + l2 / 2)
        q3 = h1 * j(t + h1 / 2, x + k2 / 2, y + m2 / 2, z + r2 / 2, vx + q2 / 2, vy + n2 / 2, vz + l2 / 2)
        n3 = h1 * p(t + h1 / 2, x + k2 / 2, y + m2 / 2, z + r2 / 2, vx + q2 / 2, vy + n2 / 2, vz + l2 / 2)
        l3 = h1 * b(t + h1 / 2, x + k2 / 2, y + m2 / 2, z + r2 / 2, vx + q2 / 2, vy + n2 / 2, vz + l2 / 2)

        k4 = h1 * f(t + h1, x + k3, y + m3, z + r3, vx + q3, vy + n3, vz + l3)
        m4 = h1 * g(t + h1, x + k3, y + m3, z + r3, vx + q3, vy + n3, vz + l3)
        r4 = h1 * h(t + h1, x + k3, y + m3, z + r3, vx + q3, vy + n3, vz + l3)
        q4 = h1 * j(t + h1, x + k3, y + m3, z + r3, vx + q3, vy + n3, vz + l3)
        n4 = h1 * p(t + h1, x + k3, y + m3, z + r3, vx + q3, vy + n3, vz + l3)
        l4 = h1 * b(t + h1, x + k3, y + m3, z + r3, vx + q3, vy + n3, vz + l3)

        x += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y += (m1 + 2 * m2 + 2 * m3 + m4) / 6
        z += (r1 + 2 * r2 + 2 * r3 + r4) / 6
        vx += (q1 + 2 * q2 + 2 * q3 + q4) / 6
        vy += (n1 + 2 * n2 + 2 * n3 + n4) / 6
        vz += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        x_mas.append(x)
        y_mas.append(y)
        z_mas.append(z)
        if z < 0: break

def create_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot(x_mas, y_mas, z_mas)
    plt.show()

if __name__ == "__main__":
    print('введите массу и радиус мяча')
    m, r = input().split(' ')
    m = float(m)
    r = float(r)
    print('введите начальную линейную скорость мяча')
    vx, vy, vz = input().split(' ')
    vx, vy, vz = float(vx), float(vy), float(vz)
    print('введите угловую скорость мяча')
    wx, wy, wz  = input().split(' ')
    wx, wy, wz = float(wx), float(wy), float(wz)
    s = math.pi * r * r
    runge_kutt()
    create_plot()
    print(z_mas)
