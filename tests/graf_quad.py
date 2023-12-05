import numpy as np
"""Álgebra linear em python"""
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)

def quadratica(x):
    return x*x

# Processamento de dados
fig, ax = plt.subplots()

#Saída de dados

ax.plot(x, quadratica(x), label='quadratic')

plt.show()


