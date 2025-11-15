import matplotlib.pyplot as plt

VSD = [0, 0.3, 0.5, 1, 2, 4, 6, 8, 10]

# EJ 1 COM
ID4 = [0, 2.7, 3.5, 3.6, 3.6, 3.6, 3.6, 3.6, 3.6]
corte = [15, 0]
sat = [0, 6]

ID4 = [0, 6, 8.5, 12, 12.1, 12.1, 12.1, 12.1, 12.1]
# 6, 9, 13, 14.1, 16.1, 18.1, 20.1, 22.1
corte = [15, 0]
sat = [0, 36.3]
#Q_1 = [6, 3.6]

# Plotting the curves
#plt.plot(VSD, ID1, 'o-', label='V_GS = 1.5[V]')
#plt.plot(VSD, ID2, 'o-', label='V_GS = 1.6[V]')

#plt.plot(VSD, ID4, 'o-', label='V_GS = -1.5[V]')
plt.plot(VSD, ID4, 'o-', label='V_GS = -2[V]')

#plt.plot(VSD, ID4, 'o-', label='V_GS = 1.8[V]')
#plt.plot(VSD, ID5, 'o-', label='V_GS = 1.9[V]')

#plt.plot(VDS, ID6, 'o-', label='V_GS = 2.0[V]')



#plt.plot(VGS_corte_sat, ID_corte_sat, 'o-', label='Recta de carga')
plt.plot([corte[0], sat[0]], [corte[1], sat[1]], 'o-', label='Recta de carga')


plt.xlabel('V_SD (V)')
plt.ylabel('I_D (mA)')
plt.title('Curva característica del P-MOSFET y su recta de carga')

plt.legend()
plt.grid(True)
plt.show()
