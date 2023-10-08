#Biblioteca para graficos

import matplotlib.pyplot as plt

x = list(range(1, 7))
y = [3, 5, 6, 2, 3, 0]

plt.plot(x, y, marker ='o')
plt.title('Grafico de las notas matematicas')
plt.xlabel('Pruebas')
plt.ylabel('Notas')
plt.show()