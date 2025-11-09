import matplotlib.pyplot as plt

# ===== Datos Prácticos =====
I_mA_A = [0.05, 0.1, 0.5, 1, 5, 10, 15, 20, 30, 50]          # mA
V_mV_A = [450, 437, 547, 579, 654, 685, 709, 717, 736, 760]  # mV
I_A_dir = [i*1e-3 for i in I_mA_A]                           # A
V_A_dir = [v*1e-3 for v in V_mV_A]                           # V

I_uA_A = [0.01, 0.0151, 0.02, 0.0251, 0.03]  # µA
V_V_A  = [9.91, 14.97, 19.88, 24.9, 29.8]    #  V
I_A_inv = [-i*1e-6 for i in I_uA_A]          #  A
V_A_inv = [-v for v in V_V_A]                #  V

# ===== Conjunto B (tus nuevas tablas) =====
# Verde: fila1 = corriente (mA), fila2 = voltaje (mV)
I_mA_B = [0.05, 0.1, 0.5, 1, 5, 10, 15, 20, 30, 50]          # mA
V_mV_B = [408, 443, 527, 563, 646, 682, 703, 718, 739, 766]  # mV
I_B_dir = [i*1e-3 for i in I_mA_B]                           # A
V_B_dir = [v*1e-3 for v in V_mV_B]                           # V

# Tabla inversa: fila1 = corriente (A), fila2 = voltaje (V)
# En tu imagen la corriente es -0.0188 (µA). La llevo a amperes.
I_B_inv = [-(0.0188e-6)]*5                                   # A
V_B_inv = [-10, -15, -20, -25, -30]                          # V

# ===== Eje X híbrido (mitad V izq / mitad mV der) =====
Vneg_max    = max(abs(v) for v in (V_A_inv + V_B_inv))       # para normalizar lado negativo
Vpos_mV_max = max(V_mV_A + V_mV_B)                           # para normalizar lado positivo (mV)

def x_display(v):
    return (-abs(v)/Vneg_max) if v < 0 else ((v*1000)/Vpos_mV_max)

def map_xy(Vd_list, I_list):
    return [x_display(v) for v in Vd_list], I_list

# Conjunto A
XA_inv, YA_inv = map_xy(V_A_inv, I_A_inv)
XA_dir, YA_dir = map_xy(V_A_dir, I_A_dir)
XA = XA_inv + XA_dir
YA = YA_inv + YA_dir
XA, YA = zip(*sorted(zip(XA, YA)))

# Conjunto B
XB_inv, YB_inv = map_xy(V_B_inv, I_B_inv)
XB_dir, YB_dir = map_xy(V_B_dir, I_B_dir)
XB = XB_inv + XB_dir
YB = YB_inv + YB_dir
XB, YB = zip(*sorted(zip(XB, YB)))

# ===== Ticks personalizados =====
ticks_left_V   = [-30, -25, -20, -15, -10]
pos_left  = [-abs(v)/Vneg_max for v in ticks_left_V]
ticks_right_mV = [0, 200, 400, 600, Vpos_mV_max]
pos_right = [m/Vpos_mV_max for m in ticks_right_mV]
xticks = pos_left + [0] + pos_right[1:]
xticklabels = [f"{v} V" for v in ticks_left_V] + ["0"] + [f"{m:.0f} mV" for m in ticks_right_mV[1:]]

# ===== Plot =====
fig, ax = plt.subplots(figsize=(9,6))
ax.plot(XB, YB, '-s', linewidth=1.6, markersize=4, label="Datos simulados")  # NUEVA LÍNEA
ax.plot(XA, YA, '-o', linewidth=1.6, markersize=4, label="Datos Prácticos")


ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_xlim(-1.05, 1.05)
ax.set_xlabel("Voltaje Vd  (izquierda: V, derecha: mV)")
ax.set_ylabel("Corriente Id (A)")
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, ls='--', alpha=0.4)
ax.legend()
ax.set_title("Curva característica I-V del diodo 1N4004")
plt.tight_layout()
plt.show()
