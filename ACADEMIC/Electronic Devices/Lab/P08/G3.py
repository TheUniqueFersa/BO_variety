import matplotlib.pyplot as plt
VSD = [0, 0.3, 0.5, 1, 2, 4, 6, 8, 10]
VDS = [0, 0.3, 0.5, 1, 2, 4, 6, 8, 10]

# Tercer gráfica
ID1 = [0, 0.000002, 0.000005, 0.00001, 0.00002, 0.00004, 0.00006, 0.00008, 0.000099]
ID2 = [0, 1.5, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6]
ID3 = [0, 3.9, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4]
ID4 = [0, 4.5, 6.5, 8.1, 8.1, 8.1, 8.1, 8.1, 8.1]
ID5 = [0, 8.1, 12.5, 20, 22.5, 22.5, 22.5, 22.5, 22.5]



#plt.plot(Vsd, ID1, color='red', label='VGS = 0.9[V]', marker='o')

plt.plot(VSD, ID1, 'o-', label='V_GS = ')
plt.plot(VSD, ID2, 'o-', label='V_GS = ')
plt.plot(VSD, ID3, 'o-', label='V_GS = ')
plt.plot(VSD, ID4, 'o-', label='V_GS = ')
plt.plot(VSD, ID5, 'o-', label='V_GS = ')

plt.xlabel('V_SD (V)')
plt.ylabel('I_D (mA)')
plt.title('Curvas características del MOSFET de empobrecimiento de canal P')

plt.legend()
plt.grid(True)
plt.show()
