import matplotlib.pyplot as plt
# Cero Gráfica
ID11 = [0.000002, 0.4, 1.5, 2.7, 3.9]
ID21 = [0.0001, 0.1, 0.4, 0.9, 1.6]

VGS = [2, 2.1, 2.2, 2.3, 2.4]

plt.plot(VGS, ID21, 'o-', label='V_DS = 10V', color="red")


plt.xlabel('V_GS (V)')
plt.ylabel('I_D (mA)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('MOSFET de enriquecimiento 2N7000 canal N')
plt.legend()
plt.grid(True)
plt.show()



# Primer gráfica

# Curvas características ID vs VSD (VGS = 0 V)
ID11 = [0.000002, 0.4, 1.5, 2.7, 3.9]
ID21 = [0.000099, 0.4, 1.6, 3.6, 6.4]

VGS = [-0.9, -1.1, -1.3, -1.5, -1.7]

plt.plot(VGS, ID21, 'o-', label='V_DS = 10V')


plt.xlabel('V_GS (V)')
plt.ylabel('I_D (mA)')
plt.title('MOSFET de enriquecimiento AO3401 canal P')
plt.legend()
plt.grid(True)
plt.show()


# Segunda gráfica
ID11 = [0.000002, 0.4, 1.5, 2.7, 3.9]
ID21 = [0.000099, 10, 22.5, 40, 62.5]

VGS = [-2, -1, -0.5, 0, 0.5]

plt.plot(VGS, ID21, 'o-', label='V_DS = 10V', color="red")


plt.xlabel('V_GS (V)')
plt.ylabel('I_D (mA)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('MOSFET de empobrecimiento canal N')
plt.legend()
plt.grid(True)
plt.show()



# Tercer gráfica
ID11 = [0.000002, 0.4, 1.5, 2.7, 3.9]
ID21 = [0.000099, 1.6, 6.4, 8.1, 22.5]

VGS = [0.9, 0.5, 0.1, 0, -0.6]

plt.plot(VGS, ID21, 'o-', label='V_DS = 10V')


plt.xlabel('V_GS (V)')
plt.ylabel('I_D (mA)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('MOSFET de empobrecimiento canal P')
plt.legend()
plt.grid(True)
plt.show()