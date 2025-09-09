import matplotlib.pyplot as plt

# ===== Conjunto A (tu línea actual) =====
Iz_pos_mA_A = [0.05,0.1,0.5,1,5,10,15,20,30,50]
Vz_pos_mV_A = [300,400,600,700,700,700,795,804,818,835]
I_pos_A_A   = [i*1e-3 for i in Iz_pos_mA_A]
V_pos_V_A   = [v*1e-3 for v in Vz_pos_mV_A]

Iz_neg_mA_A = [0.05,0.1,0.5,1,5,10,15,20,30,50]
Vz_neg_V_A  = [5.29,5.39,5.45,5.45,5.47,5.49,5.50,5.52,5.55,5.60]
I_neg_A_A   = [-i*1e-3 for i in Iz_neg_mA_A]
V_neg_V_A   = [-v for v in Vz_neg_V_A]

# ===== Conjunto B (nuevos de tus imágenes) =====
Iz_pos_mA_B = [0.05,0.1,0.5,1,5,10,15,20,30,50]
Vz_pos_mV_B = [294,329,412,448,531,567,588,603,624,650]
I_pos_A_B   = [i*1e-3 for i in Iz_pos_mA_B]
V_pos_V_B   = [v*1e-3 for v in Vz_pos_mV_B]

Iz_neg_mA_B = [0.05,0.1,0.5,1,5,10,15,20,30,50]
Vz_neg_V_B  = [5.481,5.499,5.54,5.559,5.6,5.618,5.628,5.636,5.646,5.66]
I_neg_A_B   = [-i*1e-3 for i in Iz_neg_mA_B]
V_neg_V_B   = [-v for v in Vz_neg_V_B]

# ===== Normalizaciones 50/50 usando A ∪ B =====
Vneg_max     = max(abs(v) for v in (V_neg_V_A + V_neg_V_B))     # ~5.66 V
Vpos_mV_max  = max(Vz_pos_mV_A + Vz_pos_mV_B)                   # ~835 mV
Ineg_mA_max  = max(Iz_neg_mA_A + Iz_neg_mA_B)                   # 50 mA
Ipos_mA_max  = max(Iz_pos_mA_A + Iz_pos_mA_B)                   # 50 mA

def x_display(v):
    return (-abs(v)/Vneg_max) if v < 0 else ((v*1000.0)/Vpos_mV_max)

def y_display(i):
    return -(abs(i)*1e3)/Ineg_mA_max if i < 0 else (i*1e3)/Ipos_mA_max

def curve(V_neg, I_neg, V_pos, I_pos):
    X = [x_display(v) for v in V_neg + V_pos]
    Y = [y_display(i) for i in I_neg + I_pos]
    X, Y = zip(*sorted(zip(X, Y), key=lambda t: t[0]))
    return X, Y

XA, YA = curve(V_neg_V_A, I_neg_A_A, V_pos_V_A, I_pos_A_A)
XB, YB = curve(V_neg_V_B, I_neg_A_B, V_pos_V_B, I_pos_A_B)

# ===== Ticks =====
x_ticks_left_V   = [-5.66, -5.60, -5.55, -5.50, -5.45]
x_pos_left       = [-abs(v)/Vneg_max for v in x_ticks_left_V]
x_ticks_right_mV = [0, 200, 400, 600, 800]
x_pos_right      = [m/Vpos_mV_max for m in x_ticks_right_mV]
xticks      = x_pos_left + [0] + x_pos_right[1:]
xticklabels = [f"{v:.2f} V" for v in x_ticks_left_V] + ["0"] + [f"{m} mV" for m in x_ticks_right_mV[1:]]

y_ticks_neg_mA = [-50, -20, -10, -5, -1, -0.1]
y_pos_neg      = [-abs(m)/Ineg_mA_max for m in y_ticks_neg_mA]
y_ticks_pos_mA = [0.1, 1, 5, 10, 20, 50]
y_pos_pos      = [m/Ipos_mA_max for m in y_ticks_pos_mA]
yticks      = y_pos_neg + [0] + y_pos_pos
ytlabels    = [f"{m:g} mA" for m in y_ticks_neg_mA] + ["0"] + [f"{m:g} mA" for m in y_ticks_pos_mA]

# ===== Plot =====
fig, ax = plt.subplots(figsize=(12,7))
ax.plot(XA, YA, '-o', color='orange', lw=1.8, ms=5, label='Datos prácticos')
ax.plot(XB, YB, '-s', color='blue', lw=1.8, ms=5, label='Datos Simulados')

ax.set_xticks(xticks); ax.set_xticklabels(xticklabels)
ax.set_yticks(yticks); ax.set_yticklabels(ytlabels)
ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.05, 1.05)

ax.axhline(0, color='black', lw=1); ax.axvline(0, color='black', lw=1)
ax.grid(True, ls='--', alpha=0.4)
ax.set_xlabel("Voltaje Vd (izquierda: V, derecha: mV)")
ax.set_ylabel("Corriente Id[mA]")
ax.set_title("Curva característica V-I del diodo zener")
ax.legend()
plt.tight_layout()
plt.show()
