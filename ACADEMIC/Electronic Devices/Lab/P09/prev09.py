import matplotlib.pyplot as plt

VDS = [0, 0.3, 0.5, 1, 2, 4, 6, 8, 10]

# Drain current values from the table
ID1 = [0.06146, 0.0668, 0.07462, 0.08335, 0.09397, 0.1029, 0.10995, 0.1176]
ID2 = [0.252, 0.2815, 0.318, 0.3566, 0.393, 0.4235, 0.4486, 0.4752]
ID3 = [0, 0.734, 0.7903, 0.885, 0.9866, 1.098, 1.177, 1.248, 1.325]
ID4 = [1.76, 2.015, 2.22, 2.46, 2.73, 2.93, 3.17, 3.43]
ID5 = [4.31, 4.76, 5.223, 5.81, 6.49, 7.27, 8.18, 8.81]
ID6 = [0, 6.31, 6.89, 7.69, 8.5, 9.45, 10.76, 11.775, 13.218]


# Plotting the curves
#plt.plot(VSD, ID1, 'o-', label='V_GS = 1.5[V]')
#plt.plot(VSD, ID2, 'o-', label='V_GS = 1.6[V]')

plt.plot(VDS, ID3, 'o-', label='V_GS = 8[V]')

#plt.plot(VSD, ID4, 'o-', label='V_GS = 1.8[V]')
#plt.plot(VSD, ID5, 'o-', label='V_GS = 1.9[V]')

#plt.plot(VDS, ID6, 'o-', label='V_GS = 2.0[V]')


VGS_corte_sat = [15, 0]
ID_corte_sat = [0, 25.2318]

VGS_corte_sat_1 = [15, 0]
ID_corte_sat_1 = [0, 2.6736]

#plt.plot(VGS_corte_sat, ID_corte_sat, 'o-', label='Recta de carga')
plt.plot(VGS_corte_sat_1, ID_corte_sat_1, 'o-', label='Recta de carga')

plt.xlabel('V_DS (V)')
plt.ylabel('I_D (mA)')
plt.title('Curva característica del MOSFET y su recta de carga')

plt.legend()
plt.grid(True)
plt.show()
