import math
import matplotlib.pyplot as plt
f = lambda x, y: ((-1) ** (0 + 3 + 1)) * 0.9 * y + 0.9 * x ** 2 + 1.9
g = lambda x: (3587 * math.e ** ((9 * x) / 10) - 567 * x ** 2 - 1260 * x - 2858) / 729
h = 0.2
x0 = [0]
n = int((2 - 0) / h)
y = [1]
yt = []
r1 = []
r2 = []
r3 = []
r4 = []
ost = []
for i in range(1, n + 1):
    x0.append(h * i)
    r1.append(h * f(x0[i - 1], y[i - 1]))
    r2.append(h * f(x0[i - 1] + (h / 2), y[i - 1] + (r1[i - 1] / 2)))
    r3.append(h * f(x0[i - 1] + (h / 2), y[i - 1] + (r2[i - 1] / 2)))
    r4.append(h * f(x0[i - 1] + h, y[i - 1] + r3[i - 1]))
    y.append(y[i - 1] + ((r1[i - 1] + 2 * r2[i - 1] + 2 * r3[i - 1] + r4[i - 1]) / 6))
    yt.append(g(x0[i - 1]))
    ost.append(abs(y[i - 1] - yt[i - 1]))
yt.append(g(x0[n]))
print('x0 = ',', '.join(list(map(str, x0))))
print('y = ', ' '.join(list(map(str, y))))
print('yt = ', ' '.join(list(map(str, yt))))
print('Погрешность =', ' '.join(list(map(str, ost))))
plt.plot(x0, y)
plt.plot(x0, yt)
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 2)
plt.show()