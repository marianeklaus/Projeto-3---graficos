# Getting Started Matplotluib

# Atribuição de variáveis

import numpy as np
"""Álgebra linear em python"""
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2, 2*np.pi, 200)
y = np.sin(x)

# Processamento de dados
fig, ax = plt.subplots()

#Saída de dados

ax.plot(x,y)

plt.show()