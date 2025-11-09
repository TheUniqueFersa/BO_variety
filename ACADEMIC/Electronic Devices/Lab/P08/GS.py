import matplotlib.pyplot as plt
VSD = [0, 0.3, 0.5, 1, 2, 4, 6, 8, 10]
VDS = [0, 0.3, 0.5, 1, 2, 4, 6, 8, 10]
# Primer gráfica

# Curvas características ID vs VSD (VGS = 0 V)
ID1 = [0, 0.000003, 0.000005, 0.000010, 0.000020, 0.000040, 0.000060, 0.000080, 0.000099]
ID2 = [0, 5.1, 7.5, 10, 10, 10, 10, 10, 10]
ID3 = [0, 8.1, 12.5, 20, 22.5, 22.5, 22.5, 22.5, 22.5]
ID4 = [0, 11.1, 17.5, 30, 40, 40, 40, 40, 40]
ID5 = [0, 14.1, 22.5, 40.194, 60.091, 62.5, 62.5, 62.5, 62.5]

plt.plot(VSD, ID1, 'o-', label='V_GS = -0.9V')
plt.plot(VSD, ID2, 'o-', label='V_GS = -1.1V')
plt.plot(VSD, ID3, 'o-', label='V_GS = -1.3V')
plt.plot(VSD, ID4, 'o-', label='V_GS = -1.5V')
plt.plot(VSD, ID5, 'o-', label='V_GS = -1.7V')

plt.xlabel('V_SD (V)')
plt.ylabel('I_D (mA)')
plt.title('Curvas características del MOSFET de enriquecimiento AO3401 canal P')
plt.legend()
plt.grid(True)
plt.show()


# Segunda gráfica
ID1 = [0, 0.000003, 0.000005, 0.000010, 0.000020, 0.000040, 0.000060, 0.000080, 0.000099]
ID2 = [0, 5.1, 7.5, 10, 10, 10, 10, 10, 10]
ID3 = [0, 8.1, 12.5, 20, 22.5, 22.5, 22.5, 22.5, 22.5]
ID4 = [0, 11.1, 17.5, 30, 40, 40, 40, 40, 40]
ID5 = [0, 14.1, 22.5, 40.194, 60.091, 62.5, 62.5, 62.5, 62.5]

plt.plot(VSD, ID1, 'o-', label='V_GS = -2V')
plt.plot(VSD, ID2, 'o-', label='V_GS = -1V')
plt.plot(VSD, ID3, 'o-', label='V_GS = -0.5V')
plt.plot(VSD, ID4, 'o-', label='V_GS = 0V')
plt.plot(VSD, ID5, 'o-', label='V_GS = 0.5V')

plt.xlabel('V_DS (V)')
plt.ylabel('I_D (mA)')
plt.title('Curvas características del MOSFET de empobrecimiento de canal N')

plt.legend()
plt.grid(True)
plt.show()

# Tercer gráfica
ID1 = [0, 0.000002, 0.000005, 0.00001, 0.00002, 0.00004, 0.00006, 0.00008, 0.000099]
ID2 = [0, 1.5, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6]
ID3 = [0, 3.9, 5.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.4]
ID4 = [0, 4.5, 6.5, 8.1, 8.1, 8.1, 8.1, 8.1, 8.1]
ID5 = [0, 8.1, 12.5, 20, 22.5, 22.5, 22.5, 22.5, 22.5]

#plt.plot(Vsd, ID1, color='red', label='VGS = 0.9[V]', marker='o')

plt.plot(VSD, ID1, 'o-', label='V_GS = 0.9V')
plt.plot(VSD, ID2, 'o-', label='V_GS = 0.5V')
plt.plot(VSD, ID3, 'o-', label='V_GS = 0.1V')
plt.plot(VSD, ID4, 'o-', label='V_GS = 0V')
plt.plot(VSD, ID5, 'o-', label='V_GS = -0.6V')

plt.xlabel('V_SD (V)')
plt.ylabel('I_D (mA)')
plt.title('Curvas características del MOSFET de empobrecimiento de canal P')

plt.legend()
plt.grid(True)
plt.show()

